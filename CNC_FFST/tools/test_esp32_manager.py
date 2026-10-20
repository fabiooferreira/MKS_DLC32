"""Meaningful manager tests. USB is simulated; eFuse JSON uses real virtual espefuse.
Run with the manager tool venv: python tools/test_esp32_manager.py
Set DISPLAY for the optional real Tk GUI test.
"""
import copy
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('manager', ROOT / 'python/Gerenciador_ESP32_DLC32.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def report():
    fields = {name: {'value': 0 if name.startswith('FLASH_CRYPT') else False,
                      'readable': True, 'writeable': True} for name in m.FIELDS}
    return m.validate_report({'formato': 'CNC_FFST_DIAGNOSTICO_1', 'data_utc': 'test',
            'flash': '4MB', 'efuses': fields,
            'identificacao': {'mac': '00:11:22:33:44:55',
                             'chip_e_revisao': 'ESP32-D0WD-V3 (revision v3.1)', 'cristal': '40MHz'}})


def make_package(directory, version='0.3.0'):
    source = ROOT / 'artifacts' / f'CNC_FFST_{version}_FULL_4MB.bin'
    binary = Path(directory) / source.name
    shutil.copy2(source, binary)
    info = m.inspect_full(binary)
    manifest = {'format': 'CNC_FFST_PACKAGE_1', 'chip': 'esp32', 'flash_bytes': m.FLASH_BYTES,
                'offset': 0, 'file': binary.name, 'firmware': 'CNC_FFST-' + version,
                'auth': version == '0.3.0', 'flash_encryption': False,
                'sha256': info['sha256'], 'app_image_sha256': info['app']['image_sha256']}
    path = Path(directory) / 'pacote.json'
    m.write_json(path, manifest)
    return path


class FakeUSB(m.Backend):
    def __init__(self, storage, fail=None):
        super().__init__(sys.executable, storage)
        self.calls = []
        self.fail = fail
        self.current = report()

    def device(self, port):
        self.calls.append('device')
        return copy.deepcopy(self.current)

    def run(self, args, **kwargs):
        if 'read_flash' in args:
            self.calls.append('read_flash')
            Path(args[-1]).write_bytes(b'\xff' * (10 if self.fail == 'short_backup' else m.FLASH_BYTES))
            if self.fail == 'read_flash':
                raise RuntimeError('simulated backup failure')
        elif 'write_flash' in args:
            self.calls.append('write_flash')
            if self.fail == 'write_flash':
                raise RuntimeError('simulated write failure')
        elif 'verify_flash' in args:
            self.calls.append('verify_flash')
            if self.fail == 'verify_flash':
                raise RuntimeError('simulated verify failure')
        elif 'chip_id' in args:
            return 'Chip is ESP32-D0WD-V3 (revision v3.1)\nCrystal is 40MHz\nMAC: 00:11:22:33:44:55\n'
        else:
            raise AssertionError('Unexpected command: ' + repr(args))
        return ''


class ManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='cnc-manager-test-')
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_real_virtual_efuse_and_secret_filter(self):
        output = subprocess.check_output([sys.executable, '-m', 'espefuse', '--chip', 'esp32',
                   '--virt', 'summary', '--format', 'json', *m.FIELDS], text=True)
        efuses = m.parse_efuses(output)
        self.assertEqual(m.encryption_state(efuses), 'inativa')
        raw = json.loads(output[output.index('{'):])
        raw['SECRET_KEY'] = {'value': 'SENSITIVE_FIXTURE'}
        self.assertNotIn('SENSITIVE_FIXTURE', json.dumps(m.parse_efuses(json.dumps(raw))))

    def test_import_recomputes_security_and_drops_unknown_values(self):
        data = report()
        data['criptografia_flash'] = 'falsa conclusão'
        data['secret'] = 'SENSITIVE_FIXTURE'
        clean = m.validate_report(data)
        self.assertEqual(clean['criptografia_flash'], 'inativa')
        self.assertNotIn('SENSITIVE_FIXTURE', json.dumps(clean))

    def test_device_collection_saves_only_public_report(self):
        backend = m.Backend(sys.executable, self.root)
        backend.check_tools = lambda: m.VERSIONS
        chip = 'Chip is ESP32-D0WD-V3 (revision v3.1)\nCrystal is 40MHz\nMAC: 00:11:22:33:44:55\n'
        raw = report()['efuses']
        raw['SECRET_KEY'] = {'value': 'SENSITIVE_FIXTURE'}
        def run(args, **kwargs):
            if 'chip_id' in args:
                return chip
            if 'flash_id' in args:
                return 'Detected flash size: 4MB\n'
            if 'summary' in args:
                return 'espefuse\n' + json.dumps(raw)
            raise AssertionError(args)
        backend.run = run
        collected = backend.device('COM7')
        self.assertTrue(m.analyze(collected)['gravacao_normal_permitida'])
        saved = list(self.root.glob('relatorios/**/*.json'))
        self.assertEqual(len(saved), 1)
        self.assertNotIn('SENSITIVE_FIXTURE', saved[0].read_text())

    def test_device_collection_rejects_mid_query_board_change(self):
        backend = m.Backend(sys.executable, self.root)
        backend.check_tools = lambda: m.VERSIONS
        counter = [0]
        def run(args, **kwargs):
            if 'chip_id' in args:
                counter[0] += 1
                mac = '00:11:22:33:44:55' if counter[0] == 1 else '00:11:22:33:44:66'
                return 'Chip is ESP32-D0WD-V3 (revision v3.1)\nMAC: ' + mac + '\n'
            if 'flash_id' in args:
                return 'Detected flash size: 4MB\n'
            if 'summary' in args:
                return json.dumps(report()['efuses'])
            raise AssertionError(args)
        backend.run = run
        with self.assertRaises(ValueError):
            backend.device('COM7')
        self.assertFalse(list(self.root.glob('relatorios/**/*.json')))

    def test_even_encryption_count_is_not_eligible(self):
        data = report()
        data['efuses']['FLASH_CRYPT_CNT']['value'] = 3
        self.assertEqual(m.encryption_state(data['efuses']), 'inativa')
        self.assertFalse(m.analyze(data)['gravacao_normal_permitida'])

    def test_each_security_change_blocks_normal_flashing(self):
        for name in m.FIELDS:
            with self.subTest(name=name):
                data = report()
                data['efuses'][name]['value'] = 1 if name.startswith('FLASH_CRYPT') else True
                self.assertFalse(m.analyze(data)['gravacao_normal_permitida'])
        data = report()
        data['efuses']['FLASH_CRYPT_CNT']['writeable'] = False
        self.assertFalse(m.analyze(data)['gravacao_normal_permitida'])

    def test_unknown_efuse_and_wrong_chip_rejected(self):
        data = report()
        del data['efuses']['ABS_DONE_0']
        with self.assertRaises(ValueError):
            m.validate_report(data)
        with self.assertRaises(ValueError):
            m.parse_chip('Chip is ESP32-S3 (revision v0.2)\nMAC: 00:11:22:33:44:55')
        with self.assertRaises(ValueError):
            m.parse_chip('No device')

    def test_unsupported_flash_capacity_blocked(self):
        data = report()
        data['flash'] = '8MB'
        self.assertFalse(m.analyze(data)['gravacao_normal_permitida'])

    def test_no_arbitrary_operations_or_unsafe_flags(self):
        for operation in ['burn_efuse', 'burn_key', 'erase_flash', 'write_flash', 'unknown']:
            with self.assertRaises(ValueError):
                m.command('COM7', operation, 'image.bin')
        for operation in ['write', 'verify', 'backup']:
            module, args = m.command('COM7', operation, 'path with spaces.bin')
            self.assertEqual(module, 'esptool')
            self.assertNotIn('--force', args)
            self.assertIn('0x0', args)
            self.assertEqual(args[-1], 'path with spaces.bin')

    def test_both_existing_images_validate(self):
        for version in ['0.2.0', '0.3.0']:
            path = make_package(self.root, version)
            manifest, binary = m.validate_package(path)
            self.assertEqual(manifest['auth'], version == '0.3.0')
            self.assertEqual(binary.stat().st_size, m.FLASH_BYTES)

    def test_modified_image_and_path_traversal_rejected(self):
        path = make_package(self.root)
        manifest = m.read_json(path)
        binary = path.parent / manifest['file']
        with binary.open('r+b') as stream:
            stream.seek(0x10080)
            value = stream.read(1)
            stream.seek(-1, 1)
            stream.write(bytes([value[0] ^ 1]))
        with self.assertRaises(ValueError):
            m.validate_package(path)
        manifest['file'] = '../escape.bin'
        m.write_json(path, manifest)
        with self.assertRaises(ValueError):
            m.validate_package(path)

    def test_encrypted_manifest_and_wrong_auth_rejected(self):
        path = make_package(self.root)
        manifest = m.read_json(path)
        manifest['flash_encryption'] = True
        m.write_json(path, manifest)
        with self.assertRaises(ValueError):
            m.validate_package(path)
        manifest['flash_encryption'] = False
        manifest['auth'] = False
        m.write_json(path, manifest)
        with self.assertRaises(ValueError):
            m.validate_package(path)

    def test_flash_orders_backup_before_write_and_verify(self):
        path = make_package(self.root)
        backend = FakeUSB(self.root / 'state')
        result = backend.flash('COM7', report(), path)
        self.assertLess(backend.calls.index('read_flash'), backend.calls.index('write_flash'))
        self.assertLess(backend.calls.index('write_flash'), backend.calls.index('verify_flash'))
        entry = m.read_json(result)
        self.assertEqual(entry['status'], 'gravado_e_verificado')
        self.assertFalse(entry['protecao_de_leitura'])
        self.assertEqual(Path(entry['backup']).stat().st_size, m.FLASH_BYTES)
        if os.name != 'nt':
            self.assertEqual(Path(entry['backup']).stat().st_mode & 0o777, 0o600)

    def test_changed_board_never_written(self):
        path = make_package(self.root)
        backend = FakeUSB(self.root / 'state')
        backend.current['identificacao']['mac'] = '00:11:22:33:44:66'
        with self.assertRaises(ValueError):
            backend.flash('COM7', report(), path)
        self.assertNotIn('write_flash', backend.calls)

    def test_backup_failure_never_written_and_not_marked_valid(self):
        for failure in ['read_flash', 'short_backup']:
            path = make_package(self.root)
            backend = FakeUSB(self.root / failure, fail=failure)
            with self.assertRaises((RuntimeError, ValueError)):
                backend.flash('COM7', report(), path)
            self.assertNotIn('write_flash', backend.calls)
            self.assertFalse(list(backend.storage.glob('backups/**/backup.json')))
            self.assertEqual(m.read_json(next(backend.storage.glob('gravacoes/**/gravacao.json')))['status'], 'falha')

    def test_verify_failure_not_reported_as_success(self):
        path = make_package(self.root)
        backend = FakeUSB(self.root / 'state', fail='verify_flash')
        with self.assertRaises(RuntimeError):
            backend.flash('COM7', report(), path)
        entry = m.read_json(next(backend.storage.glob('gravacoes/**/gravacao.json')))
        self.assertEqual(entry['status'], 'falha')
        self.assertNotIn('protecao_de_leitura', entry)

    def test_venv_python_path_is_preserved(self):
        backend = m.Backend(sys.executable, self.root)
        self.assertEqual(backend.python, os.path.abspath(sys.executable))
        self.assertEqual(backend.check_tools(), m.VERSIONS)

    @unittest.skipUnless(os.environ.get('DISPLAY'), 'requires DISPLAY')
    def test_gui_embedded_page_background_scan(self):
        root = m.tk.Tk()
        root.withdraw()
        app = m.create_page(root)
        app.backend = lambda: FakeUSB(self.root / 'gui')
        app.off.set(True)
        app.board_ok.set(True)
        app.port.set('COM7')
        with patch.object(m.messagebox, 'showerror', side_effect=AssertionError):
            app.scan.invoke()
            end = time.monotonic() + 3
            while app.busy and time.monotonic() < end:
                root.update()
                time.sleep(0.01)
            self.assertFalse(app.busy)
            self.assertEqual(app.report['identificacao']['mac'], report()['identificacao']['mac'])
            self.assertIn('gravacao_normal_permitida', app.analysis_text.get('1.0', 'end'))
        app.destroy()
        root.destroy()

    @unittest.skipUnless(os.environ.get('DISPLAY') and os.environ.get('CNC_TEST_BUILDER'),
                         'requires DISPLAY and CNC_TEST_BUILDER')
    def test_actual_builder_generated_two_page_program(self):
        path = Path(os.environ['CNC_TEST_BUILDER'])
        spec = importlib.util.spec_from_file_location('real_user_builder', path)
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        self.assertIn(('function', 'create_page'), builder.inspect_script(ROOT / 'python/Gerenciador_ESP32_DLC32.py'))
        other = self.root / 'Outra.py'
        other.write_text('import tkinter as tk\ndef create_page(parent):\n return tk.Label(parent,text="Outra")\n')
        combined = self.root / 'Montado.py'
        combined.write_text(builder.generate_source([
            {'path': str(ROOT / 'python/Gerenciador_ESP32_DLC32.py'), 'title': 'Gerenciador', 'entry': 'create_page'},
            {'path': str(other), 'title': 'Outra', 'entry': 'create_page'}], [], 'Teste gerenciador'))
        spec = importlib.util.spec_from_file_location('real_manager_assembled', combined)
        assembled = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(assembled)
        def children(parent):
            for child in parent.winfo_children():
                yield child
                yield from children(child)
        def exercise(root):
            page = sys.modules['_embedded_page_0']
            app = next(w for w in children(root) if isinstance(w, page.App))
            self.assertEqual(Path(app.storage.get()), self.root / 'CNC_FFST_Gerenciador')
            app.backend = lambda: FakeUSB(self.root / 'mounted-state')
            app.off.set(True)
            app.board_ok.set(True)
            app.port.set('COM7')
            app.scan.invoke()
            end = time.monotonic() + 3
            while app.busy and time.monotonic() < end:
                root.update()
                time.sleep(0.01)
            self.assertFalse(app.busy)
            self.assertIsNotNone(app.report)
            root.destroy()
        with patch.object(m.tk.Tk, 'mainloop', exercise), patch.dict(os.environ), \
                patch.object(m.messagebox, 'showerror', side_effect=AssertionError):
            assembled.main()


if __name__ == '__main__':
    unittest.main(verbosity=2)
