"""Prepare a fixed shared key, reusing a previous build's embedded record.

No key value is printed. The public BIN necessarily contains recoverable key bytes;
this is application access control, not protection against reverse engineering.
"""
from pathlib import Path
import os
import secrets

PREFIX = b'FFST_SHAREDKEY1:'
SUFFIX = b':FFST_KEY_END'


def extract_key(data):
    index = data.find(PREFIX)
    if index < 0 or data.find(PREFIX, index+1) >= 0:
        raise ValueError('Unique shared-key record not found')
    start = index+len(PREFIX)
    key = data[start:start+32]
    if len(key) != 32 or data[start+32:start+32+len(SUFFIX)] != SUFFIX:
        raise ValueError('Invalid shared-key record')
    return key


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    private = root/'.private'
    private.mkdir(exist_ok=True, mode=0o700)
    seed = private/'shared_key.bin'
    if seed.exists():
        key = seed.read_bytes()
        if len(key) != 32:
            raise ValueError('Invalid retained key; refusing silent rotation')
    else:
        binary = root/'artifacts/CNC_FFST_0.3.0_FULL_4MB.bin'
        try:
            key = extract_key(binary.read_bytes())
        except (OSError, ValueError):
            key = secrets.token_bytes(32)
        with os.fdopen(os.open(seed, os.O_WRONLY|os.O_CREAT|os.O_EXCL, 0o600), 'wb') as out:
            out.write(key)
    record = PREFIX+key+SUFFIX
    generated = root/'Firmware/Grbl_Esp32/src/FFSTSharedKey.generated.h'
    text = '// Generated shared credential. Do not publish this header separately.\n'
    text += 'static const volatile uint8_t ffstSharedKeyRecord[] = {'
    text += ','.join('0x%02x'%byte for byte in record)+'};\n'
    if not generated.exists() or generated.read_text() != text:
        generated.write_text(text)
    print('Shared credential prepared/reused; value not displayed.')
