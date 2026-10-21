"""Real Tk + real generated single-file client + compiled auth shim. No hardware.
Use DISPLAY and a Python with Pillow/Tkinter. Optional --builder user's Montador.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import queue
import sys
import tempfile
import threading
import time
from unittest.mock import patch
import tkinter as tk
from tkinter import messagebox
from test_auth import AuthTests,KEY,HASH,ROOT

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m

def children(root):
    for w in root.winfo_children():yield w;yield from children(w)

def button(root,label):
    return next(w for w in children(root) if w.winfo_class() in ('Button','TButton') and w.cget('text')==label)

def stop_timers(root):
    widgets=[root,*children(root)]
    for timer in root.tk.call('after','info'):
        command=str(root.tk.call('after','info',timer)[0])
        owner=next((w for w in widgets if command in (w._tclCommands or [])),root)
        owner.after_cancel(timer)

class RawPort:
    port='USB_SIM';name='USB_SIM'
    def __init__(self,lib):self.lib=lib;self.rx=queue.Queue();self.is_open=True;self.lock=threading.RLock()
    def close(self):self.is_open=False
    def reset_input_buffer(self):
        while not self.rx.empty():self.rx.get_nowait()
    def readline(self):
        try:return self.rx.get(timeout=.05)
        except queue.Empty:return b''
    def write(self,data):
        with self.lock:
            self.lib.host_clear()
            if data.startswith(b'\xf8'):
                self.lib.host_frame(data,len(data))
                for line in self.lib.host_output().splitlines():self.rx.put(line+b'\n')
            elif data==b'\x18':
                self.lib.host_reset();self.lib.host_frame(b'',0)
                for line in self.lib.host_output().splitlines():self.rx.put(line+b'\n')
            elif data==b'?':self.rx.put(b'<Idle|MPos:1,2,3,4|WCO:0,0,0,0|FS:0,0>\n')
            elif data in [b'!',b'\x84',b'\x85']:pass
            else:
                self.lib.host_serial_bytes(data,len(data))
                for response in self.lib.host_output().splitlines():self.rx.put(response+b'\n')
        return len(data)

def main(builder_path):
    AuthTests.setUpClass();ports=[];errors=[]
    try:
        with tempfile.TemporaryDirectory(prefix='ffst-s3-gui-') as directory:
            base=Path(directory);identity=base/'identity.json'
            identity.write_text(json.dumps({'firmware':'CNC_FFST-S3-0.1.2','app_image_sha256':HASH}))
            def open_fn(page):
                def connect(name,baud):
                    AuthTests.lib.host_init();raw=RawPort(AuthTests.lib);ports.append(raw)
                    return page._ffst_auth.SignedPort(raw,KEY,boot_wait=0,identity_path=identity)
                return connect
            with patch.dict(os.environ,{'CNC_PCBS_CONFIG_DIR':str(base)}):
                profiles=['UART','USB']
                if (ROOT/'python/PROTECTED/CNC_FFST_Unico.py').exists():profiles.append('PROTECTED')
                for profile in profiles:
                    page=load('ffst_s3_'+profile,ROOT/'python'/profile/'CNC_FFST_Unico.py')
                    root=tk.Tk();root.withdraw()
                    root.report_callback_exception=lambda kind,value,tb: errors.append(str(value))
                    with patch.object(messagebox,'showerror') as error,patch.object(messagebox,'showwarning'),patch.object(messagebox,'showinfo'):
                        app=page.App(root)
                        try:
                            app.port.set('USB_SIM')
                            with patch.object(page,'open_authenticated',open_fn(page)):
                                button(root,'Conectar').invoke()
                            assert app.stream.port and app.stream.port.is_open
                            app.update_indicators();root.update()
                            assert 'USB_SIM' in app.connection_label.get()
                            # An interrupted file can leave its selection metadata behind.
                            app.active_file=0
                            app.run_macro({'command':'$X'})
                            assert all(str(b.cget('state'))=='normal' for b in app.macro_buttons), 'Unlock disabled macros although no job is running'
                            app.stream.running=True
                            app.update_macro_availability()
                            assert all(str(b.cget('state'))=='disabled' for b in app.macro_buttons)
                            app.stream.running=False;app.active_file=None
                            app.update_macro_availability()
                            ports[-1].rx.put(b'[PRB:1.0,2.0,3.0,4.0:1]\n')
                            limit=time.monotonic()+3
                            while app.stream.probe_result is None and time.monotonic()<limit:
                                root.update();time.sleep(.01)
                            assert app.stream.probe_result==((1.0,2.0,3.0),True),app.stream.probe_result
                            signed=app.stream.port
                            previous=signed._generation
                            signed.write(b'\x18')
                            deadline=time.monotonic()+4
                            while time.monotonic()<deadline and not (signed._generation>previous and signed.authenticated):
                                root.update();time.sleep(.01)
                            assert signed.authenticated and signed._generation>previous
                            assert signed.is_open
                            app.active_file=0;app.awaiting_idle=True
                            app.stream.paused=True;app.stream.m0_waiting=True
                            app.stream._m0_anchor=(1.,2.,3.)
                            app.progress['value']=70;app.job_elapsed=12
                            app.disconnect()
                            assert app.active_file is None and not app.awaiting_idle
                            assert not app.stream.paused and not app.stream.m0_waiting
                            assert not app.stream.inflight and app.stream._m0_anchor is None
                            assert app.job_elapsed==0 and float(app.progress['value'])==0
                            with patch.object(page,'open_authenticated',open_fn(page)):
                                button(root,'Conectar').invoke()
                            assert app.stream.port.authenticated and app.stream.port is not signed
                            assert not app.stream.running and not app.stream.cancel
                            app.run_macro({'command':'$X'})
                            assert all(str(b.cget('state'))=='normal' for b in app.macro_buttons)
                            assert not error.called,error.call_args_list
                            assert not errors,errors
                        finally:
                            app.camera_stop.set();app.disconnect();stop_timers(root);root.destroy()
                    print('PASS:',profile,'standalone Tk, button connection/HMAC, port indicator, four-axis probe response.')
            if builder_path:
                builder=load('real_s3_page_builder',builder_path)
                source=ROOT/'python/PROTECTED/CNC_FFST_Unico.py' if (ROOT/'python/PROTECTED/CNC_FFST_Unico.py').exists() else ROOT/'python/UART/CNC_FFST_Unico.py'
                extra=base/'Outra.py';extra.write_text('import tkinter as tk\ndef create_page(parent):\n return tk.Label(parent,text="Outra página")\n')
                combined=base/'Montado.py'
                combined.write_text(builder.generate_source([
                    {'path':str(source),'title':'CNC S3','entry':'App'},
                    {'path':str(extra),'title':'Outra','entry':'create_page'}],[],'CNC FFST S3'))
                assembled=load('s3_real_montado',combined)
                def exercise(root):
                    root.report_callback_exception=lambda kind,value,tb: errors.append(str(value))
                    page=sys.modules['_embedded_page_0']
                    next(w for w in children(root) if w.winfo_class()=='TCombobox').set('USB_SIM')
                    with patch.object(page,'open_authenticated',open_fn(page)):
                        button(root,'Conectar').invoke()
                    root.update()
                    labels=[root.getvar(w.cget('textvariable')) for w in children(root)
                            if w.winfo_class()=='TLabel' and w.cget('textvariable')]
                    assert any('USB_SIM' in str(s) for s in labels)
                    assert not errors,errors
                    stop_timers(root);button(root,'Sair').invoke()
                with patch.object(tk.Tk,'mainloop',exercise),patch.dict(os.environ), \
                     patch.object(messagebox,'showerror') as error,patch.object(messagebox,'showwarning'),patch.object(messagebox,'showinfo'):
                    assembled.main();assert not error.called,error.call_args_list
                print('PASS: original Montador generated two-page application, HMAC connection and clean exit.')
    finally:
        for port in ports:port.close()
        AuthTests.tearDownClass()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--builder',type=Path)
    main(parser.parse_args().builder)
