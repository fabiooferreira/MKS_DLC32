/* CNC_FFST application access control, HMAC v1 compatible with existing client.
 * Per-command authorization; never globally unlock G-code after handshake.
 * ISR collects fixed-size realtime frames only. Crypto and replies run foreground.
 * This does not provide flash extraction protection. GPL-3.0-or-later.
 */
#include "ffst_auth.h"
#ifdef FFST_HOST_TEST
#include "host_env.h"
#else
#include "ffst_key.generated.h"
#endif
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#ifndef FFST_HOST_TEST
#include "esp_system.h"
#ifdef CNC_FFST_PROTECTED
#include "esp_flash_encrypt.h"
#include "esp_secure_boot.h"
#include "esp_efuse.h"
#include "esp_efuse_table.h"
#endif
#include "bootloader_random.h"
#include "esp_ota_ops.h"
#include "mbedtls/md.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"
#include "grbl/protocol.h"
#include "grbl/system.h"
#include "grbl/state_machine.h"
#endif

static uint8_t key[32];
static char image_hash[65], nonce[65];
static uint32_t sequence, rt_sequence;
static volatile bool authenticated;
static volatile uint32_t epoch;
static TaskHandle_t owner;
static unsigned trusted_depth, command_active;
static portMUX_TYPE mux = portMUX_INITIALIZER_UNLOCKED;
static QueueHandle_t rt_queue;
typedef struct { char text[96]; uint32_t epoch; } rt_packet_t;
static struct { char text[96]; unsigned length; bool active, overflow; } frame;
static on_reset_ptr old_reset;
static on_stream_changed_ptr old_stream;
static on_execute_realtime_ptr old_realtime, old_delay;

