"""Host test of actual Probe.cpp logic; GPIO/ISR timing is not simulated."""
from pathlib import Path
import subprocess
import tempfile

project = Path(__file__).resolve().parents[1]
source = (project / 'Firmware/Grbl_Esp32/src/Probe.cpp').read_text()
source = source.replace('#include "Grbl.h"', '#include "stub.h"')
source = source.replace('#include "mks/MKS_draw_lvgl.h"', '')
stub = r'''
#pragma once
#include <cstdint>
#include <cstring>
#include <string>
constexpr int UNDEFINED_PIN=-1, INPUT=1, INPUT_PULLUP=2, CLIENT_SERIAL=0;
enum class MsgLevel { Info };
enum class Probe { Off, Active };
struct Flag { bool value; bool get() { return value; } };
inline Flag flag{true}; inline Flag* probe_invert=&flag;
inline int level=1, configured_mode=-1, configured_pin=-99;
inline int sys_position[3]={10,20,30}, sys_probe_position[3]={};
inline Probe sys_probe_state=Probe::Active;
struct Exec { struct { bool motionCancel=false; } bit; };
inline Exec sys_rt_exec_state;
struct PROBE_CTRL_T {};
inline int digitalRead(int) { return level; }
inline void pinMode(int p,int m) { configured_pin=p; configured_mode=m; }
inline std::string pinName(int) { return "test"; }
template<class... T> void grbl_msg_sendf(T...) {}
void probe_init(); bool probe_get_state();
void set_probe_direction(bool); void probe_state_monitor();
'''
test = r'''
#include "stub.h"
#include <cassert>
int main() {
 probe_init();
 if(PROBE_PIN==UNDEFINED_PIN) {
   assert(configured_pin==-99); assert(!probe_get_state()); return 0;
 }
 assert(configured_pin==PROBE_PIN && configured_mode==INPUT_PULLUP);
 for(bool invert : {false,true}) for(bool away : {false,true}) {
   flag.value=invert; set_probe_direction(away);
   for(int raw : {0,1}) {
     level=raw; sys_probe_state=Probe::Active;
     sys_rt_exec_state.bit.motionCancel=false;
     std::memset(sys_probe_position,0,sizeof(sys_probe_position));
     const bool active=(bool(raw)^invert);
     assert(probe_get_state()==active);
     probe_state_monitor();
     if(active^away) {
       assert(sys_probe_state==Probe::Off);
       assert(sys_rt_exec_state.bit.motionCancel);
       assert(!std::memcmp(sys_position,sys_probe_position,sizeof(sys_position)));
     } else {
       assert(sys_probe_state==Probe::Active);
       assert(!sys_rt_exec_state.bit.motionCancel);
       assert(sys_probe_position[0]==0);
     }
   }
 }
}
'''
with tempfile.TemporaryDirectory() as d:
    d=Path(d)
    (d/'stub.h').write_text(stub)
    (d/'Probe.cpp').write_text(source)
    (d/'test.cpp').write_text(test)
    for pin in (22,-1):
        subprocess.run(['g++','-std=c++17','-Wall','-Wextra','-Werror',
                        '-DCNC_FFST_BUILD',f'-DPROBE_PIN={pin}',
                        str(d/'Probe.cpp'),str(d/'test.cpp'),'-o',str(d/'test')],check=True)
        subprocess.run([str(d/'test')],check=True)
print('PASS: 8 input/polarity/direction cases, position capture, cancel flag, '
      'pull-up initialization and undefined-pin state. Host logic only.')
