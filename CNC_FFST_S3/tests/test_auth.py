"""Compile the real S3 auth adapter for host testing; no physical motion/eFuses."""
import ctypes
import hashlib
import hmac
import importlib.util
import json
import queue
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import time

ROOT=Path(__file__).resolve().parents[1]
KEY=b'K'*32
HASH='11'*32

def mac(message):return hmac.new(KEY,message.encode(),hashlib.sha256).hexdigest()

class AuthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        binary=Path(cls.temp.name)/'auth.so'
        subprocess.run(['gcc','-shared','-fPIC','-DFFST_HOST_TEST','-I'+str(ROOT/'tests'),
                        '-I'+str(ROOT/'firmware/main'),str(ROOT/'tests/host_env.c'),
                        str(ROOT/'firmware/main/ffst_auth.c'),'-lcrypto','-o',str(binary)],check=True)
        cls.lib=ctypes.CDLL(str(binary))
        cls.lib.host_output.restype=ctypes.c_char_p
        cls.lib.host_last_command.restype=ctypes.c_char_p
        cls.lib.host_line.argtypes=[ctypes.c_char_p]
        cls.lib.host_frame.argtypes=[ctypes.c_char_p,ctypes.c_uint]
        cls.lib.host_serial_bytes.argtypes=[ctypes.c_char_p,ctypes.c_uint]
    @classmethod
    def tearDownClass(cls):cls.temp.cleanup()
    def setUp(self):self.lib.host_init();self.seq=0;self.rtseq=0
    def line(self,line):self.lib.host_clear();return self.lib.host_line(line.encode())
    def output(self):return self.lib.host_output().decode()
    def hello(self):
        self.assertEqual(self.line('$FFHELLO'),0)
        match=re.search(r'\[FFNONCE:([a-f0-9]{64}):([a-f0-9]{64})\]',self.output())
        self.assertIsNotNone(match);self.nonce=match[1]
        self.assertEqual(match[2],mac('server|'+self.nonce+'|'+HASH))
        self.proof=mac('client|'+self.nonce+'|'+HASH)
        self.assertEqual(self.line('$FFAUTH='+self.proof),0)
    def envelope(self,payload,sequence=None):
        seq=str(self.seq if sequence is None else sequence);encoded=payload.encode().hex()
        return '$FFCMD='+seq+','+mac(self.nonce+'|'+seq+'|'+encoded)+','+encoded
    def signed(self,payload):
        result=self.line(self.envelope(payload));self.seq+=1;return result
    def rt_frame(self,c,seq=None):
        seq=str(self.rtseq if seq is None else seq);command=bytes([c]).hex()
        return b'\xf8'+(seq+','+mac(self.nonce+'|rt|'+seq+'|'+command)+','+command+'\n').encode()
    def serial_line(self,text,ending='\n'):
        self.lib.host_clear();data=(text+ending).encode()
        self.lib.host_serial_bytes(data,len(data))
        return self.output()
    def test_serial_line_endings_reach_command_parser(self):
        for ending in ['\n','\r','\r\n']:
            self.assertIn('[FFFW:',self.serial_line('$FFINFO',ending))
            self.assertIn('ok',self.output())
    def test_serial_identification_remains_available_in_estop(self):
        self.lib.host_state(2)
        self.assertIn('[FFFW:',self.serial_line('$FFINFO'))
        self.assertIn('ok',self.serial_line('$I'))
        self.assertIn('error:',self.serial_line('G0X1'))
        self.assertEqual(self.lib.host_executed(),1) # $I only, never motion
    def test_serial_handshake_keeps_unsigned_motion_blocked(self):
        reply=self.serial_line('$FFHELLO')
        match=re.search(r'\[FFNONCE:([a-f0-9]{64}):([a-f0-9]{64})\]',reply)
        self.assertIsNotNone(match);nonce=match[1]
        self.assertIn('[FFAUTH:OK]',self.serial_line('$FFAUTH='+mac('client|'+nonce+'|'+HASH)))
        self.assertIn('error:',self.serial_line('G0X10'))
        self.assertIn('error:',self.serial_line('$H'))
        self.assertFalse(self.lib.host_rt_allowed(ord('~')))
    def test_identity_matches_exact_firmware(self):
        self.assertEqual(self.line('$FFINFO'),0)
        self.assertIn('[FFFW:CNC_FFST-S3-0.1.3:'+HASH+']',self.output())
    def test_raw_motion_tool_homing_jog_probe_blocked(self):
        for line in ['G0X1','G1A1F1','M3S100','G38.2Z-1F1','$H','$J=G91X1F1','$N0=G0X1','$I=FAKE']:
            self.assertNotEqual(self.line(line),0,line)
        self.assertEqual(self.lib.host_executed(),0)
    def test_handshake_does_not_unlock_unsigned_motion(self):
        self.hello();self.assertNotEqual(self.line('G0X10'),0)
        self.assertNotEqual(self.line('$H'),0)
    def test_signed_motion_including_axis_a(self):
        self.hello();self.assertEqual(self.signed('G1A45F10'),0)
        self.assertEqual(self.lib.host_last_command(),b'G1A45F10')
    def test_replay_bad_mac_and_sequence_rejected(self):
        self.hello();packet=self.envelope('G0X1')
        self.assertEqual(self.line(packet),0)
        self.assertNotEqual(self.line(packet),0)
        self.assertNotEqual(self.line(self.envelope('G0X2',9)),0)
        packet=self.envelope('G0X2',1);packet=packet.replace(packet.split(',')[1],'0'*64)
        self.assertNotEqual(self.line(packet),0)
        self.assertEqual(self.lib.host_executed(),1)
    def test_reset_invalidates_old_proof_and_commands(self):
        self.hello();packet=self.envelope('G0X1');proof=self.proof
        self.lib.host_reset()
        self.assertNotEqual(self.line('$FFAUTH='+proof),0)
        self.assertNotEqual(self.line(packet),0)
        self.assertEqual(self.lib.host_executed(),0)
    def test_same_nonce_cannot_reauthenticate_and_rewind(self):
        self.hello();packet=self.envelope('G0X1');self.assertEqual(self.line(packet),0)
        self.assertNotEqual(self.line('$FFAUTH='+self.proof),0)
        self.assertNotEqual(self.line(packet),0)
    def test_unsigned_realtime_resume_blocked_even_after_auth(self):
        for connected in [False,True]:
            if connected:self.hello()
            for value in [ord('~'),0x81,0x90,0x99,0x9e,0xa0,0xa1]:
                self.assertFalse(self.lib.host_rt_allowed(value),hex(value))
    def test_public_safety_commands_remain_allowed(self):
        for value in [0x18,0x19,ord('?'),ord('!'),0x80,0x82,0x84,0x85,0x87]:
            self.assertTrue(self.lib.host_rt_allowed(value),hex(value))
    def test_signed_out_of_band_resume_and_replay(self):
        self.hello();packet=self.rt_frame(ord('~'))
        self.lib.host_clear();self.lib.host_frame(packet,len(packet))
        self.assertEqual(self.lib.host_rt_executed(),1);self.assertIn('[FFRT:OK]',self.output())
        self.lib.host_clear();self.lib.host_frame(packet,len(packet))
        self.assertEqual(self.lib.host_rt_executed(),1);self.assertIn('[FFRT:ERR]',self.output())
    def test_reset_invalidates_out_of_band_packet(self):
        self.hello();packet=self.rt_frame(ord('~'));self.lib.host_reset()
        self.lib.host_frame(packet,len(packet));self.assertEqual(self.lib.host_rt_executed(),0)
    def test_overlong_frame_never_executes(self):
        self.hello();packet=b'\xf8'+b'1'*1000+b'\n'
        self.lib.host_frame(packet,len(packet));self.assertEqual(self.lib.host_rt_executed(),0)
    def test_alarm_and_estop_still_block_signed_gcode(self):
        self.hello()
        for state in [1,2]:
            self.lib.host_state(state);self.assertNotEqual(self.signed('G0X1'),0)
        self.assertEqual(self.lib.host_executed(),0)
    def test_raw_command_cannot_inherit_long_running_signed_scope(self):
        self.hello();self.lib.host_inject_raw_during_command()
        self.assertEqual(self.signed("G38.2Z-1F1"),0)
        self.assertNotEqual(self.lib.host_nested_status(),0)
        self.assertEqual(self.lib.host_executed(),1)
    def test_public_configuration_is_limited(self):
        for line in ['$$','$G','$I','$N','$X','$100=80','$32=1']:
            self.assertEqual(self.line(line),0,line)
        for line in ['$H','$J=X1','$N0=M3','$RST=*','$SLP','$BL']:
            self.assertNotEqual(self.line(line),0,line)
    def test_existing_python_client_round_trip(self):
        spec=importlib.util.spec_from_file_location('ffst_client_s3',ROOT/'python/cnc_ffst_auth_source.py')
        client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
        lib=self.lib
        class RawPort:
            is_open=True
            port='USB_SIM'
            def __init__(self):self.rx=queue.Queue();self.writes=[]
            def reset_input_buffer(self):
                while not self.rx.empty():self.rx.get_nowait()
            def close(self):self.is_open=False
            def readline(self):
                try:return self.rx.get(timeout=.05)
                except queue.Empty:return b''
            def write(self,data):
                self.writes.append(data)
                lib.host_clear()
                if data.startswith(b'\xf8'):
                    lib.host_frame(data,len(data))
                    for line in lib.host_output().splitlines():self.rx.put(line+b'\n')
                elif data==b'\x18':
                    lib.host_reset();lib.host_frame(b'',0)
                    for response in lib.host_output().splitlines():self.rx.put(response+b'\n')
                elif data in (b'?',b'\x80'):self.rx.put(b'<Idle|MPos:0,0,0,0|FS:0,0>\n')
                else:
                    lib.host_serial_bytes(data,len(data))
                    for response in lib.host_output().splitlines():self.rx.put(response+b'\n')
                return len(data)
        identity=Path(self.temp.name)/'identity.json'
        identity.write_text(json.dumps({'firmware':'CNC_FFST-S3-0.1.3','app_image_sha256':HASH}))
        raw=RawPort();port=client.SignedPort(raw,KEY,boot_wait=0,identity_path=identity)
        try:
            port.write(b'G1A45F10\n')
            self.assertEqual(port.readline(),b'ok\n')
            self.assertEqual(lib.host_last_command(),b'G1A45F10')
            port.write(b'~')
            self.assertEqual(lib.host_rt_executed(),1)
            old_nonce=port.nonce;old_generation=port._generation
            before=lib.host_executed();sent=len(raw.writes)
            port.write(b'\x18')
            deadline=time.monotonic()+4
            while time.monotonic()<deadline and not (port._generation>old_generation and port.authenticated and port._ready.is_set()):time.sleep(.01)
            self.assertTrue(port.authenticated,str(port.failure))
            self.assertNotEqual(port.nonce,old_nonce)
            self.assertIs(port.raw,raw);self.assertTrue(raw.is_open)
            self.assertEqual(lib.host_executed(),before) # No movement replay.
            self.assertFalse(any(w.startswith(b'$FFCMD=') for w in raw.writes[sent:]))
            while port.readline():pass
            lib.host_state(2)
            current_nonce=port.nonce
            port.write(b'G0X1\n')
            self.assertEqual(port.readline(),b'error:9\n')
            self.assertTrue(port.authenticated)
            self.assertEqual(port.nonce,current_nonce) # Safety rejection keeps session.
            lib.host_state(0)
            port.write(b'G0X2\n')
            self.assertEqual(port.readline(),b'ok\n')
            self.assertEqual(lib.host_last_command(),b'G0X2')
        finally:port.close()
    def test_serial_writes_do_not_overlap_status_or_stop(self):
        import threading
        spec=importlib.util.spec_from_file_location('serial_writer_test',ROOT/'python/cnc_ffst_auth_source.py')
        client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
        entered=threading.Event();release=threading.Event();writes=[];overlap=[]
        class Raw:
            active=False
            def write(self,data):
                if self.active:overlap.append(data)
                self.active=True;writes.append(data)
                if data==b'command':entered.set();release.wait(2)
                self.active=False
                return len(data)
        port=client.SignedPort.__new__(client.SignedPort)
        port.raw=Raw();port._raw_tx=threading.Lock()
        command=threading.Thread(target=port._write_raw,args=(b'command',))
        stop=threading.Thread(target=port._write_raw,args=(b'!',))
        command.start()
        try:
            self.assertTrue(entered.wait(1))
            self.assertEqual(port._write_raw(b'?'),1)
            self.assertEqual(writes,[b'command'])
            stop.start()
            self.assertFalse(overlap)
        finally:
            release.set();command.join(2)
            if stop.ident is not None:stop.join(2)
        self.assertEqual(writes,[b'command',b'!'])
        self.assertFalse(overlap)
        self.assertEqual(port._write_raw(b'?'),1)
        self.assertEqual(writes[-1],b'?')
    def test_fragmented_serial_lines_keep_handshake_and_ack(self):
        spec=importlib.util.spec_from_file_location('fragmented_client',ROOT/'python/cnc_ffst_auth_source.py')
        client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
        original_exchange=client.exchange
        client.exchange=lambda *args,**kwargs: original_exchange(*args,timeout=.4,**kwargs)
        lib=self.lib
        class Raw:
            is_open=True
            def __init__(self):self.rx=queue.Queue();self.writes=[]
            def close(self):self.is_open=False
            def reset_input_buffer(self):
                while not self.rx.empty():self.rx.get_nowait()
            def readline(self):
                try:return self.rx.get(timeout=.01)
                except queue.Empty:return b''
            def write(self,data):
                self.writes.append(data);lib.host_clear();lib.host_serial_bytes(data,len(data))
                output=lib.host_output()
                # Serial timeout can split even 'ok' and CR/LF; empty reads do not end a line.
                for value in output:
                    self.rx.put(bytes([value]));self.rx.put(b'')
                return len(data)
        identity=Path(self.temp.name)/'fragmented_identity.json'
        identity.write_text(json.dumps({'firmware':'CNC_FFST-S3-0.1.3','app_image_sha256':HASH}))
        raw=Raw();port=client.SignedPort(raw,KEY,boot_wait=0,identity_path=identity)
        try:
            for command in [b'M5\n',b'G1X2F100\n']:
                port.write(command)
                deadline=time.monotonic()+1;reply=b''
                while not reply and time.monotonic()<deadline:reply=port.readline()
                self.assertEqual(reply,b'ok\r\n')
                self.assertTrue(port.authenticated)
            self.assertEqual(len([w for w in raw.writes if w.startswith(b'$FFCMD=')]),2)
            self.assertEqual(lib.host_last_command(),b'G1X2F100')
            lib.host_state(2)
            port.write(b'G0X3\n')
            reply=b'';deadline=time.monotonic()+1
            while not reply and time.monotonic()<deadline:reply=port.readline()
            self.assertEqual(reply,b'error:9\r\n')
            self.assertEqual(lib.host_last_command(),b'G1X2F100')
        finally:port.close()
    def test_status_and_hold_use_canonical_bytes_independent_of_legacy_setting(self):
        import threading
        spec=importlib.util.spec_from_file_location('rt_wire_client',ROOT/'python/cnc_ffst_auth_source.py')
        client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
        class Raw:
            is_open=True
            def __init__(self):self.writes=[]
            def write(self,data):self.writes.append(data);return len(data)
        port=client.SignedPort.__new__(client.SignedPort)
        port.raw=Raw();port._closed=False;port._recovering=False;port._raw_tx=threading.Lock()
        self.assertEqual(port.write(b'?'),1)
        self.assertEqual(port.write(b'!\x18'),2)
        self.assertEqual(port.raw.writes,[b'\x80',b'\x82\x18'])
    def test_close_session_invalidates_old_signed_packets(self):
        self.hello();packet=self.envelope('G0X1')
        self.assertEqual(self.line('$FFBYE'),0)
        self.assertNotEqual(self.line(packet),0)
        self.assertEqual(self.lib.host_executed(),0)
    def test_reset_notice_is_single_and_discards_stale_realtime(self):
        self.hello();self.lib.host_reset();self.lib.host_reset()
        self.lib.host_clear();self.lib.host_frame(b'',0)
        self.assertEqual(self.output().count('[FFSESSION:RESET]'),1)
        self.lib.host_clear();self.lib.host_frame(b'',0)
        self.assertNotIn('[FFSESSION:RESET]',self.output())
    def test_guards_present_in_real_core_entry_points(self):
        protocol=(ROOT/'firmware/main/grbl/protocol.c').read_text()
        self.assertNotIn('system_execute_line(',protocol)
        self.assertNotIn('gc_execute_block(',protocol)
        for file,expected in [('gcode.c','if(!ffst_auth_trusted()) return Status_AccessDenied;'),
                              ('system.c','if(ffst_auth_system(line, &auth_result)) return auth_result;'),
                              ('protocol.c','if(ffst_auth_rx(c) || !ffst_auth_realtime_allowed(c)) return true;')]:
            self.assertIn(expected,(ROOT/'firmware/main/grbl'/file).read_text())

if __name__=='__main__':unittest.main(verbosity=2)
