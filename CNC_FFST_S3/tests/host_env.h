#pragma once
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#define IRAM_ATTR
#define CMD_RESET 0x18
#define CMD_STOP 0x19
#define CMD_CYCLE_START_LEGACY '~'
#define CMD_CYCLE_START 0x81
#define CMD_FEED_HOLD 0x82
#define CMD_SAFETY_DOOR 0x84
#define CMD_JOG_CANCEL 0x85
#define CMD_STATUS_REPORT 0x80
#define CMD_STATUS_REPORT_ALL 0x87
#define STATE_IDLE 0
#define STATE_ALARM 1
#define STATE_ESTOP 2
#define STATE_JOG 4
#define Status_OK 0
#define Status_AccessDenied 78
#define Status_SystemGClock 9
#define ESP_OK 0
#define MBEDTLS_MD_SHA256 1
#define pdTRUE 1
#define pdFALSE 0
#define portMUX_INITIALIZER_UNLOCKED 0
#define portENTER_CRITICAL(x) ((void)(x))
#define portEXIT_CRITICAL(x) ((void)(x))
#define portENTER_CRITICAL_ISR(x) ((void)(x))
#define portEXIT_CRITICAL_ISR(x) ((void)(x))
#define portYIELD_FROM_ISR() ((void)0)
typedef int status_code_t;
typedef void (*stream_write_ptr)(const char *);
typedef int sys_state_t;
typedef int portMUX_TYPE;
typedef int BaseType_t;
typedef void *TaskHandle_t;
typedef struct { size_t size;unsigned head,tail,count;unsigned char data[4][128]; } host_queue_t;
typedef host_queue_t *QueueHandle_t;
typedef void (*on_reset_ptr)(void);
typedef void (*on_stream_changed_ptr)(void);
typedef void (*on_execute_realtime_ptr)(sys_state_t state);
extern struct host_grbl {on_reset_ptr on_reset;on_stream_changed_ptr on_stream_changed;on_execute_realtime_ptr on_execute_realtime,on_execute_delay;} grbl;
extern struct host_hal {struct {void (*write)(const char *);} stream;} hal;
extern bool host_isr;
static inline bool xPortInIsrContext(void) { return host_isr; }
static inline TaskHandle_t xTaskGetCurrentTaskHandle(void) {return (void *)1;}
static inline QueueHandle_t xQueueCreate(unsigned count,unsigned size) {host_queue_t *q=calloc(1,sizeof(*q));q->size=size;return q;}
static inline int xQueueSend(QueueHandle_t q,const void *p,unsigned delay) {if(q->count==4)return 0;memcpy(q->data[q->head],p,q->size);q->head=(q->head+1)%4;q->count++;return 1;}
static inline int xQueueSendFromISR(QueueHandle_t q,const void *p,int *wake){*wake=0;return xQueueSend(q,p,0);}
static inline int xQueueReceive(QueueHandle_t q,void *p,unsigned delay){if(!q->count)return 0;memcpy(p,q->data[q->tail],q->size);q->tail=(q->tail+1)%4;q->count--;return 1;}
static const volatile unsigned char ffst_key_record[]="FFST_SHAREDKEY1:KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK:FFST_KEY_END";
typedef int esp_partition_t;
const esp_partition_t *esp_ota_get_running_partition(void);
int esp_partition_get_sha256(const esp_partition_t *,uint8_t *hash);
void esp_fill_random(void *data,size_t size);
static inline void bootloader_random_enable(void) {}
static inline void bootloader_random_disable(void) {}
static inline const void *mbedtls_md_info_from_type(int type) {return (void *)1;}
int mbedtls_md_hmac(const void *,const unsigned char *,size_t,const unsigned char *,size_t,unsigned char *);
sys_state_t state_get(void);
bool spindle_is_on(void);
status_code_t gc_execute_block(char *);
status_code_t system_execute_line(char *,void (*write)(const char *));
bool protocol_enqueue_realtime_command(uint8_t c);