static int unhex(char c)
{
    return c >= '0' && c <= '9' ? c-'0' : (c >= 'a' && c <= 'f' ? c-'a'+10 : -1);
}
static void hex(const uint8_t *src, char *dst, size_t n)
{
    static const char digits[]="0123456789abcdef";
    for(size_t i=0;i<n;i++) { dst[i*2]=digits[src[i]>>4];dst[i*2+1]=digits[src[i]&15]; }
    dst[n*2]=0;
}
static bool decode(const char *src, uint8_t *dst, size_t n)
{
    if(strlen(src)!=2*n) return false;
    for(size_t i=0;i<n;i++) {
        int a=unhex(src[2*i]),b=unhex(src[2*i+1]);
        if(a<0||b<0) return false;
        dst[i]=(a<<4)|b;
    }
    return true;
}
static bool digest(const char *msg,uint8_t *dst)
{
    return mbedtls_md_hmac(mbedtls_md_info_from_type(MBEDTLS_MD_SHA256),key,32,
                           (const unsigned char *)msg,strlen(msg),dst)==0;
}
static bool valid(const char *msg,const char *tag)
{
    uint8_t expected[32],received[32];unsigned diff=0;
    if(!decode(tag,received,32)||!digest(msg,expected)) return false;
    for(unsigned i=0;i<32;i++) diff|=expected[i]^received[i];
    return diff==0;
}
static bool get_hash(void)
{
    if(image_hash[0]) return true;
    uint8_t hash[32];
    const esp_partition_t *part=esp_ota_get_running_partition();
    if(!part||esp_partition_get_sha256(part,hash)!=ESP_OK) return false;
    hex(hash,image_hash,32);return true;
}
static bool number(const char *text,uint32_t *value)
{
    size_t n=strlen(text);uint64_t v=0;
    if(!n||n>10||(n>1&&text[0]=='0')) return false;
    for(size_t i=0;i<n;i++) { if(text[i]<'0'||text[i]>'9') return false;v=v*10+text[i]-'0'; }
    if(v>=UINT32_MAX) return false;
    *value=(uint32_t)v;return true;
}
bool IRAM_ATTR ffst_auth_trusted(void)
{
    return !xPortInIsrContext() && owner && owner==xTaskGetCurrentTaskHandle() && trusted_depth;
}
void IRAM_ATTR ffst_auth_reset(void)
{
    if(xPortInIsrContext()) portENTER_CRITICAL_ISR(&mux); else portENTER_CRITICAL(&mux);
    authenticated=false;nonce[0]=0;epoch++;frame.active=false;
    if(xPortInIsrContext()) portEXIT_CRITICAL_ISR(&mux); else portEXIT_CRITICAL(&mux);
}
static void IRAM_ATTR on_reset(void) { ffst_auth_reset();if(old_reset) old_reset(); }
static void on_stream(void) { ffst_auth_reset();if(old_stream) old_stream(); }
static bool signed_rt(uint8_t c)
{
    return c==CMD_CYCLE_START_LEGACY||c==CMD_CYCLE_START||(c>=0x90&&c<=0x9e)||c==0xa0||c==0xa1;
}
bool IRAM_ATTR ffst_auth_realtime_allowed(uint8_t c)
{
    if(ffst_auth_trusted()) return true;
    if(c==0x18) { ffst_auth_reset();return true; }
    // Status, stop/hold/door/jog-cancel remain public; start and tool toggles do not.
    if(c=='?'||c=='!'||c==CMD_SAFETY_DOOR||c==CMD_JOG_CANCEL||c==CMD_STOP||
       c==CMD_STATUS_REPORT_ALL||c==CMD_STATUS_REPORT||c==CMD_FEED_HOLD) return true;
    return c>=32 && c<127 && c!='~';
}
bool IRAM_ATTR ffst_auth_rx(uint8_t c)
{
    if(ffst_auth_trusted()) return false;
    if(c==CMD_RESET||c=='?'||c=='!'||c==CMD_SAFETY_DOOR||c==CMD_JOG_CANCEL||
       c==CMD_STOP||c==CMD_STATUS_REPORT||c==CMD_STATUS_REPORT_ALL||c==CMD_FEED_HOLD) return false;
    bool isr=xPortInIsrContext(), consumed=false, ready=false;
    rt_packet_t packet;
    if(isr) portENTER_CRITICAL_ISR(&mux); else portENTER_CRITICAL(&mux);
    if(c==0xf8) {
        frame.length=0;frame.active=true;frame.overflow=false;consumed=true;
    } else if(frame.active) {
        consumed=true;
        if(c=='\n') {
            frame.active=false;
            if(!frame.overflow) {
                memcpy(packet.text,frame.text,frame.length);packet.text[frame.length]=0;
                packet.epoch=epoch;ready=true;
            }
        } else if(c>=32 && c<=126 && frame.length<sizeof(frame.text)-1)
            frame.text[frame.length++]=c;
        else frame.overflow=true;
    }
    if(isr) portEXIT_CRITICAL_ISR(&mux); else portEXIT_CRITICAL(&mux);
    if(ready && rt_queue) {
        if(isr) { BaseType_t wake=pdFALSE;xQueueSendFromISR(rt_queue,&packet,&wake);if(wake) portYIELD_FROM_ISR(); }
        else xQueueSend(rt_queue,&packet,0);
    }
    return consumed;
}
void ffst_auth_poll(void)
{
    if(!rt_queue) return;
    rt_packet_t packet;
    while(xQueueReceive(rt_queue,&packet,0)==pdTRUE) {
        bool accepted=false;
        char *seq=packet.text,*tag=strchr(seq,','),*cmd=tag?strchr(tag+1,','):NULL;
        uint32_t value;uint8_t c;
        if(tag && cmd && authenticated && packet.epoch==epoch) {
            *tag++=0;*cmd++=0;
            char message[112];snprintf(message,sizeof(message),"%.64s|rt|%.10s|%.2s",nonce,seq,cmd);
            if(number(seq,&value)&&value==rt_sequence&&decode(cmd,&c,1)&&signed_rt(c)&&valid(message,tag)) {
                uint32_t checked=epoch;
                portENTER_CRITICAL(&mux);
                if(authenticated&&checked==epoch&&packet.epoch==epoch) {rt_sequence++;accepted=true;}
                portEXIT_CRITICAL(&mux);
                if(accepted) {
                    TaskHandle_t previous=owner;unsigned depth=trusted_depth;
                    owner=xTaskGetCurrentTaskHandle();trusted_depth++;
                    protocol_enqueue_realtime_command(c);
                    owner=previous;trusted_depth=depth;
                }
            }
        }
        hal.stream.write(accepted?"[FFRT:OK]\r\n":"[FFRT:ERR]\r\n");
    }
}
static void realtime(sys_state_t state) {ffst_auth_poll();if(old_realtime) old_realtime(state);}
static void delay(sys_state_t state) {ffst_auth_poll();if(old_delay) old_delay(state);}
static bool safe_setting(const char *line)
{
    const char *equal=strchr(line,'=');
    if(!equal) return false;
    char text[12];size_t n=equal-line-1;
    if(!n||n>=sizeof(text)) return false;
    memcpy(text,line+1,n);text[n]=0;uint32_t v;
    if(!number(text,&v)) return false;
    return v<=6|| (v>=10&&v<=13)||(v>=20&&v<=27)||(v>=30&&v<=32)||
           (v>=100&&v<=105)||(v>=110&&v<=115)||(v>=120&&v<=125)||(v>=130&&v<=135);
}
bool ffst_auth_system(char *line,status_code_t *result)
{
    if(strncmp(line,"$FF",3)) {
        if(ffst_auth_trusted()) return false;
        const char *allow[]={"$","$$","$+","$G","$#","$I","$N","$X","$HELP","$PINS","$SETTINGS","$ALARMS","$ERRORS","$COMMANDS"};
        for(unsigned i=0;i<sizeof(allow)/sizeof(*allow);i++) if(!strcmp(line,allow[i])) return false;
        if(safe_setting(line) && (state_get()==STATE_IDLE || state_get()==STATE_ALARM) && !spindle_is_on()) return false;
        *result=Status_AccessDenied;return true;
    }
    *result=Status_AccessDenied;
#if defined(CNC_FFST_PROTECTED) && !defined(FFST_HOST_TEST)
    if(!strncmp(line,"$FFSEC=",7)) {
        uint8_t challenge[16],tag[32],mac[6];
        if(!decode(line+7,challenge,sizeof(challenge)) || !get_hash()) return true;
        bool key1=false,key2=false;
        for(int block=EFUSE_BLK_KEY0;block<=EFUSE_BLK_KEY5;block++) {
            esp_efuse_purpose_t purpose=esp_efuse_get_key_purpose((esp_efuse_block_t)block);
            bool locked=esp_efuse_get_key_dis_read((esp_efuse_block_t)block) &&
                        esp_efuse_get_key_dis_write((esp_efuse_block_t)block);
            if(purpose==ESP_EFUSE_KEY_PURPOSE_XTS_AES_256_KEY_1) key1=locked;
            if(purpose==ESP_EFUSE_KEY_PURPOSE_XTS_AES_256_KEY_2) key2=locked;
        }
        esp_efuse_mac_get_default(mac);
        char payload[400],message[420],encoded[800],taghex[65];
        snprintf(payload,sizeof(payload),
            "{\"nonce\":\"%s\",\"mac\":\"%02x%02x%02x%02x%02x%02x\",\"appsha\":\"%s\","
            "\"encryption_release\":%d,\"secure_boot\":%d,\"secure_download\":%d,"
            "\"jtag_disabled\":%d,\"keys_read_protected\":%d,\"maintenance_safe\":%d}",
            line+7,mac[0],mac[1],mac[2],mac[3],mac[4],mac[5],image_hash,
            esp_get_flash_encryption_mode()==ESP_FLASH_ENC_MODE_RELEASE,
            esp_secure_boot_enabled(),esp_efuse_read_field_bit(ESP_EFUSE_ENABLE_SECURITY_DOWNLOAD),
            esp_efuse_read_field_bit(ESP_EFUSE_HARD_DIS_JTAG) && esp_efuse_read_field_bit(ESP_EFUSE_DIS_USB_JTAG),
            key1&&key2, !spindle_is_on() && (state_get()==STATE_IDLE || state_get()==STATE_ALARM || state_get()==STATE_ESTOP));
        snprintf(message,sizeof(message),"security|%s",payload);
        if(!digest(message,tag)) return true;
        hex((uint8_t *)payload,encoded,strlen(payload));hex(tag,taghex,32);
        hal.stream.write("[FFSEC:");hal.stream.write(encoded);hal.stream.write(":");hal.stream.write(taghex);hal.stream.write("]\r\n");
        *result=Status_OK;return true;
    }
#endif
    if(!strcmp(line,"$FFINFO")) {
        if(!get_hash()) return true;
        hal.stream.write("[FFFW:" FFST_FIRMWARE_VERSION ":");hal.stream.write(image_hash);hal.stream.write("]\r\n");
        *result=Status_OK;return true;
    }
    if(!strcmp(line,"$FFHELLO")) {
        ffst_auth_reset();sequence=rt_sequence=0;
        uint8_t random[32],tag[32];char msg[160],taghex[65];
        /* Radio/ADC are unused on this USB-only profile: provide fresh HWRNG entropy. */
        bootloader_random_enable();esp_fill_random(random,sizeof(random));bootloader_random_disable();
        hex(random,nonce,32);
        if(!get_hash()) return true;
        snprintf(msg,sizeof(msg),"server|%s|%s",nonce,image_hash);
        if(!digest(msg,tag)) return true;
        hex(tag,taghex,32);
        hal.stream.write("[FFNONCE:");hal.stream.write(nonce);hal.stream.write(":");hal.stream.write(taghex);hal.stream.write("]\r\n");
        *result=Status_OK;return true;
    }
    if(!nonce[0]) return true;
    if(!strncmp(line,"$FFAUTH=",8)) {
        if(authenticated||!get_hash()) return true;
        uint32_t checked=epoch;bool accepted=false;
        char msg[160];snprintf(msg,sizeof(msg),"client|%s|%s",nonce,image_hash);
        if(valid(msg,line+8)) {
            portENTER_CRITICAL(&mux);
            if(checked==epoch&&nonce[0]) {authenticated=true;sequence=rt_sequence=0;accepted=true;}
            portEXIT_CRITICAL(&mux);
        }
        if(accepted) {hal.stream.write("[FFAUTH:OK]\r\n");*result=Status_OK;}
        return true;
    }
    if(strncmp(line,"$FFCMD=",7)||!authenticated||ffst_auth_trusted()||command_active) return true;
    uint32_t checked=epoch,value;
    char *seq=line+7,*tag=strchr(seq,','),*payload=tag?strchr(tag+1,','):NULL;
    if(!tag||!payload) return true;
    *tag++=0;*payload++=0;
    size_t length=strlen(payload);
    if(!number(seq,&value)||value!=sequence||!length||length>400||length%2) return true;
    char msg[490];snprintf(msg,sizeof(msg),"%s|%s|%s",nonce,seq,payload);
    if(!valid(msg,tag)) return true;
    char decoded[201];
    if(!decode(payload,(uint8_t *)decoded,length/2)) return true;
    decoded[length/2]=0;
    for(size_t i=0;i<length/2;i++) if(decoded[i]<32||decoded[i]>126) return true;
    if(!strncmp(decoded,"$FF",3)) return true;
    bool accepted=false;
    portENTER_CRITICAL(&mux);
    if(authenticated && checked==epoch) {sequence++;accepted=true;}
    portEXIT_CRITICAL(&mux);
    if(!accepted) return true;
    owner=xTaskGetCurrentTaskHandle();trusted_depth++;command_active++;
    if(!strncmp(decoded,"RT:",3)&&strlen(decoded)==5) {
        uint8_t c;
        if(decode(decoded+3,&c,1)&&signed_rt(c)) {protocol_enqueue_realtime_command(c);*result=Status_OK;}
    } else if(decoded[0]=='$') *result=system_execute_line(decoded,hal.stream.write);
    else if(state_get()&(STATE_ALARM|STATE_ESTOP|STATE_JOG)) *result=Status_SystemGClock;
    else *result=gc_execute_block(decoded);
    command_active--;trusted_depth--;if(!trusted_depth) owner=NULL;
    return true;
}
/* Raw parser callbacks must not inherit a long-running signed command's scope.
 * protocol_poll_cmd() can run recursively during probe/homing/hold waits. */
