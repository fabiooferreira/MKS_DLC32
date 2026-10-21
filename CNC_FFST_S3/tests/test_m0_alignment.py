"""Real Python Streamer and reader with a GRBL coordinate model; not hardware validation."""
import importlib.util
from pathlib import Path
import queue
import re
import threading
import time
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('m0_control', ROOT/'python/UART/CNC_FFST_Unico.py')
page=importlib.util.module_from_spec(spec);spec.loader.exec_module(page)

class ModelPort:
    is_open=True
    failure=None
    def __init__(self):
        self.rx=queue.Queue();self.writes=[];self.machine=[10.,20.,5.];self.offset=[0.,0.,0.]
        self.absolute=True;self.scale=1.;self.feed=100.;self.tool='M3';self.speed=1000.;self.state='Idle'
    def close(self):self.is_open=False
    def readline(self):
        try:return self.rx.get(timeout=.02)
        except queue.Empty:return b''
    def reply(self,line):self.rx.put((line+'\n').encode())
    def write(self,data):
        text=data.decode().strip();self.writes.append(text)
        if text=='?':
            self.reply('<'+self.state+'|MPos:'+','.join(map(str,self.machine))+'|WCO:'+','.join(map(str,self.offset))+'|FS:0,0>')
            return len(data)
        if text in ('!','\x18'):return len(data)
        if text=='$G':
            self.reply('[GC:G1 G54 G17 '+('G21' if self.scale==1 else 'G20')+' '+('G90' if self.absolute else 'G91')+' G94 '+self.tool+' M9 F'+str(self.feed)+' S'+str(self.speed)+']')
        elif text=='$$':self.reply('$13=0')
        elif self.state!='Idle':self.reply('error:9');return len(data)
        else:
            jog=text.startswith('$J=');text=text[3:] if jog else text
            words=[(k,float(v)) for k,v in re.findall(r'([A-Z])([+-]?(?:\d+(?:\.\d*)?|\.\d+))',text)]
            gs=[v for k,v in words if k=='G'];absolute=self.absolute;scale=self.scale
            if 20 in gs:scale=25.4
            if 21 in gs:scale=1.
            if 90 in gs:absolute=True
            if 91 in gs:absolute=False
            if not jog:self.absolute=absolute;self.scale=scale
            for key,value in words:
                if key in 'XYZ':
                    i='XYZ'.index(key)
                    if 92 in gs:self.offset[i]=self.machine[i]-value*scale
                    else:self.machine[i]=value*scale+self.offset[i] if absolute else self.machine[i]+value*scale
                elif key=='M':self.tool='M'+str(int(value))
                elif key=='F':self.feed=value
                elif key=='S':self.speed=value
        self.reply('ok');return len(data)

