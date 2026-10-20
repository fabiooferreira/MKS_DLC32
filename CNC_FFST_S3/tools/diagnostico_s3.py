"""Read-only ESP32-S3 chip/eFuse report. No key blocks or flash contents.
python diagnostico_s3.py COM7 --out relatorio_s3.json
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
FIELDS=('SPI_BOOT_CRYPT_CNT','SECURE_BOOT_EN','DIS_DOWNLOAD_MODE','ENABLE_SECURITY_DOWNLOAD',
        'DIS_DOWNLOAD_MANUAL_ENCRYPT','HARD_DIS_JTAG','SOFT_DIS_JTAG','DIS_USB_JTAG','DIS_PAD_JTAG',
        *('KEY_PURPOSE_'+str(i) for i in range(6)))

def extract_fields(text):
    start=text.find('{')
    if start<0:raise ValueError('Resumo de eFuses sem JSON')
    data,_=json.JSONDecoder().raw_decode(text[start:])
    result={}
    for name in FIELDS:
        entry=data.get(name)
        if not isinstance(entry,dict) or 'value' not in entry:raise ValueError('Campo ausente: '+name)
        result[name]={k:entry.get(k) for k in ('value','readable','writeable')}
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('port');parser.add_argument('--out',default='relatorio_s3.json')
    args=parser.parse_args()
    print('Somente consulta; pode reiniciar a placa. Pare a máquina e feche o controlador antes de executar.')
    def read(module,command):
        p=subprocess.run([sys.executable,'-m',module,'--chip','esp32s3','--port',args.port,*command],
                         capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
        if p.returncode:raise RuntimeError('Falha na consulta. Confira porta/driver/USB e esptool 4.8.1; nenhuma proteção foi alterada.')
        return p.stdout
    first=read('esptool',['chip_id'])
    mac=re.search(r'MAC:\s*([0-9a-fA-F:]{17})',first)
    chip=re.search(r'Chip is\s*([^\r\n]+)',first)
    if not mac or not chip or 'ESP32-S3' not in chip[1]:raise ValueError('Identificação S3 incompleta')
    flash=read('esptool',['flash_id'])
    size=re.search(r'Detected flash size:\s*([^\r\n]+)',flash)
    efuses=extract_fields(read('espefuse',['summary','--format','json',*FIELDS]))
    last=read('esptool',['chip_id'])
    last_mac=re.search(r'MAC:\s*([0-9a-fA-F:]{17})',last)
    if not last_mac or last_mac[1].lower()!=mac[1].lower():raise ValueError('A placa mudou durante a consulta')
    report={'format':'CNC_FFST_S3_DIAGNOSTIC_1','date_utc':datetime.now(timezone.utc).isoformat(),
            'chip':chip[1],'mac':mac[1].lower(),'flash':size[1] if size else 'desconhecida',
            'efuses':efuses,'privacy':'Sem blocos de chave, firmware ou dados Wi-Fi',
            'note':'Não certifica proteção completa; não identifica o layout da DevKit.'}
    Path(args.out).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Relatório salvo:',args.out)

if __name__=='__main__':main()
