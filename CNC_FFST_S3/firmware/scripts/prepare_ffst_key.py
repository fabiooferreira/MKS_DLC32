"""PlatformIO pre-hook: retain common app key; never silently rotate it."""
from pathlib import Path
import os
Import('env')
root=Path(env['PROJECT_DIR']).parent
seed=root/'.private/shared_key.bin'
if seed.is_file():
    key=seed.read_bytes()
    if len(key)!=32:raise RuntimeError('Invalid retained shared credential')
else:
    binary=root/'artifacts/UART/CNC_FFST_S3_0.1.0_UART_FULL_16MB.bin'
    data=binary.read_bytes()
    prefix,suffix=b'FFST_SHAREDKEY1:',b':FFST_KEY_END'
    index=data.find(prefix)
    if index<0 or data.find(prefix,index+1)>=0:raise RuntimeError('Existing credential record not found')
    start=index+len(prefix);key=data[start:start+32]
    if len(key)!=32 or data[start+32:start+32+len(suffix)]!=suffix:raise RuntimeError('Invalid credential record')
    seed.parent.mkdir(mode=0o700,exist_ok=True)
    with os.fdopen(os.open(seed,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600),'wb') as out:out.write(key)
record=b'FFST_SHAREDKEY1:'+key+b':FFST_KEY_END'
text='/* Generated credential: do not print or publish separately. */\nstatic const volatile unsigned char ffst_key_record[] = {'+','.join(str(v) for v in record)+'};\n'
header=root/'firmware/main/ffst_key.generated.h'
if not header.exists() or header.read_text()!=text:header.write_text(text)
print('CNC_FFST: common application credential retained; no value displayed.')
