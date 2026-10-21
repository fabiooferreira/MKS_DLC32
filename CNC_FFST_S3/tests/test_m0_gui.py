"""Modeless pause dialog and explicit Retornar; real Tk, no board."""
import os
import tempfile
import tkinter as tk
from test_m0_alignment import page
with tempfile.TemporaryDirectory() as temp:
    # Module was imported already; prevent writing application config into the source tree.
    from pathlib import Path
    page.CONFIG=Path(temp)/'config.json'
    page.DIAGNOSTIC_LOG=Path(temp)/'log.txt'
    root=tk.Tk();app=page.App(root)
    try:
        app.stream.running=True;app.stream.m0_waiting=True
        app.stream._m0_managed=True;app.stream.m0_alignment_ready=True
        app.active_file=0
        app.events.put(('m0_alignment',10));app.poll();root.update()
        window=app._m0_notice
        assert window.title()=='Pausa para Conferência de Posicionamento e Ajuste Fino'
        assert root.grab_current() is None
        text=' '.join(str(w.cget('text')) for w in window.winfo_children() if 'text' in w.keys())
        assert 'Pressione Retornar' in text
        assert 'Comandos de posição e macros estão ativos' in text
        assert all(str(b.cget('state'))=='normal' for b in app.macro_buttons)
        app.close_m0_notice();root.update()
        assert not app.stream._m0_resume.is_set()
        assert app.stream.m0_waiting and app.stream.m0_alignment_ready
        app.show_m0_notice();app.resume();root.update()
        assert app._m0_notice is None
        assert app.stream._m0_resume.is_set()
        print('PASS: exact pause title, modeless dialog, enabled macros; closing does not resume; Retornar does.')
    finally:
        app.camera_stop.set();root.destroy()
