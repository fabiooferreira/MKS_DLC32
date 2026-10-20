"""Produce one user-facing Python file, embedding auth code, identity and compressed BIN."""
from pathlib import Path
import base64
import json
import textwrap
import zlib

root = Path(__file__).resolve().parents[1]
folder = root/'python'
auth = (folder/'cnc_ffst_auth.py').read_text()
auth = auth[:auth.index("if __name__ == '__main__':")]
auth = auth.replace(
    "path = Path(path or Path(__file__).with_name('CNC_FFST_0.3.0_FULL_4MB.bin'))",
    'path = Path(path) if path is not None else None')
auth = auth.replace('data = path.read_bytes()',
                    'data = path.read_bytes() if path else zlib.decompress(base64.b85decode(_firmware_blob))')
auth = auth.replace(
    "path = Path(identity_path or Path(__file__).with_name('firmware_identity.json'))",
    'path = Path(identity_path) if identity_path is not None else None')
auth = auth.replace("identity = json.loads(path.read_text(encoding='utf-8'))",
                    "identity = json.loads(path.read_text(encoding='utf-8')) if path else _firmware_identity")
identity = json.loads((folder/'firmware_identity.json').read_text())
packed = base64.b85encode(zlib.compress((folder/'CNC_FFST_0.3.0_FULL_4MB.bin').read_bytes(), 9)).decode('ascii')
resource = '\n'.join('        '+repr(line).replace("'", "b'", 1)
                     for line in textwrap.wrap(packed, 100, break_on_hyphens=False))
factory = '''# Authentication and firmware resources are embedded; no sidecar files needed.
def _create_embedded_auth():
    import base64
    import zlib
    import types
    _firmware_blob = (
'''+resource+'''
    )
    _firmware_identity = '''+repr(identity)+'\n'+textwrap.indent(auth,'    ')+'''
    return types.SimpleNamespace(
        open_authenticated=open_authenticated, SAFE_REALTIME=SAFE_REALTIME,
        SignedPort=SignedPort, mac=mac, exchange=exchange,
        load_key=load_key, verify_firmware=verify_firmware)

_ffst_auth = _create_embedded_auth()
open_authenticated = _ffst_auth.open_authenticated
SAFE_REALTIME = _ffst_auth.SAFE_REALTIME
'''
app = (folder/'Fabricação Laser Fresa.py').read_text()
app = app.replace('from cnc_ffst_auth import open_authenticated, SAFE_REALTIME',factory)
destination = folder/'CNC_FFST_Unico.py'
destination.write_text(app, encoding='utf-8')
print('Single Python file generated:', destination.name, destination.stat().st_size, 'bytes')
