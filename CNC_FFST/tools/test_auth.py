"""Exercise actual FFSTAuth.cpp with host GPIO/NVS/RTOS shims and the Python transport.

Crypto shim uses OpenSSL HMAC-SHA256; the ESP32 build uses mbedTLS.
This is not a hardware, GUI, network-stack or motion test.
"""
from pathlib import Path
import hashlib
import hmac
import importlib.util
import json
import queue
import subprocess
import tempfile
import threading
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('cnc_ffst_auth', ROOT/'python/cnc_ffst_auth.py')
auth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auth)
KEY = bytes.fromhex('42'*32)  # test fixture only; never provisioned into shipped firmware

STUB = r'''
#pragma once
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <cstdio>
#include <string>
#include <iostream>
enum class Error : uint8_t { Ok=0, AuthenticationFailed=110 };
enum class State { Idle, Alarm, Cycle };
enum class SpindleState { Disable, Cw };
enum class Cmd : uint8_t { Reset=0x18,StatusReport='?',FeedHold='!',SafetyDoor=0x84,JogCancel=0x85 };
namespace WebUI { enum class AuthenticationLevel { LEVEL_GUEST }; }
constexpr uint8_t CLIENT_COUNT=6,CLIENT_ALL=255,CLIENT_SERIAL=0;
using TaskHandle_t=void*;
inline void* currentTask=(void*)1;
inline void* xTaskGetCurrentTaskHandle() { return currentTask; }
struct HostSystem { State state=State::Idle; bool abort=false; }; inline HostSystem sys;
struct HostGC { struct { SpindleState spindle=SpindleState::Disable; } modal; }; inline HostGC gc_state;
struct HostRT { struct { bool reset=false; } bit; }; inline HostRT sys_rt_exec_state;
inline std::string output;
inline void grbl_send(uint8_t,const char* s) { output+=s; }
inline void grbl_sendf(uint8_t,const char* fmt,...) {
 char b[1024]; va_list a;va_start(a,fmt);vsnprintf(b,sizeof(b),fmt,a);va_end(a);output+=b;
}
Error execute_line(char*,uint8_t,WebUI::AuthenticationLevel);
void execute_realtime_command(Cmd,uint8_t);
'''
PREFS = r'''
#pragma once
#include <cstring>
inline unsigned char stored[32]; inline bool hasKey=false;
class Preferences { public:
 bool begin(const char*,bool) { return true; }
 size_t getBytesLength(const char*) { return hasKey?32:0; }
 size_t getBytes(const char*,void* p,size_t n) { if(!hasKey)return 0;memcpy(p,stored,n);return n; }
 size_t putBytes(const char*,const void* p,size_t n) { memcpy(stored,p,n);hasKey=true;return n; }
 void end() {}
};
'''
MD = r'''
#pragma once
#include <openssl/hmac.h>
#define MBEDTLS_MD_SHA256 1
inline const EVP_MD* mbedtls_md_info_from_type(int) { return EVP_sha256(); }
inline int mbedtls_md_hmac(const EVP_MD* md,const unsigned char* key,size_t n,
 const unsigned char* msg,size_t len,unsigned char* out) {
 unsigned count=0;return HMAC(md,key,n,msg,len,out,&count)?0:-1;
}
'''
MAIN = r'''
#include "stub.h"
#include "FFSTAuth.h"
#include <algorithm>
Error execute_line(char* text,uint8_t client,WebUI::AuthenticationLevel) {
 if(!ffst_auth_trusted(client))return Error::AuthenticationFailed;
 output+="[EXEC:"+std::string(text)+"]\r\n";return Error::Ok;
}
void execute_realtime_command(Cmd cmd,uint8_t client) {
 if(!ffst_auth_realtime(uint8_t(cmd),client)) { output+="[RT:DENIED]\r\n";return; }
 if(cmd==Cmd::Reset)ffst_auth_reset();
 output+="[RT:OK]\r\n";
}
int main() {
 ffst_auth_init();
 std::string wire;
 while(std::getline(std::cin,wire)) {
   if(wire.size()<2)continue;
   uint8_t client=wire[0]-'0';std::string line=wire.substr(2);
   output.clear();Error result=Error::AuthenticationFailed;bool ack=true;
   if(line.rfind("@FRAME:",0)==0) {
      ffst_auth_rx(0xf8,client);
      for(char c:line.substr(7))ffst_auth_rx(c,client);
      ffst_auth_rx('\n',client);ack=false;
   }
   else if(line=="@RESET") {ffst_auth_reset();output="Grbl 1.1\r\n";result=Error::Ok;}
   else if(line=="@BUSY") {sys.state=State::Cycle;result=Error::Ok;}
   else if(line=="@IDLE") {sys.state=State::Idle;result=Error::Ok;}
   else if(line=="@TRUSTCHECK") {
     // A different RTOS task must never inherit the current executing task's privilege.
     result=ffst_auth_trusted(client)?Error::AuthenticationFailed:Error::Ok;
   }
   else if(line.rfind("@RT:",0)==0) {
     unsigned c=strtoul(line.c_str()+4,nullptr,16);
     execute_realtime_command(static_cast<Cmd>(c),client); result=Error::Ok;
   }
   else {
    char buffer[768];snprintf(buffer,sizeof(buffer),"%s",line.c_str());
    if(!ffst_auth_handle(buffer,client,result)) {
      if(line.size() && line[0]=='$') {
        size_t equal=line.find('=');
        std::string name=line.substr(1,equal==std::string::npos?equal:equal-1);
        if(equal!=std::string::npos) {
          if(ffst_auth_setting(name.c_str(),line.c_str()+equal+1,client))result=Error::Ok;
        } else if(ffst_auth_command(name.c_str(),client))result=Error::Ok;
      }
    }
   }
   std::cout<<output<<(ack?(result==Error::Ok?"ok\r\n":"error:110\r\n"):"")<<std::flush;
 }
}
'''


