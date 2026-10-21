"""Run exact C core/auth plus real Python client through simulator serial/TCP. No hardware."""
from pathlib import Path
import argparse
from collections import deque
import importlib.util
import json
import queue
import socket
import subprocess
import tempfile
import time
import serial
ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module);return module

class FragmentedPort:
    """Deterministic partial reads/empty timeouts, including split ok and CR/LF."""
    def __init__(self,raw):self.raw=raw;self.parts=deque()
    def __getattr__(self,name):return getattr(self.raw,name)
    def reset_input_buffer(self):self.parts.clear();return self.raw.reset_input_buffer()
    def readline(self):
        if self.parts:return self.parts.popleft()
        data=self.raw.readline()
        for value in data:
            self.parts.append(bytes([value]));self.parts.append(b'')
        return self.parts.popleft() if self.parts else b''


class DropOneAck:
    def __init__(self,raw):self.raw=raw;self.armed=False;self.waiting=False;self.dropped=False;self.sequences=[]
    def __getattr__(self,name):return getattr(self.raw,name)
    def write(self,data):
        if data.startswith(b'$FFCMD='):
            seq,tag,payload=data[7:].strip().split(b',',2)
            self.sequences.append(seq)
            command=bytes.fromhex(payload.decode()).decode()
            if self.armed and not self.dropped and command.startswith('M5'):self.waiting=True
        return self.raw.write(data)
    def readline(self):
        line=self.raw.readline()
        if self.waiting and line.strip()==b'ok':
            self.waiting=False;self.dropped=True
            return b''
        return line


