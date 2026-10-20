"""No hardware: production orchestration with fake serial, real keys and ciphertext tests elsewhere."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT/'installer/Instalador_CNC_FFST_S3.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ART = ROOT/'artifacts/PROTECTED'
MAN = json.loads((ART/'manifest.json').read_text())
BIN = ART/MAN['file']
META = {'protected': True, 'app_offset': MAN['application_offset'],
    'partition_offset': MAN['partition_offset'], 'app_image_sha256': MAN['app_image_sha256'],
    'signing_public_sha256': MAN['signing_public_sha256'], 'update_size': MAN['update_size']}
m.KNOWN_IMAGES[MAN['sha256']] = META
MAC='1234567890ab'


def fresh():
    return {name: {'value': 'USER' if name.startswith('KEY_PURPOSE') else 0} for name in m.SECURITY_FIELDS}


class Fake(m.Backend):
    def __init__(self):
        super().__init__(lambda s: None)
        self.commands=[]; self.fields=fresh(); self.reports=[]
    def command(self,args):
        self.commands.append(args)
        if 'chip_id' in args: return 'Chip is ESP32-S3\nMAC: 12:34:56:78:90:ab'
        if 'flash_id' in args: return 'Detected flash size: 16MB'
        if 'summary' in args: return json.dumps(self.fields)
        if 'get_security_info' in args: return 'Secure Boot: Enabled\nFlash Encryption: Enabled'
        return 'OK'
    def verify_protection(self,port,path,require_image=True):
        self.reports.append(require_image)
        return {'mac':MAC,'maintenance_safe':1}
    @staticmethod
    def check_owner_key(vault, metadata):
        pass # Real owner key check exercised separately below.


class Tests(unittest.TestCase):
    def folders(self,tmp):
        vault,backup=Path(tmp)/'keys',Path(tmp)/'backup'
        vault.mkdir();backup.mkdir()
        (vault/'secure_boot_signing_key.pem').write_bytes(b'fixture-owner-key')
        return vault,backup
    def test_customer_client_does_not_embed_firmware(self):
        import ast,base64,zlib
        text=(ROOT/'python/PROTECTED/CNC_FFST_Unico.py').read_text()
        tree=ast.parse(text)
        factory=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='_create_embedded_auth')
        assignment=next(n for n in factory.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='_firmware_blob' for t in n.targets))
        embedded=zlib.decompress(base64.b85decode(ast.literal_eval(assignment.value)))
        self.assertTrue(embedded.startswith(b'FFST_SHAREDKEY1:'))
        self.assertTrue(embedded.endswith(b':FFST_KEY_END'))
        self.assertEqual(len(embedded),len(b'FFST_SHAREDKEY1:')+32+len(b':FFST_KEY_END'))
        self.assertNotIn('BEGIN PRIVATE KEY',text)
    def test_signed_full_image_validates(self):
        self.assertEqual(m.validate_image(BIN),MAN['sha256'])
    def test_protected_bin_refused_in_reversible_mode(self):
        backend=Fake()
        with self.assertRaises(ValueError): backend.install('COM7',BIN,False)
        self.assertEqual(backend.commands,[])
    def test_missing_backup_prevents_burn(self):
        backend=Fake()
        with self.assertRaises(ValueError): backend.install('COM7',BIN,True)
        self.assertFalse(any('burn_key' in c for c in backend.commands))
    def test_existing_security_prevents_burn(self):
        backend=Fake();backend.fields['SPI_BOOT_CRYPT_CNT']['value']=7
        with self.assertRaises(ValueError): backend.install('COM7',BIN,True)
        self.assertFalse(any('burn_key' in c for c in backend.commands))
    def test_initial_sequence_keys_backup_then_write_no_boot(self):
        backend=Fake()
        with tempfile.TemporaryDirectory() as tmp:
            vault,backup=self.folders(tmp)
            backend.install('COM7',BIN,True,vault,backup)
            self.assertEqual((vault/MAC/'flash_key.bin').read_bytes(),(backup/MAC/'flash_key.bin').read_bytes())
            self.assertEqual(len((vault/MAC/'flash_key.bin').read_bytes()),64)
            state=json.loads((vault/MAC/'device.json').read_text())
            self.assertEqual(state['phase'],'pending_first_boot')
            commands=backend.commands
            burn=next(i for i,c in enumerate(commands) if 'burn_key' in c)
            write=next(i for i,c in enumerate(commands) if 'write_flash' in c)
            self.assertLess(burn,write)
            self.assertIn('XTS_AES_256_KEY_1',commands[burn]);self.assertIn('XTS_AES_256_KEY_2',commands[burn])
            for c in commands[write:]:
                self.assertIn('no_reset',c);self.assertNotIn('hard_reset',c);self.assertNotIn('--force',c)
    def test_distinct_boards_get_distinct_keys(self):
        backend=Fake()
        with tempfile.TemporaryDirectory() as tmp:
            vault,backup=self.folders(tmp)
            a=backend.prepare_keys(MAC,vault,backup,META)
            b=backend.prepare_keys('abcdef123456',vault,backup,META)
            self.assertNotEqual((a/'flash_key.bin').read_bytes(),(b/'flash_key.bin').read_bytes())
            with self.assertRaises(ValueError): backend.prepare_keys(MAC,vault,backup,META)
    def test_overlapping_backup_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError): Fake().prepare_keys(MAC,tmp,Path(tmp)/'sub',META)
    def test_update_only_writes_encrypted_application(self):
        backend=Fake()
        with tempfile.TemporaryDirectory() as tmp:
            vault,backup=self.folders(tmp);backend.prepare_keys(MAC,vault,backup,META)
            backend.update_protected('COM7',BIN,vault)
            write=next(c for c in backend.commands if 'write_flash' in c)
            self.assertEqual(write[-2],hex(META['app_offset']))
            self.assertTrue(write[-1].endswith('application_encrypted.bin'))
            self.assertIn('--force',write);self.assertNotIn('--encrypt',write)
            self.assertFalse(any('burn_key' in c for c in backend.commands))
            self.assertEqual(backend.reports,[False,True])
    def test_wrong_local_key_blocks_update(self):
        backend=Fake()
        with tempfile.TemporaryDirectory() as tmp:
            vault,backup=self.folders(tmp);backend.prepare_keys(MAC,vault,backup,META)
            (vault/MAC/'flash_key.bin').write_bytes(b'x'*64)
            with self.assertRaises(ValueError):backend.update_protected('COM7',BIN,vault)
            self.assertEqual(backend.commands,[])
    def test_owner_private_key_not_optional(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):m.Backend.check_owner_key(tmp,META)
    def test_owner_key_matches_built_image(self):
        key=ROOT/'firmware/ffst_secure_boot_signing_key.pem'
        if not key.exists(): self.skipTest('Local signing key intentionally excluded from source delivery')
        import shutil
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy2(key,Path(tmp)/'secure_boot_signing_key.pem')
            m.Backend.check_owner_key(tmp,META)


class SecurityReportTests(unittest.TestCase):
    def report(self, change=None):
        import serial,hmac,types
        blob=BIN.read_bytes();start=blob.index(b'FFST_SHAREDKEY1:')+len(b'FFST_SHAREDKEY1:');key=blob[start:start+32]
        class Port:
            def __enter__(self): return self
            def __exit__(self,*args): pass
            def reset_input_buffer(self): pass
            def write(self,command):
                nonce=command.decode().strip().split('=')[1]
                self.status={'nonce':nonce,'mac':MAC,'appsha':MAN['app_image_sha256'],
                    'encryption_release':1,'secure_boot':1,'secure_download':1,
                    'jtag_disabled':1,'keys_read_protected':1,'maintenance_safe':1}
                if change:change(self.status)
            def readline(self):
                payload=json.dumps(self.status,separators=(',',':')).encode()
                tag=hmac.digest(key,b'security|'+payload,'sha256').hex()
                return ('[FFSEC:'+payload.hex()+':'+tag+']\n').encode()
        backend=m.Backend(lambda s:None)
        with patch.object(serial,'Serial',return_value=Port()),patch('time.sleep'):
            return backend.verify_protection('COM7',BIN)
    def test_fresh_authenticated_security_report(self):
        self.assertEqual(self.report()['mac'],MAC)
    def test_old_security_response_rejected(self):
        with self.assertRaises(ValueError):self.report(lambda s:s.update(nonce='0'*32))
    def test_incomplete_protection_rejected(self):
        with self.assertRaises(ValueError):self.report(lambda s:s.update(keys_read_protected=0))
    def test_wrong_application_hash_rejected(self):
        with self.assertRaises(ValueError):self.report(lambda s:s.update(appsha='0'*64))


if __name__=='__main__':unittest.main(verbosity=2)
