#include "Grbl.h"
#ifdef CNC_FFST_AUTH
#include "FFSTAuth.h"
#include "FFSTSharedKey.generated.h"
#include <mbedtls/md.h>
#include <esp_system.h>
#include <esp_ota_ops.h>
#include <esp_partition.h>
#include <freertos/semphr.h>
#include <ctype.h>

// Fixed shared credential requested by the owner; recoverable from the distributed image.
namespace {
uint8_t key[32];
bool loaded = false, paired = false;
char imageHash[65] = {};
bool getImageHash() {
    if(imageHash[0]) return true;
    uint8_t hash[32];
    auto partition=esp_ota_get_running_partition();
    if(!partition || esp_partition_get_sha256(partition,hash)!=ESP_OK) return false;
    const char* digits="0123456789abcdef";
    for(unsigned i=0;i<32;++i) { imageHash[2*i]=digits[hash[i]>>4];imageHash[2*i+1]=digits[hash[i]&15]; }
    imageHash[64]=0;return true;
}
struct Session { char nonce[65]; uint32_t seq, rtseq; bool authenticated; } sessions[CLIENT_COUNT] = {};
struct RTFrame { char text[96]; unsigned length; bool active, overflow; } frames[CLIENT_COUNT] = {};
SemaphoreHandle_t sessionMutex = nullptr;
struct Lock {
    bool held=true;
    Lock() { xSemaphoreTakeRecursive(sessionMutex,portMAX_DELAY); }
    void release() { if(held) { held=false; xSemaphoreGiveRecursive(sessionMutex); } }
    ~Lock() { release(); }
};
TaskHandle_t executingTask = nullptr;
uint8_t executingClient = CLIENT_ALL;
TaskHandle_t rtTask = nullptr;
uint8_t rtClient = CLIENT_ALL;
int unhex(char c) {
    if (c >= '0' && c <= '9') return c-'0';
    if (c >= 'a' && c <= 'f') return c-'a'+10;
    return -1;
}
bool decode(const char* text, uint8_t* dst, size_t n) {
    if (strlen(text) != n*2) return false;
    for (size_t i=0; i<n; ++i) {
        int a=unhex(text[2*i]), b=unhex(text[2*i+1]);
        if (a<0 || b<0) return false;
        dst[i]=(a<<4)|b;
    }
    return true;
}
void hex(const uint8_t* src, char* dst, size_t n) {
    const char* digits="0123456789abcdef";
    for(size_t i=0; i<n; ++i) { dst[2*i]=digits[src[i]>>4]; dst[2*i+1]=digits[src[i]&15]; }
    dst[2*n]=0;
}
bool digest(const char* message, uint8_t* out) {
    return mbedtls_md_hmac(mbedtls_md_info_from_type(MBEDTLS_MD_SHA256),key,32,
        reinterpret_cast<const unsigned char*>(message),strlen(message),out)==0;
}
bool valid(const char* message,const char* tag) {
    uint8_t expected[32], received[32];
    if (!decode(tag,received,32) || !digest(message,expected)) return false;
    unsigned diff=0;
    for(unsigned i=0;i<32;++i) diff|=expected[i]^received[i];
    return diff==0;
}
void load() {
    if(loaded) return;
    for(unsigned i=0;i<32;++i) key[i]=ffstSharedKeyRecord[sizeof("FFST_SHAREDKEY1:")-1+i];
    paired=true;loaded=true;
}
bool safeNumber(const char* n) {
    if(!n || !*n) return false;
    for(const char* p=n;*p;++p) if(!isdigit(*p)) return false;
    int i=atoi(n);
    return i==0||i==1||i==2||i==3||i==4||i==5||i==6||i==10||i==11||i==12||i==13||
           (i>=20&&i<=27)||i==30||i==31||i==32||i==38||i==40||
           (i>=100&&i<=105)||(i>=110&&i<=115)||(i>=120&&i<=125)||(i>=130&&i<=135);
}
}

