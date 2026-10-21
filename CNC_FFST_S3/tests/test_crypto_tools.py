from pathlib import Path
import tempfile,subprocess,json,secrets,sys,hashlib
r=Path(__file__).resolve().parents[1];app=r/'artifacts/PROTECTED/firmware_update_signed.bin'
def run(module,args):
 p=subprocess.run([sys.executable,'-m',module,*args],capture_output=True,text=True)
 if p.returncode:raise RuntimeError(p.stdout+p.stderr)
 return p.stdout
with tempfile.TemporaryDirectory() as tmp:
 t=Path(tmp);key=secrets.token_bytes(64)
 (t/'key.bin').write_bytes(key);(t/'part1.bin').write_bytes(key[:32]);(t/'part2.bin').write_bytes(key[32:])
 (t/'other.bin').write_bytes(secrets.token_bytes(64))
 base=['--chip','esp32s3','--virt','--path-efuse-file',str(t/'efuses.bin'),'--do-not-confirm']
 run('espefuse',base+['burn_key','BLOCK_KEY0',str(t/'part1.bin'),'XTS_AES_256_KEY_1',
                    'BLOCK_KEY1',str(t/'part2.bin'),'XTS_AES_256_KEY_2'])
 output=run('espefuse',base+['summary','--format','json','KEY_PURPOSE_0','KEY_PURPOSE_1','BLOCK_KEY0','BLOCK_KEY1'])
 data,_=json.JSONDecoder().raw_decode(output[output.index('{'):])
 for n in ('BLOCK_KEY0','BLOCK_KEY1'):
  assert data[n]['readable'] is False and data[n]['writeable'] is False,data[n]
 assert data['KEY_PURPOSE_0']['value']=='XTS_AES_256_KEY_1'
 assert data['KEY_PURPOSE_1']['value']=='XTS_AES_256_KEY_2'
 print('PASS: virtual eFuses AES256 purposes and read/write key protection (no physical chip).')
 run('espsecure',['encrypt_flash_data','--aes_xts','--keyfile',str(t/'key.bin'),'--address','0x30000','--output',str(t/'cipher.bin'),str(app)])
 run('espsecure',['decrypt_flash_data','--aes_xts','--keyfile',str(t/'key.bin'),'--address','0x30000','--output',str(t/'plain.bin'),str(t/'cipher.bin')])
 assert (t/'plain.bin').read_bytes()==app.read_bytes()
 run('espsecure',['decrypt_flash_data','--aes_xts','--keyfile',str(t/'other.bin'),'--address','0x30000','--output',str(t/'wrong.bin'),str(t/'cipher.bin')])
 assert (t/'wrong.bin').read_bytes()!=app.read_bytes()
 print('PASS: real espsecure AES-XTS roundtrip at update offset; another key cannot recover the application.')
 # Signature verification uses the exact bootloader bytes that will be written.
 full=(r/'artifacts/PROTECTED/CNC_FFST_S3_0.2.3_PROTECTED_FULL_16MB.bin').read_bytes()
 boot=r/'artifacts/PROTECTED/bootloader_signed.bin'
 assert full[:len(boot.read_bytes())]==boot.read_bytes()
 run('espsecure',['verify_signature','--version','2','--keyfile',str(r/'artifacts/PROTECTED/secure_boot_public_key.pem'),str(boot)])
 run('espsecure',['verify_signature','--version','2','--keyfile',str(r/'artifacts/PROTECTED/secure_boot_public_key.pem'),str(app)])
 print('PASS: signed bootloader and application verified, merged bootloader identical to signed bytes.')