status_code_t ffst_auth_input_system(char *line, stream_write_ptr write)
{
    TaskHandle_t previous=owner;unsigned depth=trusted_depth;
    owner=NULL;trusted_depth=0;
    status_code_t result=system_execute_line(line,write);
    owner=previous;trusted_depth=depth;return result;
}
status_code_t ffst_auth_input_gcode(char *line)
{
    TaskHandle_t previous=owner;unsigned depth=trusted_depth;
    owner=NULL;trusted_depth=0;
    status_code_t result=gc_execute_block(line);
    owner=previous;trusted_depth=depth;return result;
}
void ffst_auth_init(void)
{
    for(unsigned i=0;i<32;i++)key[i]=ffst_key_record[sizeof("FFST_SHAREDKEY1:")-1+i];
    rt_queue=xQueueCreate(4,sizeof(rt_packet_t));
    // Fail closed if no queue: line authentication works; realtime frames are discarded.
    old_reset=grbl.on_reset;grbl.on_reset=on_reset;
    old_stream=grbl.on_stream_changed;grbl.on_stream_changed=on_stream;
    old_realtime=grbl.on_execute_realtime;grbl.on_execute_realtime=realtime;
    old_delay=grbl.on_execute_delay;grbl.on_execute_delay=delay;
}
void my_plugin_init(void) {ffst_auth_init();}