bool ffst_auth_trusted(uint8_t client) {
    auto task=xTaskGetCurrentTaskHandle();
    return (executingTask && executingTask==task && executingClient==client) ||
           (rtTask && rtTask==task && rtClient==client);
}
void ffst_auth_init() { sessionMutex=xSemaphoreCreateRecursiveMutex(); }
void ffst_auth_reset() {
    Lock lock;
    memset(sessions,0,sizeof(sessions));
    memset(frames,0,sizeof(frames));
    // Keep the in-progress stack's ownership until it unwinds; no new packets are authorized.
}
bool ffst_auth_setting(const char* number,const char* value,uint8_t client) {
    if(ffst_auth_trusted(client) || !value) return true;
    return safeNumber(number) && (sys.state==State::Idle || sys.state==State::Alarm) &&
           gc_state.modal.spindle==SpindleState::Disable;
}
bool ffst_auth_command(const char* number,uint8_t client) {
    if(ffst_auth_trusted(client)) return true;
    // Explicit read-only commands, alarm acknowledgement and sleep; no aliases can bypass this.
    if(!number) return false;
    const char* allowed[]={"", "$", "+", "L", "S", "SC", "CMD", "A", "E", "G", "X", "V", "#", "I", "N", "T"};
    for(auto n:allowed) if(!strcmp(number,n)) return true;
    return false;
}
bool ffst_auth_realtime(uint8_t command,uint8_t client) {
    return ffst_auth_trusted(client) || command==uint8_t(Cmd::Reset) ||
        command==uint8_t(Cmd::StatusReport) || command==uint8_t(Cmd::FeedHold) ||
        command==uint8_t(Cmd::SafetyDoor) || command==uint8_t(Cmd::JogCancel);
}

bool ffst_auth_handle(char* line,uint8_t client,Error& result) {
    if(strncmp(line,"$FF",3)) return false;
    result=Error::AuthenticationFailed;
    if(client>=CLIENT_COUNT) return true;
    Lock lock;
    load();
    Session& s=sessions[client];
    if(!strcmp(line,"$FFINFO")) {
        if(!getImageHash()) return true;
        grbl_sendf(client,"[FFFW:CNC_FFST-0.3.0:%s]\r\n",imageHash);
        result=Error::Ok; return true;
    }
    // This edition has a fixed compiled key. USB/network cannot replace it.
    if(!strncmp(line,"$FFPAIR",7)) return true;
    if(!strcmp(line,"$FFHELLO")) {
        memset(&s,0,sizeof(s));
        if(!paired) { grbl_send(client,"[FFUNPAIRED]\r\n"); return true; }
        uint8_t random[32], tag[32];
        for(unsigned i=0;i<32;i+=4) { uint32_t r=esp_random(); memcpy(random+i,&r,4); }
        hex(random,s.nonce,32);
        if(!getImageHash()) return true;
        char message[160], taghex[65]; snprintf(message,sizeof(message),"server|%s|%s",s.nonce,imageHash);
        if(!digest(message,tag)) return true;
        hex(tag,taghex,32);
        grbl_sendf(client,"[FFNONCE:%s:%s]\r\n",s.nonce,taghex);
        result=Error::Ok; return true;
    }
    if(!paired || !s.nonce[0]) return true;
    if(!strncmp(line,"$FFAUTH=",8)) {
        if(s.authenticated) return true; // one proof per nonce: cannot rewind sequence/replay motion.
        if(!getImageHash()) return true;
        char message[160]; snprintf(message,sizeof(message),"client|%s|%s",s.nonce,imageHash);
        s.authenticated=valid(message,line+8); s.seq=0;
        if(s.authenticated) { grbl_send(client,"[FFAUTH:OK]\r\n"); result=Error::Ok; }
        return true;
    }
    if(strncmp(line,"$FFCMD=",7) || !s.authenticated || ffst_auth_trusted(client)) return true;
    char* sequence=line+7;
    char* tag=strchr(sequence,','); if(!tag) return true; *tag++=0;
    char* payload=strchr(tag,','); if(!payload) return true; *payload++=0;
    size_t nseq=strlen(sequence), nhex=strlen(payload);
    if(!nseq || nseq>10 || (nseq>1 && sequence[0]=='0') || !nhex || nhex>400 || nhex%2) return true;
    uint64_t number=0;
    for(const char* p=sequence;*p;++p) { if(!isdigit(*p)) return true; number=number*10+(*p-'0'); }
    if(number!=s.seq || number>=UINT32_MAX) return true;
    char message[490]; snprintf(message,sizeof(message),"%s|%s|%s",s.nonce,sequence,payload);
    if(!valid(message,tag)) return true;
    char decoded[201];
    if(!decode(payload,reinterpret_cast<uint8_t*>(decoded),nhex/2)) return true;
    decoded[nhex/2]=0;
    // Single printable ASCII command only. Hex envelope keeps raw realtime bytes out of the parser.
    for(size_t i=0;i<nhex/2;++i) if(decoded[i]<32 || decoded[i]>126) return true;
    if(sys.abort || sys_rt_exec_state.bit.reset) return true;
    ++s.seq;  // consume even if GRBL rejects the command; never replay motion.
    lock.release(); // Never hold the session mutex across a move/probe/homing wait.
    executingTask=xTaskGetCurrentTaskHandle(); executingClient=client;
    if(!strncmp(decoded,"RT:",3) && strlen(decoded)==5) {
        uint8_t cmd;
        if(decode(decoded+3,&cmd,1)) { execute_realtime_command(static_cast<Cmd>(cmd),client); result=Error::Ok; }
    } else if(strncmp(decoded,"$FF",3)) {
        result=execute_line(decoded,client,WebUI::AuthenticationLevel::LEVEL_GUEST);
    }
    executingTask=nullptr; executingClient=CLIENT_ALL;
    return true;
}

