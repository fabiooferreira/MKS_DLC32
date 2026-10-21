"""Real Tk status indicators under log backlog and managed M0; no physical board."""
from pathlib import Path
import tempfile
import time
import tkinter as tk
import unittest
from test_m0_alignment import page, ModelPort

class StatusDisplayTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        page.CONFIG=Path(self.temp.name)/'config.json'
        page.DIAGNOSTIC_LOG=Path(self.temp.name)/'log.txt'
        self.root=tk.Tk();self.app=page.App(self.root)
    def tearDown(self):
        self.app.camera_stop.set();self.app.stream.disconnect()
        self.root.destroy();self.temp.cleanup()
    def test_live_fields_are_current_despite_old_log_backlog(self):
        stream=self.app.stream
        stream.latest_command='G1 X20 F100'
        stream.latest_response='ok'
        self.app.events.put(('command','M5'))
        for _ in range(1000):self.app.events.put(('log','< old response'))
        self.app.poll()
        self.assertEqual(self.app.last_command.get(),'Comando: G1 X20 F100')
        self.assertEqual(self.app.last_response.get(),'Resposta: ok')
        self.assertGreater(self.app.events.qsize(),0,'One poll drained the entire log backlog')
    def test_fields_continue_after_retornar(self):
        stream=self.app.stream;port=ModelPort();port.port="SIM";stream.port=port
        stream.reader=stream.start_worker(stream.read_loop)
        stream.start(['G1X11F100','M0','G1X12','M5'],128,[])
        deadline=time.monotonic()+5
        while not stream.m0_alignment_ready and time.monotonic()<deadline:
            self.app.poll();time.sleep(.01)
        self.assertTrue(stream.m0_alignment_ready)
        self.app.poll()
        self.app.resume()
        deadline=time.monotonic()+5
        while stream.running and time.monotonic()<deadline:
            self.app.poll();time.sleep(.01)
        self.app.poll()
        self.assertFalse(stream.running or stream.cancel)
        self.assertIn('G1X12',port.writes)
        self.assertEqual(self.app.last_command.get(),'Comando: G4 P0.01')
        self.assertEqual(self.app.last_response.get(),'Resposta: ok')

if __name__=='__main__':unittest.main(verbosity=2)
