"""CNC_FFST: diagnóstico somente leitura da DLC32 V2.1.

Instalar: python -m pip install esptool==4.8.1 bitstring==4.3.1 pyserial==3.5
Executar: python Gerenciador_ESP32_DLC32.py
Não grava firmware ou eFuses. Feche o controlador CNC antes da consulta.
"""
import datetime
import importlib.metadata
import json
import os
from pathlib import Path
import queue
import re
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

FIELDS = ('FLASH_CRYPT_CNT', 'FLASH_CRYPT_CONFIG', 'DISABLE_DL_ENCRYPT',
          'DISABLE_DL_DECRYPT', 'DISABLE_DL_CACHE', 'JTAG_DISABLE',
          'ABS_DONE_0', 'ABS_DONE_1')
VERSIONS = {'esptool': '4.8.1', 'bitstring': '4.3.1', 'pyserial': '3.5'}


def dependency_check():
    found = {}
    for name, expected in VERSIONS.items():
        try:
            found[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            found[name] = 'ausente'
    if found != VERSIONS:
        raise RuntimeError('Dependências incompatíveis: ' + json.dumps(found) +
                           '\nInstale: python -m pip install esptool==4.8.1 bitstring==4.3.1 pyserial==3.5')
    return found


def command(port, operation):
    # Lista fechada: não há comandos de gravação ou parâmetros livres.
    if operation == 'chip':
        return 'esptool', ['--chip', 'esp32', '--port', port, 'chip_id']
    if operation == 'flash':
        return 'esptool', ['--chip', 'esp32', '--port', port, 'flash_id']
    if operation == 'efuses':
        return 'espefuse', ['--chip', 'esp32', '--port', port, 'summary',
                            '--format', 'json', *FIELDS]
    raise ValueError('Operação não permitida')


def run_read(port, operation):
    module, args = command(port, operation)
    if getattr(sys, 'frozen', False):
        prefix = [sys.executable, '--worker']
    else:
        prefix = [sys.executable, str(Path(__file__).resolve()), '--worker']
    result = subprocess.run(prefix + [operation, port], capture_output=True,
                            text=True, encoding='utf-8', errors='replace',
                            timeout=90, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    if result.returncode:
        # Não incluir saída arbitrária do utilitário no relatório.
        raise RuntimeError(f'Consulta {operation} falhou (código {result.returncode}). '
                           'Confira porta, cabo USB, driver e se outro programa está conectado.')
    return result.stdout


def parse_chip(output):
    mac = re.search(r'MAC:\s*([0-9a-fA-F:]{17})', output)
    chip = re.search(r'Chip is\s+([^\r\n]+)', output)
    crystal = re.search(r'Crystal is\s+([^\r\n]+)', output)
    if not mac or not chip or 'ESP32' not in chip.group(1):
        raise ValueError('Identificação incompleta; relatório não pode ser concluído.')
    return {'mac': mac.group(1).lower(), 'chip_e_revisao': chip.group(1),
            'cristal': crystal.group(1) if crystal else 'não identificado'}


def parse_efuses(output):
    start = output.find('{')
    if start < 0:
        raise ValueError('Resposta de eFuses sem JSON.')
    data, _ = json.JSONDecoder().raw_decode(output[start:])
    safe = {}
    for name in FIELDS:
        entry = data.get(name, {})
        value = entry.get('value')
        if entry.get('readable') is not True or type(value) not in (bool, int):
            raise ValueError('eFuse não identificado ou não legível: ' + name)
        safe[name] = {'value': value, 'readable': True,
                      'writeable': entry.get('writeable') is True}
    return safe


def encryption_state(efuses):
    count = efuses['FLASH_CRYPT_CNT']['value']
    if type(count) is not int or not 0 <= count <= 127:
        raise ValueError('FLASH_CRYPT_CNT inválido')
    return 'ativa' if bin(count).count('1') % 2 else 'inativa'


def collect(port, progress):
    versions = dependency_check()
    progress('Consultando identificação do ESP32…')
    first = parse_chip(run_read(port, 'chip'))
    progress('Consultando tamanho da flash…')
    flash = run_read(port, 'flash')
    size = re.search(r'Detected flash size:\s*([^\r\n]+)', flash)
    if not size:
        raise ValueError('Não foi possível identificar o tamanho da flash.')
    progress('Consultando campos públicos de segurança…')
    efuses = parse_efuses(run_read(port, 'efuses'))
    progress('Conferindo se a placa continua sendo a mesma…')
    last = parse_chip(run_read(port, 'chip'))
    if first != last:
        raise ValueError('A identificação da placa mudou durante a consulta.')
    return {'formato': 'CNC_FFST_DIAGNOSTICO_1',
            'data_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'hardware_informado_pelo_usuario': 'MKS DLC32 V2.1 / ESP32-WROOM-32U',
            'identificacao': first, 'flash': size.group(1), 'ferramentas': versions,
            'efuses': efuses, 'criptografia_flash': encryption_state(efuses),
            'ativacao_de_protecoes': 'BLOQUEADA: exige pacote e procedimento validados',
            'pendencias': ['Confirmar fisicamente modelo e revisão da placa.',
                          'Preparar bootloader e firmware compatíveis com criptografia.',
                          'Definir atualização e recuperação antes de gravar eFuses.',
                          'Testar boot, autenticação, movimento e segurança na placa real.'],
            'privacidade': 'Sem chaves, blocos de chave, Wi-Fi ou conteúdo da flash.'}


class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=14)
        self.pack(fill='both', expand=True)
        self.events = queue.Queue()
        self.report = None
        self.busy = False
        self.port = tk.StringVar()
        ttk.Label(self, text='CNC_FFST — Gerenciador DLC32 V2.1',
                  font=('Arial', 14, 'bold')).pack(anchor='w')
        ttk.Label(self, text='Consulta somente leitura. As ferramentas podem reiniciar a placa.\n'
                  'Pare o trabalho, desligue laser/spindle e feche outros controladores.',
                  wraplength=650).pack(anchor='w', pady=10)
        row = ttk.Frame(self)
        row.pack(fill='x')
        ttk.Label(row, text='Porta USB:').pack(side='left')
        self.ports = ttk.Combobox(row, textvariable=self.port, width=28)
        self.ports.pack(side='left', padx=8)
        ttk.Button(row, text='Atualizar portas', command=self.refresh).pack(side='left')
        self.scan = ttk.Button(self, text='Consultar placa e gerar relatório', command=self.start)
        self.scan.pack(anchor='w', pady=12)
        self.save = ttk.Button(self, text='Salvar relatório para enviar', command=self.export,
                               state='disabled')
        self.save.pack(anchor='w')
        ttk.Button(self, text='Ativar proteções — aguardando pacote validado',
                   state='disabled').pack(anchor='w', pady=10)
        self.log = tk.Text(self, width=85, height=20, wrap='word', state='disabled')
        self.log.pack(fill='both', expand=True)
        self.write('Este programa não altera o firmware nem grava eFuses.\n'
                   'O relatório identifica o chip e o estado atual; não certifica proteção completa.')
        self.refresh()
        self.timer = self.after(100, self.poll)
        self.bind('<Destroy>', self.cleanup, add='+')

    def cleanup(self, event):
        if event.widget is self:
            self.after_cancel(self.timer)

    def write(self, text):
        self.log.configure(state='normal')
        self.log.insert('end', text + '\n')
        self.log.see('end')
        self.log.configure(state='disabled')

    def refresh(self):
        try:
            from serial.tools import list_ports
            ports = [item.device for item in list_ports.comports()]
            self.ports['values'] = ports
            if not self.port.get() and ports:
                self.port.set(ports[0])
        except ImportError:
            self.write('Instale: python -m pip install esptool==4.8.1 bitstring==4.3.1 pyserial==3.5')

    def start(self):
        if self.busy:
            return
        port = self.port.get().strip()
        if not port:
            messagebox.showerror('Porta', 'Selecione a porta USB.', parent=self)
            return
        self.report = None
        self.busy = True
        self.scan.configure(state='disabled')
        self.save.configure(state='disabled')
        def work():
            try:
                result = collect(port, lambda s: self.events.put(('log', s)))
                self.events.put(('done', result))
            except Exception as exc:
                self.events.put(('error', str(exc)))
        threading.Thread(target=work, daemon=True).start()

    def poll(self):
        try:
            while True:
                kind, value = self.events.get_nowait()
                if kind == 'log':
                    self.write(value)
                else:
                    self.busy = False
                    self.scan.configure(state='normal')
                    if kind == 'done':
                        self.report = value
                        self.save.configure(state='normal')
                        self.write(json.dumps(value, ensure_ascii=False, indent=2))
                    else:
                        self.write('ERRO: ' + value)
        except queue.Empty:
            pass
        self.timer = self.after(100, self.poll)

    def export(self):
        if self.report is None:
            return
        name = 'DLC32_' + self.report['identificacao']['mac'].replace(':', '') + '.json'
        destination = filedialog.asksaveasfilename(parent=self, initialfile=name,
                          defaultextension='.json', filetypes=[('Relatório JSON', '*.json')])
        if destination:
            try:
                Path(destination).write_text(json.dumps(self.report, ensure_ascii=False, indent=2),
                                             encoding='utf-8')
                self.write('Relatório salvo. Você pode enviar esse arquivo para análise.')
            except OSError as exc:
                messagebox.showerror('Não foi possível salvar', str(exc), parent=self)


def create_page(parent):
    return App(parent)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--worker':
        import runpy
        if len(sys.argv) != 4:
            raise SystemExit(2)
        dependency_check()
        module, args = command(sys.argv[3], sys.argv[2])
        sys.argv = [module, *args]
        runpy.run_module(module, run_name='__main__')
    else:
        root = tk.Tk()
        root.title('CNC_FFST — Gerenciador ESP32')
        App(root)
        root.mainloop()
