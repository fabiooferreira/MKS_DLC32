"""Host checks only: no physical flash or eFuse operations."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT/'installer/Instalador_CNC_FFST_S3.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
BIN = ROOT/'artifacts/UART'/module.BIN_NAME


class FakeBackend(module.Backend):
    def __init__(self, chip='Chip is ESP32-S3 (revision v0.2)\nMAC: 12:34:56:78:90:ab', flash='Detected flash size: 16MB', fail_verify=False):
        super().__init__(lambda text: None)
        self.commands = []
        self.chip, self.flash, self.fail_verify = chip, flash, fail_verify

    def command(self, args):
        self.commands.append(args)
        if 'chip_id' in args: return self.chip
        if 'flash_id' in args: return self.flash
        if 'verify_flash' in args and self.fail_verify: raise RuntimeError('Verification failed')
        return 'OK'


class InstallerTests(unittest.TestCase):
    def test_valid_release_image(self):
        self.assertEqual(len(module.validate_image(BIN)), 64)

    def test_app_only_rejected(self):
        with self.assertRaises(ValueError):
            module.validate_image(ROOT/'artifacts/UART/firmware_app_0x10000.bin')

    def test_corrupt_image_rejected(self):
        data = bytearray(BIN.read_bytes()); data[0x10100] ^= 1
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'corrupt.bin'; path.write_bytes(data)
            with self.assertRaises(ValueError): module.validate_image(path)

    def test_other_chip_never_written(self):
        backend = FakeBackend(chip='Chip is ESP32-D0WD')
        with self.assertRaises(ValueError): backend.install('COM7', BIN)
        self.assertFalse(any('write_flash' in args for args in backend.commands))

    def test_other_flash_never_written(self):
        backend = FakeBackend(flash='Detected flash size: 8MB')
        with self.assertRaises(ValueError): backend.install('COM7', BIN)
        self.assertFalse(any('write_flash' in args for args in backend.commands))

    def test_write_then_verify_without_force_or_efuses(self):
        backend = FakeBackend(); backend.install('COM7', BIN)
        self.assertEqual([args[5] for args in backend.commands], ['chip_id','flash_id','write_flash','verify_flash'])
        self.assertEqual(backend.commands[2][-2], '0x0')
        for args in backend.commands:
            self.assertNotIn('--force', args)
            self.assertNotIn('espefuse', args)

    def test_verify_failure_is_failure(self):
        backend = FakeBackend(fail_verify=True)
        with self.assertRaises(RuntimeError): backend.install('COM7', BIN)


if __name__ == '__main__': unittest.main(verbosity=2)