class M0Tests(unittest.TestCase):
    def setUp(self):
        self.stream=page.Streamer(queue.Queue());self.port=ModelPort();self.stream.port=self.port
        self.reader=threading.Thread(target=self.stream.read_loop,daemon=True);self.reader.start()
        self.worker=None
    def tearDown(self):
        self.stream.cancel=True
        if self.worker:self.worker.join(3)
        self.stream.port=None;self.port.close();self.reader.join(1)
    def wait(self,condition,timeout=5):
        end=time.monotonic()+timeout
        while not condition() and time.monotonic()<end:time.sleep(.01)
        self.assertTrue(condition(),list(self.stream.events.queue))
    def pause(self):
        self.stream.running=True
        self.worker=threading.Thread(target=self.stream.stream_loop,args=([(1,'G1X11F100'),(2,'M0'),(3,'G1X12'),(-1,'G4 P0.01')],1),daemon=True)
        self.worker.start();self.wait(lambda:self.stream.m0_alignment_ready)
        self.assertEqual(self.port.tool,'M5')
        self.assertNotIn('G1X12',self.port.writes)
        self.assertNotIn('M0',self.port.writes) # Host-managed pause, not a Hold bypass.
    def test_xyz_macros_and_jog_preserve_work_position_and_shift_remainder(self):
        self.pause();anchor=self.stream.work_position
        self.stream.send_manual('G91\nG1 X0.1 Y-0.2 Z0.3 F100\nG90')
        self.wait(lambda:not self.stream._m0_editing)
        self.assertFalse(self.stream.cancel)
        for actual,want in zip(self.port.machine,[11.1,19.8,5.3]):self.assertAlmostEqual(actual,want)
        self.assertEqual(self.stream.work_position,anchor)
        self.assertEqual(self.port.tool,'M5')
        self.stream.send_manual('$J=G91 Z0.2 F50');self.wait(lambda:not self.stream._m0_editing)
        self.assertAlmostEqual(self.port.machine[2],5.5)
        self.assertEqual(self.stream.work_position,anchor)
        self.stream.resume_m0_alignment();self.worker.join(5)
        self.assertFalse(self.worker.is_alive());self.assertFalse(self.stream.cancel)
        self.assertAlmostEqual(self.port.machine[0],12.1)
        self.assertEqual(self.port.tool,'M3')
        self.assertEqual(sum(w.startswith('G92 ') for w in self.port.writes),2)
    def test_unsafe_macro_is_rejected_whole_without_motion(self):
        self.pause()
        for bad in ['G91\nG1X.1F100\nM3S100', 'G38.2Z-1F10', 'G92X0', '$H', 'G53G0X0', 'G1A1F100','G1X1F0']:
            before=list(self.port.writes)
            with self.assertRaises(ValueError):self.stream.send_manual(bad)
            self.assertEqual(before,self.port.writes)
        self.assertTrue(self.stream.m0_alignment_ready)
    def test_resume_during_adjustment_is_rejected(self):
        self.pause();self.stream._m0_editing=True
        with self.assertRaises(RuntimeError):self.stream.resume_m0_alignment()
        self.assertFalse(self.stream._m0_resume.is_set())
        self.assertEqual(self.port.tool,'M5')
        self.stream._m0_editing=False
    def test_reset_cancels_pause_without_rearming_tool(self):
        self.pause();self.port.reply('[FFSESSION:RESET]')
        self.wait(lambda:self.stream.cancel)
        self.worker.join(3)
        self.assertFalse(self.worker.is_alive());self.assertEqual(self.port.tool,'M5')
        self.assertNotIn('G1X12',self.port.writes)
    def test_alarm_before_adjustment_cancels_job_without_motion(self):
        self.pause();before=self.port.machine[:];self.port.state='Alarm'
        self.stream.send_manual('$J=G91X.1F100');self.wait(lambda:not self.stream._m0_editing)
        self.assertTrue(self.stream.cancel);self.assertEqual(before,self.port.machine)
        self.assertEqual(self.port.tool,'M5')
    def test_existing_offset_is_preserved_and_incremented(self):
        self.port.offset=[2.,3.,4.]
        self.pause();anchor=self.stream.work_position
        self.stream.send_manual('$J=G21G91X.1F100');self.wait(lambda:not self.stream._m0_editing)
        self.assertFalse(self.stream.cancel)
        self.assertAlmostEqual(self.port.offset[0],2.1)
        self.assertEqual(self.port.offset[1:],[3.,4.])
        self.assertEqual(self.stream.work_position,anchor)
    def test_jog_step_is_mm_even_when_file_uses_inches(self):
        self.port.scale=25.4
        self.pause();before=self.port.machine[:]
        self.stream.send_manual('$J=G21G91X.1F100');self.wait(lambda:not self.stream._m0_editing)
        self.assertFalse(self.stream.cancel)
        self.assertAlmostEqual(self.port.machine[0]-before[0],.1)
        self.assertEqual(self.port.scale,25.4)
    def test_normal_manual_motion_updates_coordinates_outside_pause(self):
        self.stream.send_manual('G1X12F100')
        self.wait(lambda:not self.stream.inflight)
        self.stream.fresh_status()
        self.assertEqual(self.stream.work_position,(12.,20.,5.))
        self.assertFalse(any(w.startswith('G92') for w in self.port.writes))
    def test_file_origin_change_after_pause_is_rejected_before_sending(self):
        for lines in [['M0','G92X0'], ['M0','G10L20P0X0'], ['M0','$H'], ['M0 G1X1']]:
            with self.assertRaises(RuntimeError):self.stream.start(lines,128,[])
            self.assertFalse(self.port.writes)
    def test_safe_tool_off_macro_is_allowed(self):
        self.pause();self.stream.send_manual('M5');self.wait(lambda:not self.stream._m0_editing)
        self.assertFalse(self.stream.cancel)
        self.assertEqual(self.port.tool,'M5')
    def test_disconnect_ends_worker_and_clears_execution_state(self):
        ended=threading.Event()
        def operation():
            while not self.stream.cancel:time.sleep(.01)
            ended.set()
        self.stream.running=True;self.stream.paused=True
        self.stream.m0_waiting=True;self.stream._m0_managed=True
        self.stream._m0_anchor=(1.,2.,3.)
        worker=self.stream.start_worker(operation)
        self.stream.disconnect()
        self.assertTrue(ended.is_set());self.assertFalse(worker.is_alive())
        self.assertIsNone(self.stream.port);self.assertFalse(self.port.is_open)
        self.assertFalse(self.stream.running or self.stream.paused or self.stream.m0_waiting)
        self.assertFalse(self.stream._workers or self.stream.inflight)
        self.assertIsNone(self.stream._m0_anchor)
    def test_jog_ack_before_motion_finished_does_not_send_gcode_while_jogging(self):
        original=self.port.write
        ended=threading.Event()
        def delayed_write(data):
            result=original(data)
            if data.startswith(b'$J='):
                self.port.state='Jog'
                def finish():self.port.state='Idle';ended.set()
                threading.Timer(.2,finish).start()
            return result
        self.port.write=delayed_write
        self.pause()
        self.stream.send_manual('$J=G21G91X.1F100')
        self.wait(lambda:not self.stream._m0_editing)
        self.assertFalse(self.stream.cancel, list(self.stream.events.queue))
        self.assertTrue(ended.is_set())
        self.assertTrue(self.stream.m0_alignment_ready)
        self.assertEqual(self.stream.work_position,self.stream._m0_anchor)
    def test_hold_during_jog_cancels_without_applying_g92_or_resuming(self):
        original=self.port.write
        def held_write(data):
            result=original(data)
            if data.startswith(b'$J='):self.port.state='Hold:0'
            return result
        self.port.write=held_write
        self.pause();self.stream.send_manual('$J=G21G91X.1F100')
        self.wait(lambda:not self.stream._m0_editing)
        self.assertTrue(self.stream.cancel)
        self.assertFalse(any(w.startswith('G92') for w in self.port.writes))
        self.assertNotIn('G1X12',self.port.writes)
        self.assertEqual(self.port.tool,'M5')
    def test_no_adjustment_is_available_outside_m0(self):
        with self.assertRaises(RuntimeError):self.stream.start_m0_alignment('G91X.1F100')
        self.assertFalse(self.port.writes)

if __name__=='__main__':unittest.main(verbosity=2)
