"""Real Tk smoke test with user's Montador runtime and host auth shim.

Run with a display (a virtual display is sufficient):
python tools/test_page_integration.py --builder /path/Montador_de_Paginas.py
No physical machine, serial port, movement or tools are used.
"""
import argparse
import importlib.util
import os
from pathlib import Path
import sys
import tempfile
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def descendants(widget):
    for child in widget.winfo_children():
        yield child
        yield from descendants(child)


def button(root, text):
    return next(w for w in descendants(root) if w.winfo_class() in ('TButton','Button') and w.cget('text') == text)


def stop_timers(root):
    # after_cancel must run on the widget that registered the Tcl callback.
    owners=[root,*descendants(root)]
    for timer in root.tk.call('after','info'):
        command=str(root.tk.call('after','info',timer)[0])
        owner=next((w for w in owners if command in (w._tclCommands or [])),root)
        owner.after_cancel(timer)


def main(builder_path):
    builder = module('user_page_builder', builder_path)
    assert ('class','App') in builder.inspect_script(ROOT/'python/CNC_FFST_Unico.py')
    harness = module('page_auth_test_harness', ROOT/'tools/test_auth.py')
    harness.AuthTests.setUpClass()
    errors, ports = [], []

    def backend(page):
        def open_port(name, baud):
            raw = harness.HostPort(harness.AuthTests.binary)
            raw.port = name
            raw.name = name
            ports.append(raw)
            return page._ffst_auth.SignedPort(raw,harness.KEY,boot_wait=0,
                                               identity_path=harness.AuthTests.identity)
        return open_port

    try:
        with tempfile.TemporaryDirectory(prefix='ffst-page-test-') as tmp:
            base=Path(tmp)
            extract=base/'extracted'; extract.mkdir()
            persistent=base/'persistent'; persistent.mkdir()
            single=extract/'CNC_FFST_Unico.py'
            single.write_bytes((ROOT/'python/CNC_FFST_Unico.py').read_bytes())
            runtime={"__name__":"test_builder_runtime"}
            exec(builder.RUNTIME.replace('__PAYLOAD__',repr('')),runtime)
            with patch.dict(os.environ,{'CNC_PCBS_CONFIG_DIR':str(persistent)}), \
                 patch.object(messagebox,'showerror') as showerror, \
                 patch.object(messagebox,'showwarning'), patch.object(messagebox,'showinfo') as showinfo:
                page=module('test_ffst_page',single)
                root=tk.Tk();root.withdraw()
                root.report_callback_exception=lambda kind,value,tb: errors.append(str(value))
                host=runtime['PageHost'](root);host.pack(fill='both',expand=True)
                app=page.App(host)
                try:
                    assert page.PROJECT_DIR==persistent
                    app.port.set('COM_TEST')
                    with patch.object(page,'open_authenticated',backend(page)):
                        button(root,'Conectar').invoke()
                    assert app.stream.port and app.stream.port.is_open
                    app.update_indicators()
                    assert 'COM_TEST' in app.connection_label.get()
                    root.update()
                    assert not errors,errors
                    app.disconnect()
                    with patch.object(page,'open_authenticated',side_effect=RuntimeError('Firmware 0.3.0 esperado')):
                        button(root,'Conectar').invoke()
                    assert app.status.get()=='Falha na conexão'
                    assert showerror.called
                    assert showerror.call_args.kwargs['parent'] is root
                    assert 'Firmware 0.3.0 esperado' in page.DIAGNOSTIC_LOG.read_text()
                    app.port.set('')
                    button(root,'Conectar').invoke()
                    assert app.stream.simulation and showinfo.called
                    app.save()
                    assert (persistent/'config_controlador_pcb.json').exists()
                    assert not (extract/'config_controlador_pcb.json').exists()
                    assert not errors,errors
                finally:
                    app.camera_stop.set();app.stream.disconnect()
                    stop_timers(root)
                    root.destroy()
            print('PASS: actual PageHost, Conectar button, authenticated adapter, indicators/poll, visible failure, blank-port feedback and persistent config.')

            # Generate a real two-page application and run its unmodified mounting code.
            second=base/'Outra_pagina.py'
            second.write_text('import tkinter as tk\ndef create_page(parent):\n    return tk.Label(parent,text="Outra página")\n')
            pages=[{'path':str(single),'title':'CNC','entry':'App'},
                   {'path':str(second),'title':'Outra','entry':'create_page'}]
            combined=base/'Programa_com_paginas.py'
            combined.write_text(builder.generate_source(pages,[],'Teste duas páginas'))
            assembled=module('test_combined_runtime',combined)
            def exercise_combined(root):
                root.report_callback_exception=lambda kind,value,tb: errors.append(str(value))
                cnc=sys.modules['_embedded_page_0']
                assert cnc.PROJECT_DIR==base
                ports_widget=next(w for w in descendants(root) if w.winfo_class()=='TCombobox')
                ports_widget.set('COM_MONTADO')
                with patch.object(cnc,'open_authenticated',backend(cnc)):
                    button(root,'Conectar').invoke()
                root.update()
                labels=[root.getvar(w.cget('textvariable')) for w in descendants(root)
                        if w.winfo_class()=='TLabel' and w.cget('textvariable')]
                assert any('COM_MONTADO' in str(s) for s in labels)
                assert not errors,errors
                stop_timers(root)
                button(root,'Sair').invoke()
            with patch.object(tk.Tk,'mainloop',exercise_combined), \
                 patch.object(messagebox,'showerror') as assembled_error, \
                 patch.object(messagebox,'showwarning'),patch.object(messagebox,'showinfo'):
                assembled.main()
                assert not assembled_error.called,assembled_error.call_args_list
            assert (base/'config_controlador_pcb.json').exists()
            assert not errors,errors
            print('PASS: generated two-page app from actual Montador, button authentication, visible COM indicator and clean Sair/save.')
    finally:
        for port in ports:port.close()
        harness.AuthTests.tearDownClass()


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--builder',type=Path,required=True)
    main(parser.parse_args().builder)
