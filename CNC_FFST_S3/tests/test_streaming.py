"""Threading regression for real generated Streamer; no hardware or motion."""
import importlib.util
from pathlib import Path
import queue
import threading
import time
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('streaming_page',ROOT/'python/UART/CNC_FFST_Unico.py')
page=importlib.util.module_from_spec(spec);spec.loader.exec_module(page)

class StreamingTests(unittest.TestCase):
    def test_pending_item_exists_before_immediate_ack(self):
        stream=page.Streamer(queue.Queue())
        class Port:
            def write(self,payload):
                with stream.lock:
                    self.seen=list(stream.inflight)
                    stream.inflight.pop(0)
                return len(payload)
        port=Port();stream.port=port
        stream.send_payload(b'G1X1\n',7)
        self.assertEqual(port.seen,[(7,5)])
        self.assertFalse(stream.inflight)

    def test_write_failure_removes_only_its_pending_item(self):
        stream=page.Streamer(queue.Queue());original=(1,10);stream.inflight=[original]
        class Port:
            def write(self,payload):raise OSError('write timeout')
        stream.port=Port()
        with self.assertRaisesRegex(OSError,'write timeout'):
            stream.send_payload(b'G1X1\n',2)
        self.assertEqual(stream.inflight,[original])

    def test_reader_keeps_processing_status_while_next_write_waits(self):
        second=threading.Event();release=threading.Event();rx=queue.Queue()
        class Port:
            is_open=True
            calls=0
            first=True
            def write(self,payload):
                if payload==b'?':return 1
                self.calls+=1
                if self.calls==2:
                    second.set();release.wait(3)
                rx.put(b'ok\n')
                if self.calls==1:rx.put(b'<Run|MPos:1,2,3,4|FS:100,0>\n')
                return len(payload)
            def readline(self):
                try:value=rx.get(timeout=.05)
                except queue.Empty:return b''
                if self.first:
                    self.first=False;second.wait(2)
                return value
            def close(self):self.is_open=False
        stream=page.Streamer(queue.Queue());port=Port();stream.port=port
        stream.running=True;stream.sync_command=lambda *args:None
        reader=threading.Thread(target=stream.read_loop,daemon=True)
        sender=threading.Thread(target=stream.stream_loop,args=([(1,'G1X1F100'),(2,'G1X2'),(-1,'G4P0')],1),daemon=True)
        reader.start();sender.start()
        try:
            self.assertTrue(second.wait(2),'Second write did not start')
            deadline=time.monotonic()+1
            while stream.status_version==0 and time.monotonic()<deadline:time.sleep(.01)
            self.assertGreater(stream.status_version,0,'Reader blocked behind sender: no status processed')
        finally:
            release.set();sender.join(3)
            stream.port=None;port.close();reader.join(2)
        self.assertFalse(sender.is_alive())
        self.assertFalse(stream.inflight)
        self.assertFalse(stream.cancel)
        self.assertEqual(port.calls,3)

if __name__=='__main__':unittest.main(verbosity=2)