// Out-of-band authenticated resume/override frames are consumed by the input task,
// even while the main parser is waiting inside a held probe/homing cycle.
bool ffst_auth_rx(uint8_t data,uint8_t client) {
    if(client>=CLIENT_COUNT) return false;
    if(data==uint8_t(Cmd::Reset)||data==uint8_t(Cmd::FeedHold)||data==uint8_t(Cmd::StatusReport)||
       data==uint8_t(Cmd::SafetyDoor)||data==uint8_t(Cmd::JogCancel)) return false;
    Lock lock;
    RTFrame& frame=frames[client];
    if(data==0xf8) { frame.length=0;frame.active=true;frame.overflow=false;return true; }
    if(!frame.active) return false;
    if(data!='\n') {
        if(frame.length<sizeof(frame.text)-1 && data>=32 && data<=126) frame.text[frame.length++]=data;
        else frame.overflow=true;
        return true;
    }
    frame.active=false; frame.text[frame.length]=0;
    bool accepted=false;
    uint8_t command=0;
    if(!frame.overflow) {
        Session& s=sessions[client];
        char* seq=frame.text;
        char* tag=strchr(seq,',');
        char* cmd=tag?strchr(tag+1,','):nullptr;
        if(tag && cmd && s.authenticated) {
            *tag++=0;*cmd++=0;
            size_t len=strlen(seq);uint64_t number=0;bool digits=len>0&&len<=10;
            for(size_t i=0;i<len;++i) { if(!isdigit(seq[i]))digits=false;number=number*10+(seq[i]-'0'); }
            if(len>1&&seq[0]=='0')digits=false;
            char message[110];snprintf(message,sizeof(message),"%.64s|rt|%.10s|%.2s",s.nonce,seq,cmd);
            if(digits && number==s.rtseq && number<UINT32_MAX && decode(cmd,&command,1) &&
               (command=='~'||(command>=0x90&&command<=0x9e)||command==0xa0||command==0xa1) &&
               valid(message,tag) && !sys.abort && !sys_rt_exec_state.bit.reset) {
                ++s.rtseq;accepted=true;
            }
        }
    }
    lock.release();
    if(accepted) {
        rtTask=xTaskGetCurrentTaskHandle();rtClient=client;
        execute_realtime_command(static_cast<Cmd>(command),client);
        rtTask=nullptr;rtClient=CLIENT_ALL;
    }
    grbl_send(client,accepted?"[FFRT:OK]\r\n":"[FFRT:ERR]\r\n");
    return true;
}
#endif