def scenario(binary,label,legacy=1,speed=0,fragmented=False,interruption=None,drop_ack=False,off_at_pause=False):
    client=load('review_auth_'+label,ROOT/'python/cnc_ffst_auth_source.py')
    page=load('review_page_'+label,ROOT/'python/UART/CNC_FFST_Unico.py')
    with tempfile.TemporaryDirectory(prefix='ffst-native-review-') as temporary:
        base=Path(temporary)
        identity=base/'identity.json'
        identity.write_text(json.dumps({'firmware':'CNC_FFST-S3-0.1.3','app_image_sha256':'11'*32}))
        with socket.socket() as reservation:
            reservation.bind(('127.0.0.1',0));number=reservation.getsockname()[1]
        log=(base/'sim.log').open('w')
        process=subprocess.Popen([str(binary),'-n','-t',str(speed),'-p',str(number),
            '-e',str(base/'EEPROM.DAT'),'-s','/dev/null','-b',str(base/'blocks')],
            stdin=subprocess.DEVNULL,stdout=log,stderr=log)
        stream=port=None
        try:
            for attempt in range(50):
                try:
                    raw=serial.serial_for_url(f'socket://127.0.0.1:{number}',timeout=.1,write_timeout=2)
                    break
                except serial.SerialException:
                    if process.poll() is not None:raise RuntimeError('Simulator failed to start')
                    time.sleep(.1)
            else:raise TimeoutError('Simulator port did not open')
            dropper=DropOneAck(raw)
            raw=dropper
            if fragmented:raw=FragmentedPort(raw)
            port=client.SignedPort(raw,b'K'*32,boot_wait=3 if speed else .2,identity_path=identity)
            port._ack_probe_after=.2
            stream=page.Streamer(queue.Queue());stream.port=port
            stream.reader=stream.start_worker(stream.read_loop)
            for command in ['$X','$13=0',f'$39={legacy}','G21G90G94','G0X0Y0Z0']:
                stream.sync_command(command,5)
            def wait(condition,limit=30):
                end=time.monotonic()+limit
                while not condition() and time.monotonic()<end:
                    if port.failure:raise port.failure
                    stream.realtime(b'?');time.sleep(.02)
                if not condition():raise TimeoutError('Native scenario: '+port.communication_diagnostics())
            if interruption == 'native_macro':
                stream.send_manual('G1X.4F600\nM0\nG1X.8\nM5')
                wait(lambda:stream.m0_stopped.is_set() or stream.cancel)
                assert stream.m0_stopped.is_set() and not stream.cancel, 'Native M0 did not stop'
                wait(lambda:port._receipt_query is not None)
                stream.realtime(b'~')
                stream.m0_waiting=False
                wait(lambda:not stream.running or stream.cancel)
                assert not stream.cancel, 'Signed resume failed inside native M0'
                stream.wait_idle(5)
                assert abs(stream.work_position[0]-.8)<.006, stream.work_position
                print(f'PASS {label}: asynchronous macro, real native M0, pending receipt and signed resume with $39={legacy}.',flush=True)
                return
            lines=['G21 G90 G94','M5' if off_at_pause else 'M3 S300']+[f'G1 X{i*.04:.2f} F600' for i in range(1,101)]
            lines+=['M0']+[f'G1 X{i*.04:.2f}' for i in range(101,201)]+['M5']
            stream.start(lines,128,[])
            wait(lambda:stream.m0_alignment_ready or stream.cancel)
            assert stream.m0_alignment_ready and not stream.cancel, 'Did not reach conference pause'
            anchor=stream.work_position
            if interruption:
                stream.realtime(b'\x18' if interruption=='reset' else b'!')
                wait(lambda:stream.cancel,10)
                wait(lambda:not stream.running,10)
                assert not stream._m0_resume.is_set(), 'Interruption resumed the file'
                print(f'PASS {label}: {interruption} cancels pause; no automatic continuation.',flush=True)
                return
            stream.send_manual('$J=G21G91X.1Y-.1Z.1F100')
            wait(lambda:not stream._m0_editing)
            assert not stream.cancel, 'Alignment cancelled'
            assert all(abs(a-b)<.006 for a,b in zip(anchor,stream.work_position)), 'Work coordinate drift'
            dropper.armed=drop_ack
            stream.resume_m0_alignment()
            wait(lambda:not stream.running or stream.cancel)
            assert not stream.cancel and not port.failure, 'Job did not complete'
            stream.wait_idle(5)
            assert abs(stream.work_position[0]-8)<.006, stream.work_position
            assert abs(stream.work_offset[0]-.1)<.006, stream.work_offset
            failures=[e for e in list(stream.events.queue) if e[0] in ('fault','error')]
            assert not failures, failures
            assert len(dropper.sequences)==len(set(dropper.sequences)), 'A command packet was retransmitted'
            if drop_ack:
                assert dropper.dropped and port.recovered_receipts>=1, 'Lost M5 ACK was not recovered'
            print(f'PASS {label}: real core/auth, 200 moves, M3/M5, M0, XYZ jog, G92, Retornar; '
                  f'$39={legacy}, fragments={fragmented}, lost_ack={drop_ack}, off_at_pause={off_at_pause}, recovered={port.recovered_receipts}, '
                  f'seq={port.seq}, final WPos={stream.work_position}.',flush=True)
        except Exception:
            if port:print('DIAGNOSTIC',port.communication_diagnostics(),flush=True)
            if stream:
                for event in list(stream.events.queue)[-25:]:print(event,flush=True)
            raise
        finally:
            if stream:stream.disconnect()
            elif port:port.close()
            process.kill();process.wait(timeout=3);log.close()

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--binary',required=True,type=Path)
    args=parser.parse_args()
    for config in [('legacy_on_fast',1,0,False,None,False,False),('legacy_off_realtime',0,1,False,None,False,False),
                   ('fragmented',1,0,True,None,False,False),('reset_pause',1,0,True,'reset',False,False),
                   ('hold_pause',0,1,False,'hold',False,False),('lost_m5_ack',1,0,False,None,True,False),
                   ('lost_m5_ack_fragmented',0,0,True,None,True,False),('lost_restore_m5_ack',1,0,False,None,True,True),
                   ('native_macro_pause',0,0,False,'native_macro',False,False)]:
        label,legacy,speed,fragmented,interruption,drop_ack,off_at_pause=config
        scenario(args.binary,label,legacy,speed,fragmented,interruption,drop_ack,off_at_pause)
