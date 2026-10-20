"""Write public client compatibility manifest from the ESP32 application's validated image digest."""
from pathlib import Path
import hashlib
import json
import re
import struct
import shutil


def image_digest(data):
    if len(data) < 24 or data[0] != 0xe9 or data[23] != 1:
        raise ValueError('Expected an ESP32 image with appended SHA256')
    position, checksum = 24, 0xef
    for _ in range(data[1]):
        if position + 8 > len(data):
            raise ValueError('Truncated segment header')
        _, length = struct.unpack_from('<II', data, position)
        position += 8
        if position + length > len(data):
            raise ValueError('Truncated segment')
        for byte in data[position:position+length]:
            checksum ^= byte
        position += length
    checksum_position = ((position + 16)//16)*16-1
    end = checksum_position + 1
    digest = hashlib.sha256(data[:end]).digest()
    if data[checksum_position] != checksum or data[end:end+32] != digest:
        raise ValueError('ESP32 image checksum/digest mismatch')
    return digest.hex()


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    data = (root/'artifacts/firmware.bin').read_bytes()
    header = (root/'Firmware/Grbl_Esp32/src/Grbl.h').read_text()
    version = re.search(r'GRBL_VERSION_BUILD\s*=\s*"(CNC_FFST-[^"]+)"', header)[1]
    manifest = {'protocol': 1, 'firmware': version,
                'app_image_sha256': image_digest(data),
                'application_file_sha256': hashlib.sha256(data).hexdigest()}
    destination = root/'python/firmware_identity.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(manifest, indent=2)+'\n')
    full = root/'artifacts/CNC_FFST_0.3.0_FULL_4MB.bin'
    shutil.copy2(full, root/'python'/full.name)
    print('Client firmware identity generated:', version, manifest['app_image_sha256'])
