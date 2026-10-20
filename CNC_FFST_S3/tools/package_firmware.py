"""Merge a complete ESP32-S3 image and generate its matching single-file Python.
Run using the build venv with esptool 4.8.1, after successful PlatformIO builds.
"""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import os
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
    protected=profile=='PROTECTED'
    version='CNC_FFST-S3-0.2.0-PROTECTED' if protected else VERSION
    table_offset,ota_offset,app_offset=(0x20000,0x25000,0x30000) if protected else (0x8000,0xd000,0x10000)
    built=ROOT/'firmware/.pio/build'/environment
    destination=ROOT/'artifacts'/profile
    config=(ROOT/'firmware'/('sdkconfig.'+environment)).read_text()
    for flag in ['CONFIG_SECURE_BOOT=y','CONFIG_SECURE_FLASH_ENC_ENABLED=y']:
        if not protected and flag in config.splitlines():raise ValueError('This packaging tool only accepts non-provisioning bench builds')
    for flag in ['CONFIG_ESPTOOLPY_FLASHSIZE_16MB=y','CONFIG_SPIRAM_MODE_OCT=y','CONFIG_SPIRAM_SIZE=8388608']:
        if flag not in config.splitlines():raise ValueError('N16R8 configuration mismatch: '+flag)
    if protected:
        for flag in ['CONFIG_SECURE_BOOT_V2_ENABLED=y','CONFIG_SECURE_FLASH_ENCRYPTION_MODE_RELEASE=y',
                     'CONFIG_SECURE_FLASH_ENCRYPTION_AES256=y','CONFIG_SECURE_ENABLE_SECURE_ROM_DL_MODE=y']:
            if flag not in config.splitlines():raise ValueError('Protected config missing: '+flag)
        if 'CONFIG_SECURE_DISABLE_ROM_DL_MODE=y' in config.splitlines():raise ValueError('Updates require secure download mode')
    destination.mkdir(parents=True,exist_ok=True)
    name=f'CNC_FFST_S3_{"0.2.0" if protected else "0.1.0"}_{profile}_FULL_16MB.bin'
    boot_file,app_file=built/'bootloader.bin',built/'firmware.bin'
    if protected:
        key=Path(os.environ.get('FFST_SIGNING_KEY',str(ROOT/'firmware/ffst_secure_boot_signing_key.pem')))
        public=destination/'secure_boot_public_key.pem'
        subprocess.run([sys.executable,'-m','espsecure','extract_public_key','--version','2','--keyfile',str(key),str(public)],check=True)
        normalized=destination/'bootloader_params.bin'
        subprocess.run([sys.executable,'-m','esptool','--chip','esp32s3','merge_bin',
            '--flash_mode','dio','--flash_freq','40m','--flash_size','16MB',
            '--output',str(normalized),'0x0',str(boot_file)],check=True)
        boot_file=normalized
        signed=[]
        for source in [boot_file,app_file]:
            content=source.read_bytes();padded=destination/(source.stem+'_padded.bin');target=destination/(source.stem+'_signed.bin')
            padded.write_bytes(content+b'\xff'*((-len(content))%65536))
            subprocess.run([sys.executable,'-m','espsecure','sign_data','--version','2','--keyfile',str(key),'--output',str(target),str(padded)],check=True)
            subprocess.run([sys.executable,'-m','espsecure','verify_signature','--version','2','--keyfile',str(public),str(target)],check=True)
            padded.unlink();signed.append(target)
        boot_file,app_file=signed
    binary=destination/name
    subprocess.run([sys.executable,'-m','esptool','--chip','esp32s3','merge_bin',
        '--flash_mode','keep' if protected else 'dio','--flash_freq','keep' if protected else '40m',
        '--flash_size','keep' if protected else '16MB','--fill-flash-size','16MB',
        '--output',str(binary),
        '0x0',str(boot_file),hex(table_offset),str(built/'partitions.bin'),
        hex(ota_offset),str(built/'ota_data_initial.bin'),hex(app_offset),str(app_file)],check=True)
    app=app_file.read_bytes();full=binary.read_bytes()
    if len(full)!=16*1024*1024 or full[app_offset:app_offset+len(app)]!=app:
        raise ValueError('Merged image size/application mismatch')
    identity={'protocol':1,'firmware':version,'app_image_sha256':image_digest(app),
              'application_file_sha256':hashlib.sha256(app).hexdigest()}
    prefix,suffix=b'FFST_SHAREDKEY1:',b':FFST_KEY_END'
    if full.count(prefix)!=1:raise ValueError('Credential record missing/duplicated')
    start=full.index(prefix)+len(prefix)
    if full[start+32:start+32+len(suffix)]!=suffix:raise ValueError('Invalid credential record')
    seed=ROOT/'.private/shared_key.bin'
    if seed.is_file() and full[start:start+32]!=seed.read_bytes():raise ValueError('Credential changed')
    target=ROOT/'python'/profile
    target.mkdir(parents=True,exist_ok=True)
    if not protected:shutil.copy2(binary,target/name)
    (target/'firmware_identity.json').write_text(json.dumps(identity,indent=2)+'\n')
    (destination/'firmware_identity.json').write_text(json.dumps(identity,indent=2)+'\n')
    (destination/'sdkconfig.used').write_text(config)
    for src,dst in [('firmware.bin',f'firmware_app_unsigned_{hex(app_offset)}.bin' if protected else 'firmware_app_0x10000.bin'),
                    ('bootloader.bin','bootloader_unsigned_0x0.bin' if protected else 'bootloader_0x0.bin'),
                    ('partitions.bin',f'partitions_{hex(table_offset)}.bin'),('firmware.elf','firmware.elf')]:
        shutil.copy2(built/src,destination/dst)
    if protected:
        shutil.copy2(app_file,destination/'firmware_update_signed.bin')
        if boot_file!=destination/'bootloader_signed.bin':shutil.copy2(boot_file,destination/'bootloader_signed.bin')
    auth=(ROOT/'python/cnc_ffst_auth_source.py').read_text()
    auth=auth.replace('CNC_FFST_0.3.0_FULL_4MB.bin',name).replace('CNC_FFST 0.3.0',version)
    if not protected:(target/'cnc_ffst_auth.py').write_text(auth,encoding='utf-8')
    auth=auth[:auth.index("if __name__ == '__main__':")]
    auth=auth.replace("path = Path(path or Path(__file__).with_name('"+name+"'))",
                      'path = Path(path) if path is not None else None')
    auth=auth.replace('data = path.read_bytes()',
                      'data = path.read_bytes() if path else zlib.decompress(base64.b85decode(_firmware_blob))')
    auth=auth.replace("path = Path(identity_path or Path(__file__).with_name('firmware_identity.json'))",
                      'path = Path(identity_path) if identity_path is not None else None')
    auth=auth.replace("identity = json.loads(path.read_text(encoding='utf-8'))",
                      'identity = json.loads(path.read_text(encoding="utf-8")) if path else _firmware_identity')
    embedded=(prefix+full[start:start+32]+suffix) if protected else full
    blob=base64.b85encode(zlib.compress(embedded,9)).decode()
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
    if protected:app_source=app_source.replace('S3 0.1.0 — Controlador PCB autenticado','S3 0.2.0 protegido — Controlador PCB autenticado')
    original='from cnc_ffst_auth import open_authenticated, SAFE_REALTIME'
    if original not in app_source:raise ValueError('Client auth import not found')
    app_source=app_source.replace(original,factory)
    compile(app_source,'CNC_FFST_Unico.py','exec')
    (target/'CNC_FFST_Unico.py').write_text(app_source,encoding='utf-8')
    (target/'Fabricação Fresa Laser.py').write_text(app_source,encoding='utf-8')
    manifest={'firmware':version,'profile':profile,'environment':environment,'chip':'esp32s3',
        'flash_mb':16,'psram_mb':8,'step_pulse_us':5,'direction_setup_delay_us':2,'file':name,'offset':0,'sha256':hashlib.sha256(full).hexdigest(),
        'application_offset':app_offset,'partition_offset':table_offset,
        'authentication':'FFST HMAC v1, shared existing credential','flash_encryption':protected,
        'secure_boot':protected,'efuse_changes':protected,'secure_download':protected,
        'client_embeds_firmware':not protected,
        'update_file':'firmware_update_signed.bin' if protected else None,
        'update_sha256':hashlib.sha256(app).hexdigest() if protected else None,'hardware_tested':False,**identity}
    if protected:
        manifest['signing_public_sha256']=hashlib.sha256(public.read_bytes()).hexdigest()
        manifest['update_size']=len(app)
    (destination/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (destination/'SHA256SUMS').write_text(manifest['sha256']+'  '+name+'\n')
    print('Packaged',profile,identity['app_image_sha256'])

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('profile',choices=['uart','usb','protected'])
    package(parser.parse_args().profile)
