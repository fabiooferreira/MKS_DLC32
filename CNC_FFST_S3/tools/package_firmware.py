"""Merge a complete ESP32-S3 image and generate its matching single-file Python.
Run using the build venv with esptool 4.8.1, after successful PlatformIO builds.
"""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import shutil
import struct
import subprocess
import sys
import textwrap
import zlib

ROOT=Path(__file__).resolve().parents[1]
VERSION='CNC_FFST-S3-0.1.0'

def image_digest(data):
    if len(data)<24 or data[0]!=0xe9 or data[23]!=1 or struct.unpack_from('<H',data,12)[0]!=9:
        raise ValueError('Expected an ESP32-S3 image with appended SHA256')
    pos,checksum=24,0xef
    for _ in range(data[1]):
        if pos+8>len(data):raise ValueError('Truncated image')
        length=struct.unpack_from('<I',data,pos+4)[0];pos+=8
        if pos+length>len(data):raise ValueError('Truncated segment')
        for b in data[pos:pos+length]:checksum^=b
        pos+=length
    end=((pos+16)//16)*16
    digest=hashlib.sha256(data[:end]).digest()
    if end>len(data) or data[end-1]!=checksum or data[end:end+32]!=digest:
        raise ValueError('ESP32-S3 checksum/digest mismatch')
    return digest.hex()

def package(profile):
    profile=profile.upper();environment='cnc_ffst_s3_n16r8_'+profile.lower()
    built=ROOT/'firmware/.pio/build'/environment
    destination=ROOT/'artifacts'/profile
    config=(ROOT/'firmware'/('sdkconfig.'+environment)).read_text()
    for flag in ['CONFIG_SECURE_BOOT=y','CONFIG_SECURE_FLASH_ENC_ENABLED=y']:
        if flag in config.splitlines():raise ValueError('This packaging tool only accepts non-provisioning bench builds')
    for flag in ['CONFIG_ESPTOOLPY_FLASHSIZE_16MB=y','CONFIG_SPIRAM_MODE_OCT=y','CONFIG_SPIRAM_SIZE=8388608']:
        if flag not in config.splitlines():raise ValueError('N16R8 configuration mismatch: '+flag)
    destination.mkdir(parents=True,exist_ok=True)
    name=f'CNC_FFST_S3_0.1.0_{profile}_FULL_16MB.bin'
    binary=destination/name
    subprocess.run([sys.executable,'-m','esptool','--chip','esp32s3','merge_bin',
        '--flash_mode','dio','--flash_freq','40m','--flash_size','16MB','--fill-flash-size','16MB',
        '--output',str(binary),
        '0x0',str(built/'bootloader.bin'),'0x8000',str(built/'partitions.bin'),
        '0xd000',str(built/'ota_data_initial.bin'),'0x10000',str(built/'firmware.bin')],check=True)
    app=(built/'firmware.bin').read_bytes();full=binary.read_bytes()
    if len(full)!=16*1024*1024 or full[0x10000:0x10000+len(app)]!=app:
        raise ValueError('Merged image size/application mismatch')
    identity={'protocol':1,'firmware':VERSION,'app_image_sha256':image_digest(app),
              'application_file_sha256':hashlib.sha256(app).hexdigest()}
    prefix,suffix=b'FFST_SHAREDKEY1:',b':FFST_KEY_END'
    if full.count(prefix)!=1:raise ValueError('Credential record missing/duplicated')
    start=full.index(prefix)+len(prefix)
    if full[start+32:start+32+len(suffix)]!=suffix:raise ValueError('Invalid credential record')
    seed=ROOT/'.private/shared_key.bin'
    if seed.is_file() and full[start:start+32]!=seed.read_bytes():raise ValueError('Credential changed')
    target=ROOT/'python'/profile
    target.mkdir(parents=True,exist_ok=True)
    shutil.copy2(binary,target/name)
    (target/'firmware_identity.json').write_text(json.dumps(identity,indent=2)+'\n')
    (destination/'firmware_identity.json').write_text(json.dumps(identity,indent=2)+'\n')
    (destination/'sdkconfig.used').write_text(config)
    for src,dst in [('firmware.bin','firmware_app_0x10000.bin'),('bootloader.bin','bootloader_0x0.bin'),
                    ('partitions.bin','partitions_0x8000.bin'),('firmware.elf','firmware.elf')]:
        shutil.copy2(built/src,destination/dst)
    auth=(ROOT/'python/cnc_ffst_auth_source.py').read_text()
    auth=auth.replace('CNC_FFST_0.3.0_FULL_4MB.bin',name).replace('CNC_FFST 0.3.0',VERSION)
    (target/'cnc_ffst_auth.py').write_text(auth,encoding='utf-8')
    auth=auth[:auth.index("if __name__ == '__main__':")]
    auth=auth.replace("path = Path(path or Path(__file__).with_name('"+name+"'))",
                      'path = Path(path) if path is not None else None')
    auth=auth.replace('data = path.read_bytes()',
                      'data = path.read_bytes() if path else zlib.decompress(base64.b85decode(_firmware_blob))')
    auth=auth.replace("path = Path(identity_path or Path(__file__).with_name('firmware_identity.json'))",
                      'path = Path(identity_path) if identity_path is not None else None')
    auth=auth.replace("identity = json.loads(path.read_text(encoding='utf-8'))",
                      'identity = json.loads(path.read_text(encoding="utf-8")) if path else _firmware_identity')
    blob=base64.b85encode(zlib.compress(full,9)).decode()
    resource='\n'.join('        '+repr(line).replace("'","b'",1) for line in textwrap.wrap(blob,100,break_on_hyphens=False))
    factory='''def _create_embedded_auth():
    import base64
    import zlib
    import types
    _firmware_blob = (
'''+resource+'''\n    )
    _firmware_identity = '''+repr(identity)+'\n'+textwrap.indent(auth,'    ')+'''
    return types.SimpleNamespace(open_authenticated=open_authenticated, SignedPort=SignedPort,
        SAFE_REALTIME=SAFE_REALTIME, load_key=load_key, verify_firmware=verify_firmware,
        mac=mac, exchange=exchange)
_ffst_auth = _create_embedded_auth()
open_authenticated = _ffst_auth.open_authenticated
SAFE_REALTIME = _ffst_auth.SAFE_REALTIME
'''
    app_source=(ROOT/'python/controlador_pcb_source.py').read_text()
    original='from cnc_ffst_auth import open_authenticated, SAFE_REALTIME'
    if original not in app_source:raise ValueError('Client auth import not found')
    app_source=app_source.replace(original,factory)
    compile(app_source,'CNC_FFST_Unico.py','exec')
    (target/'CNC_FFST_Unico.py').write_text(app_source,encoding='utf-8')
    manifest={'firmware':VERSION,'profile':profile,'environment':environment,'chip':'esp32s3',
        'flash_mb':16,'psram_mb':8,'step_pulse_us':5,'direction_setup_delay_us':2,'file':name,'offset':0,'sha256':hashlib.sha256(full).hexdigest(),
        'authentication':'FFST HMAC v1, shared existing credential','flash_encryption':False,
        'secure_boot':False,'efuse_changes':False,'hardware_tested':False,**identity}
    (destination/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (destination/'SHA256SUMS').write_text(manifest['sha256']+'  '+name+'\n')
    print('Packaged',profile,identity['app_image_sha256'])

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('profile',choices=['uart','usb'])
    package(parser.parse_args().profile)
