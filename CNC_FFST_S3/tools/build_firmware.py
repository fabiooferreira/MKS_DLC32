"""Reproducible local build entry point. Never flashes or modifies eFuses."""
from pathlib import Path
import argparse
import os
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]

def run(profile, signing_key=None):
    environment='cnc_ffst_s3_n16r8_'+profile
    artifacts=ROOT/'artifacts'/profile.upper();artifacts.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy()
    env.setdefault('PLATFORMIO_CORE_DIR',str(ROOT/'.platformio-core'))
    env['PLATFORMIO_SETTING_ENABLE_TELEMETRY']='No'
    env['PYTHONIOENCODING']='utf-8'
    if signing_key:env['FFST_SIGNING_KEY']=str(Path(signing_key).resolve())
    with (artifacts/'build.log').open('w',encoding='utf-8') as log:
        proc=subprocess.Popen([sys.executable,'-m','platformio','run','-d',str(ROOT/'firmware'),
            '-e',environment,'-j','2'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
            text=True,encoding='utf-8',errors='replace',env=env)
        for line in proc.stdout:
            print(line,end='');log.write(line);log.flush()
        code=proc.wait()
        if code:raise SystemExit(code)
    subprocess.run([sys.executable,str(ROOT/'tools/package_firmware.py'),profile],check=True,env=env)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('profile',choices=['uart','usb','protected','all'],default='uart',nargs='?')
    parser.add_argument('--signing-key')
    args=parser.parse_args();profile=args.profile
    for p in ['uart','usb'] if profile=='all' else [profile]:run(p,args.signing_key)