class HostPort:
    def __init__(self, binary):
        self.process = subprocess.Popen([str(binary)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.client = 0
        self.is_open = True
        self.rx = queue.Queue()
        self.sent = []
        def pump():
            for line in self.process.stdout:
                self.rx.put(line)
        threading.Thread(target=pump, daemon=True).start()

    def write(self, data):
        self.sent.append(bytes(data))
        if data.startswith(b'\xf8'):
            data = b'@FRAME:' + data[1:]
        elif data == b'\x18':
            data = b'@RESET\n'
        elif len(data) == 1:
            data = ('@RT:' + data.hex() + '\n').encode()
        self.process.stdin.write(str(self.client).encode() + b'|' + data)
        self.process.stdin.flush()
        return len(self.sent[-1])

    def readline(self):
        try:
            return self.rx.get(timeout=.1)
        except queue.Empty:
            return b''

    def reset_input_buffer(self):
        while not self.rx.empty():
            self.rx.get_nowait()

    def close(self):
        if self.is_open:
            self.is_open = False
            self.process.terminate()
            self.process.wait(timeout=3)
            self.process.stdin.close()
            self.process.stdout.close()


class AuthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        root = Path(cls.temp.name)
        (root/'mbedtls').mkdir()
        (root/'freertos').mkdir()
        (root/'freertos/semphr.h').write_text('#pragma once\n#include <mutex>\nusing SemaphoreHandle_t=std::recursive_mutex*;\nconstexpr int portMAX_DELAY=0;\ninline auto xSemaphoreCreateRecursiveMutex(){return new std::recursive_mutex;}\ninline void xSemaphoreTakeRecursive(SemaphoreHandle_t m,int){m->lock();}\ninline void xSemaphoreGiveRecursive(SemaphoreHandle_t m){m->unlock();}\n')
        (root/'esp_partition.h').write_text('#pragma once\nstruct esp_partition_t{};\nconstexpr int ESP_OK=0;\ninline int esp_partition_get_sha256(const esp_partition_t*,unsigned char* h){memset(h,0x11,32);return ESP_OK;}\n')
        (root/'esp_ota_ops.h').write_text('#pragma once\n#include <esp_partition.h>\ninline const esp_partition_t* esp_ota_get_running_partition(){static esp_partition_t p;return &p;}\n')
        cls.identity=root/'firmware_identity.json'
        cls.identity.write_text(json.dumps({'firmware':'CNC_FFST-0.3.0','app_image_sha256':'11'*32}))
        (root/'stub.h').write_text(STUB)
        record = b'FFST_SHAREDKEY1:' + KEY + b':FFST_KEY_END'
        (root/'FFSTSharedKey.generated.h').write_text('static const volatile uint8_t ffstSharedKeyRecord[] = {' + ','.join(str(b) for b in record) + '};\n')
        (root/'mbedtls/md.h').write_text(MD)
        (root/'esp_system.h').write_text('#pragma once\ninline uint32_t esp_random(){ static uint32_t x=1; x=x*1664525+1013904223; return x;}\n')
        src = ROOT/'Firmware/Grbl_Esp32/src'
        (root/'FFSTAuth.h').write_bytes((src/'FFSTAuth.h').read_bytes())
        (root/'FFSTAuth.cpp').write_text((src/'FFSTAuth.cpp').read_text().replace('#include "Grbl.h"', '#include "stub.h"'))
        (root/'main.cpp').write_text(MAIN)
        cls.binary = root/'auth-host'
        subprocess.run(['g++','-std=c++17','-Wall','-Wextra','-Werror','-DCNC_FFST_AUTH',
                        '-I'+str(root),str(root/'FFSTAuth.cpp'),str(root/'main.cpp'),
                        '-lcrypto','-o',str(cls.binary)],check=True)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.port = HostPort(self.binary)

    def tearDown(self):
        self.port.close()

    def pair(self):
        pass  # fixed fixture credential is already compiled into the host build

    def session(self):
        lines=auth.exchange(self.port, '$FFHELLO')
        nonce=next(x for x in lines if x.startswith('[FFNONCE:')).split(':')[1]
        proof=auth.mac(KEY,'client|'+nonce+'|'+'11'*32)
        auth.exchange(self.port, '$FFAUTH='+proof)
        return nonce,proof

    def envelope(self,nonce,seq,command):
        payload=command.encode().hex()
        return '$FFCMD='+str(seq)+','+auth.mac(KEY,nonce+'|'+str(seq)+'|'+payload)+','+payload

    def denied(self,line):
        with self.assertRaises(RuntimeError):
            auth.exchange(self.port,line)

    def test_usb_and_network_cannot_replace_fixed_key(self):
        self.port.client=3
        self.denied('$FFPAIR='+KEY.hex())
        self.port.client=0
        self.pair()
        self.denied('$FFPAIR='+'55'*32)

    def test_public_config_and_unsigned_execution(self):
        for line in ['$$','$+','$G','$I','$#','$X','$100=80','$32=1']:
            auth.exchange(self.port,line)
        for line in ['G0X1','G38.2Z-1F20','M3S1','$H','$J=G91X1F100','$N0=G0X1','$NVX','$RST=*','$34=50']:
            self.denied(line)

    def test_replay_proof_cannot_rewind_sequence(self):
        self.pair(); nonce,proof=self.session()
        wire=self.envelope(nonce,0,'G0X1')
        self.assertIn('[EXEC:G0X1]',auth.exchange(self.port,wire))
        self.denied(wire)
        self.denied('$FFAUTH='+proof)
        self.denied(wire)
        auth.exchange(self.port,self.envelope(nonce,1,'M5'))

    def test_tamper_sequence_reset_and_cross_transport(self):
        self.pair(); nonce,_=self.session()
        self.denied(self.envelope(nonce,1,'G0X1'))
        wire=self.envelope(nonce,0,'G0X1')
        self.denied(wire[:-1]+('0' if wire[-1]!='0' else '1'))
        self.port.client=3
        self.denied(wire)
        self.port.client=0
        auth.exchange(self.port,wire)
        auth.exchange(self.port,'@RESET')
        self.denied(self.envelope(nonce,1,'G0X2'))

    def test_new_nonce_and_busy_public_write(self):
        self.pair(); nonce,_=self.session()
        self.session()
        self.denied(self.envelope(nonce,0,'G0X1'))
        auth.exchange(self.port,'@BUSY')
        self.denied('$100=90')
        auth.exchange(self.port,'@IDLE')
        auth.exchange(self.port,'$100=90')

    def test_signed_port_real_firmware_auth_logic(self):
        self.pair()
        port=auth.SignedPort(self.port,KEY,boot_wait=0, identity_path=self.identity)
        try:
            for command in ['G0X1','G38.2Z-1F20','$100=80','M5']:
                port.write((command+'\n').encode())
                replies=[]
                for _ in range(30):
                    line=port.readline().strip()
                    replies.append(line)
                    if line==b'ok': break
                self.assertIn(b'[EXEC:'+command.encode()+b']',replies)
                self.assertIn(b'ok',replies)
            # Realtime response must not steal an application's G-code ACK.
            port.write(b'~')
            port.write(b'G0X2\n')
            replies=[]
            for _ in range(30):
                line=port.readline().strip(); replies.append(line)
                if line==b'ok': break
            self.assertIn(b'[EXEC:G0X2]',replies)
            port.write(b'\x18')
            with self.assertRaises(RuntimeError): port.write(b'G0X3\n')
        finally:
            port.close()

    def test_oversize_and_raw_realtime(self):
        self.pair()
        for code in ['18','3f','21','84','85']:
            self.assertIn('[RT:OK]',auth.exchange(self.port,'@RT:'+code))
        for code in ['7e','99','9e']:
            self.assertIn('[RT:DENIED]',auth.exchange(self.port,'@RT:'+code))
        port=auth.SignedPort(self.port,KEY,boot_wait=0, identity_path=self.identity)
        try:
            with self.assertRaises(ValueError): port.write(b'G0X'+b'1'*201+b'\n')
            with self.assertRaises(ValueError): port.write(b'G0X1')
            port.write(b'M5\n')
            for _ in range(30):
                if port.readline().strip()==b'ok': break
            else: self.fail('Missing valid-command ACK after local rejection')
        finally: port.close()

    def test_wrong_firmware_is_rejected_before_secret(self):
        self.pair()
        path = Path(self.temp.name)/'wrong-firmware.json'
        path.write_text(json.dumps({'firmware':'CNC_FFST-0.3.0','app_image_sha256':'22'*32}))
        with self.assertRaises(RuntimeError):
            auth.SignedPort(self.port,KEY,boot_wait=0,identity_path=path)
        self.assertFalse(any(w.startswith(b'$FFAUTH=') for w in self.port.sent))

    def test_realtime_does_not_wait_for_pending_motion(self):
        self.pair()
        port=auth.SignedPort(self.port,KEY,boot_wait=0,identity_path=self.identity)
        try:
            port._ready.clear()  # simulate a G38.x ACK pending while motion is held
            port.write(b'~')
            wire=self.port.sent[-1]
            self.assertTrue(wire.startswith(b'\xf8'))
            self.assertFalse(port._ready.is_set())
            # Replay that out-of-band frame: rejected without resuming twice.
            self.port.write(wire)
            for _ in range(30):
                if port.readline().strip()==b'error:110': break
            else: self.fail('Realtime replay was not rejected')
        finally: port.close()

    def test_many_writes_without_application_reader_do_not_deadlock(self):
        self.pair()
        port=auth.SignedPort(self.port,KEY,boot_wait=0,identity_path=self.identity)
        try:
            for i in range(40): port.write(f'G0X{i}\n'.encode())
            count=0
            for _ in range(100):
                if port.readline().strip()==b'ok': count+=1
                if count==40: break
            self.assertEqual(count,40)
        finally: port.close()

    def test_wrong_key_is_rejected(self):
        self.pair()
        with self.assertRaises(RuntimeError): auth.SignedPort(self.port,b'x'*32,boot_wait=0, identity_path=self.identity)


if __name__=='__main__':
    unittest.main(verbosity=2)
