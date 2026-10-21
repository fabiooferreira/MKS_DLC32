"""Real C receipt ledger + real Python transport, including dropped ACKs. No motion replay."""
import importlib.util
import json
import queue
import re
import time
import unittest
from pathlib import Path
import test_auth as fixture
from test_auth import ROOT,KEY,HASH,mac

class ReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture.AuthTests.setUpClass();cls.lib=fixture.AuthTests.lib;cls.temp=fixture.AuthTests.temp
    @classmethod
    def tearDownClass(cls):fixture.AuthTests.tearDownClass()
    def setUp(self):
        self.h=fixture.AuthTests();self.h.setUp()
    def query(self,sequence=0,challenge='55'*16):
        result=self.h.line('$FFACK='+str(sequence)+','+challenge)
        return result,self.h.output()
    def test_unauthenticated_query_is_denied(self):
        self.assertEqual(self.query()[0],78);self.assertEqual(self.lib.host_executed(),0)
    def test_receipt_is_bound_to_sequence_tag_and_challenge(self):
        self.h.hello();tag=self.h.envelope('M5').split(',')[1]
        self.assertEqual(self.h.signed('M5'),0)
        result,output=self.query();self.assertEqual(result,0)
        proof=mac('ack|'+self.h.nonce+'|'+'55'*16+'|0|'+tag+'|0')
        self.assertIn('[FFACK:0:'+'55'*16+':0:'+proof+']',output)
        self.assertEqual(self.h.signed('G1X2F100'),0)
        self.assertEqual(self.lib.host_executed(),2)
    def test_repeated_queries_never_execute_or_consume_command_sequence(self):
        self.h.hello();self.h.signed('M5')
        first=self.query();second=self.query()
        self.assertEqual(first,second);self.assertEqual(self.lib.host_executed(),1)
        self.assertEqual(self.h.signed('G0X1'),0)
        self.assertEqual(self.lib.host_executed(),2)
    def test_unknown_sequence_has_authenticated_pending_receipt(self):
        self.h.hello();result,output=self.query(7)
        proof=mac('ack|'+self.h.nonce+'|'+'55'*16+'|7|PENDING')
        self.assertEqual(result,0)
        self.assertIn('[FFACK:7:'+'55'*16+':PENDING:'+proof+']',output)
        self.assertEqual(self.lib.host_executed(),0)
    def test_safety_error_is_retained_without_becoming_success(self):
        self.h.hello();tag=self.h.envelope('G0X1').split(',')[1]
        self.lib.host_state(2);self.assertEqual(self.h.signed('G0X1'),9)
        result,output=self.query()
        proof=mac('ack|'+self.h.nonce+'|'+'55'*16+'|0|'+tag+'|9')
        self.assertEqual(result,0)
        self.assertIn(':9:'+proof+']',output)
        self.assertEqual(self.lib.host_executed(),0)
    def test_reset_invalidates_receipt(self):
        self.h.hello();self.h.signed('M5');self.lib.host_reset()
        self.assertEqual(self.query()[0],78)
        self.h.hello();self.assertIn(':PENDING:',self.query()[1])
    def test_malformed_query_is_denied(self):
        self.h.hello()
        for command in ['$FFACK=00,'+'55'*16,'$FFACK=0,short','$FFACK=0,'+'55'*16+',extra']:
            self.assertEqual(self.h.line(command),78)
        self.assertEqual(self.lib.host_executed(),0)

    def client(self,drop_command=False,drop_header=False,tamper=False,late_ack=False,drop_end=False,short_query=False):
        lib=self.lib
        spec=importlib.util.spec_from_file_location('receipt_client',ROOT/'python/cnc_ffst_auth_source.py')
        client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
        class Raw:
            is_open=True
            def __init__(self):self.rx=queue.Queue();self.commands=[];self.queries=0;self.saved=b''
            def close(self):self.is_open=False
            def reset_input_buffer(self):
                while not self.rx.empty():self.rx.get_nowait()
            def readline(self):
                try:return self.rx.get(timeout=.01)
                except queue.Empty:return b''
            def write(self,data):
                is_command=data.startswith(b'$FFCMD=');is_query=data.startswith(b'$FFACK=')
                if is_command:
                    self.commands.append(data)
                    if drop_command:return len(data)
                if is_query:
                    self.queries+=1
                    if short_query:return len(data)-1
                lib.host_clear();lib.host_serial_bytes(data,len(data));output=lib.host_output()
                if is_command:
                    self.saved=output;return len(data) # Lose the command's ACK, not the command.
                if is_query:
                    if drop_header:output=b'ok\r\n'
                    elif tamper:
                        output=re.sub(rb'(:)([0-9a-f]{64})(\])',lambda m:m[1]+(b'0' if m[2][:1]!=b'0' else b'1')+m[2][1:]+m[3],output)
                    if drop_end:output=output.replace(b'ok\r\n',b'')
                    if late_ack:output=self.saved+output
                for line in output.splitlines(keepends=True):self.rx.put(line)
                return len(data)
        identity=Path(self.temp.name)/'receipt_identity.json'
        identity.write_text(json.dumps({'firmware':'CNC_FFST-S3-0.1.3','app_image_sha256':HASH}))
        raw=Raw();port=client.SignedPort(raw,KEY,boot_wait=0,identity_path=identity)
        port._ack_probe_after=.02;port._ack_timeout=.4
        return raw,port
    def read_result(self,port):
        deadline=time.monotonic()+2;lines=[]
        while time.monotonic()<deadline:
            try:line=port.readline()
            except OSError:return lines
            if line:lines.append(line)
            if line==b'ok\n' or line.startswith(b'error:'):return lines
        self.fail('No result or failure within test deadline')
    def test_lost_ack_recovers_without_resending_command(self):
        raw,port=self.client()
        try:
            port.write(b'M5\n');lines=self.read_result(port)
            self.assertEqual(lines[-1],b'ok\n')
            self.assertEqual(port.recovered_receipts,1)
            self.assertEqual(len(raw.commands),1);self.assertEqual(self.lib.host_executed(),1)
            port.write(b'G1X2F100\n');self.assertEqual(self.read_result(port)[-1],b'ok\n')
            self.assertEqual(len(raw.commands),2);self.assertEqual(self.lib.host_executed(),2)
        finally:port.close()
    def test_late_original_ack_and_query_ack_produce_one_ack(self):
        raw,port=self.client(late_ack=True)
        try:
            port.write(b'M5\n');self.assertEqual(self.read_result(port)[-1],b'ok\n')
            self.assertEqual(port.readline(),b'')
            self.assertEqual(port.recovered_receipts,1);self.assertEqual(len(raw.commands),1)
        finally:port.close()
    def test_missing_command_is_not_replayed_and_times_out_even_without_next_write(self):
        raw,port=self.client(drop_command=True)
        try:
            port.write(b'G0X1\n');lines=self.read_result(port)
            self.assertFalse(any(line==b'ok\n' for line in lines))
            self.assertIsNotNone(port.failure)
            self.assertEqual(self.lib.host_executed(),0);self.assertEqual(len(raw.commands),1)
            self.assertEqual(port.recovered_receipts,0)
        finally:port.close()
    def test_bare_query_ok_without_header_never_confirms_missing_command(self):
        raw,port=self.client(drop_command=True,drop_header=True)
        try:
            port.write(b'G0X1\n');lines=self.read_result(port)
            self.assertFalse(any(line==b'ok\n' for line in lines))
            self.assertIsNotNone(port.failure);self.assertEqual(self.lib.host_executed(),0)
            self.assertEqual(port.recovered_receipts,0)
        finally:port.close()
    def test_forged_proof_blocks_connection(self):
        raw,port=self.client(tamper=True)
        try:
            port.write(b'M5\n');lines=self.read_result(port)
            self.assertFalse(any(line==b'ok\n' for line in lines))
            self.assertIsNotNone(port.failure);self.assertEqual(port.recovered_receipts,0)
            with self.assertRaises(Exception):port.write(b'G0X1\n')
            self.assertEqual(len(raw.commands),1)
        finally:port.close()
    def test_recovered_safety_error_remains_error(self):
        raw,port=self.client()
        try:
            self.lib.host_state(2)
            port.write(b'G0X1\n');lines=self.read_result(port)
            self.assertEqual(lines[-1],b'error:9\n')
            self.assertEqual(self.lib.host_executed(),0)
            self.assertEqual(len(raw.commands),1)
        finally:port.close()
    def test_short_query_write_stops_without_retransmission(self):
        raw,port=self.client(short_query=True)
        try:
            port.write(b'M5\n');lines=self.read_result(port)
            self.assertFalse(any(line==b'ok\n' for line in lines))
            self.assertIsNotNone(port.failure);self.assertEqual(port.recovered_receipts,0)
            self.assertEqual(len(raw.commands),1)
        finally:port.close()
    def test_explicit_operation_budget_is_used_for_a_long_probe(self):
        raw,port=self.client(drop_command=True)
        try:
            port.write_with_timeout(b'G38.2Z-1F1\n',10)
            self.assertEqual(port._pending_timeout,10)
            self.assertEqual(port._pending_command,'G38.2Z-1F1')
        finally:port.close()
    def test_indefinite_budget_is_only_accepted_for_explicit_native_pause(self):
        raw,port=self.client(drop_command=True)
        try:
            with self.assertRaises(ValueError):port.write_with_timeout(b'G0X1\n',float('inf'))
            self.assertFalse(raw.commands)
            port.write_with_timeout(b'M0\n',float('inf'))
            self.assertEqual(port._pending_timeout,float('inf'))
        finally:port.close()
    def test_dwell_uses_declared_duration_without_unbounded_wait(self):
        raw,port=self.client(drop_command=True)
        try:
            port.write(b'G4P300\n')
            self.assertEqual(port._pending_timeout,330)
            self.assertEqual(len(raw.commands),1)
        finally:port.close()
    def test_progress_and_fresh_hold_extend_wait_but_stationary_run_does_not(self):
        from unittest.mock import patch
        spec=importlib.util.spec_from_file_location('budget_client',ROOT/'python/cnc_ffst_auth_source.py')
        client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
        port=client.SignedPort.__new__(client.SignedPort)
        port._pending_since=100;port._pending_timeout=120;port._ack_timeout=120
        port.last_motion_progress=0;port._last_status_at=0
        port._last_machine_state='';port._last_reported_position=None
        with patch.object(client.time,'monotonic',return_value=219):
            port._track_status(b'<Run|MPos:1,0,0,0>\n')
        with patch.object(client.time,'monotonic',return_value=221):
            self.assertTrue(port._ack_expired())  # A state label alone proves no progress.
            port._track_status(b'<Run|MPos:2,0,0,0>\n')
            self.assertFalse(port._ack_expired())
        with patch.object(client.time,'monotonic',return_value=342):
            port._track_status(b'<Run|MPos:2,0,0,0>\n')
            self.assertTrue(port._ack_expired())
            port._track_status(b'<Hold:0|MPos:2,0,0,0>\n')
            self.assertFalse(port._ack_expired())
        with patch.object(client.time,'monotonic',return_value=346):
            self.assertTrue(port._ack_expired())  # A disconnected/stale Hold cannot wait forever.
    def test_missing_query_terminator_is_not_mistaken_for_success(self):
        raw,port=self.client(drop_end=True)
        try:
            port.write(b'M5\n');lines=self.read_result(port)
            self.assertFalse(any(line==b'ok\n' for line in lines))
            self.assertIsNotNone(port.failure);self.assertEqual(port.recovered_receipts,0)
        finally:port.close()

if __name__=='__main__':unittest.main(verbosity=2)
