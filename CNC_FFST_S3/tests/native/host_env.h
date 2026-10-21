#pragma once
#include "grbl/hal.h"
#include "grbl/protocol.h"
#include "grbl/system.h"
#include "grbl/state_machine.h"
#include <pthread.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <openssl/hmac.h>
#include <openssl/rand.h>
#define IRAM_ATTR
#define ESP_OK 0
#define MBEDTLS_MD_SHA256 1
#define pdTRUE 1
#define pdFALSE 0
#define portMUX_INITIALIZER_UNLOCKED 0
#define portENTER_CRITICAL(x) pthread_mutex_lock(&sim_auth_mux)
#define portEXIT_CRITICAL(x) pthread_mutex_unlock(&sim_auth_mux)
#define portENTER_CRITICAL_ISR(x) portENTER_CRITICAL(x)
#define portEXIT_CRITICAL_ISR(x) portEXIT_CRITICAL(x)
#define portYIELD_FROM_ISR() ((void)0)
typedef int portMUX_TYPE;
typedef int BaseType_t;
typedef void *TaskHandle_t;
typedef struct {size_t size;unsigned head,tail,count;pthread_mutex_t lock;unsigned char data[4][128];} *QueueHandle_t;
extern pthread_mutex_t sim_auth_mux;
static inline bool xPortInIsrContext(void){return false;}
static inline TaskHandle_t xTaskGetCurrentTaskHandle(void){return (void *)(uintptr_t)pthread_self();}
static inline QueueHandle_t xQueueCreate(unsigned count,unsigned size){QueueHandle_t q=calloc(1,sizeof(*q));q->size=size;pthread_mutex_init(&q->lock,NULL);return q;}
static inline int xQueueSend(QueueHandle_t q,const void*p,unsigned timeout){pthread_mutex_lock(&q->lock);int ok=q->count<4;if(ok){memcpy(q->data[q->head],p,q->size);q->head=(q->head+1)%4;q->count++;}pthread_mutex_unlock(&q->lock);return ok;}
static inline int xQueueSendFromISR(QueueHandle_t q,const void*p,int*wake){*wake=0;return xQueueSend(q,p,0);}
static inline int xQueueReceive(QueueHandle_t q,void*p,unsigned timeout){pthread_mutex_lock(&q->lock);int ok=q->count>0;if(ok){memcpy(p,q->data[q->tail],q->size);q->tail=(q->tail+1)%4;q->count--;}pthread_mutex_unlock(&q->lock);return ok;}
static const volatile unsigned char ffst_key_record[]="FFST_SHAREDKEY1:KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK:FFST_KEY_END";
typedef int esp_partition_t;
static inline const esp_partition_t *esp_ota_get_running_partition(void){static int p;return &p;}
static inline int esp_partition_get_sha256(const esp_partition_t*p,uint8_t*hash){memset(hash,0x11,32);return 0;}
static inline void esp_fill_random(void*dst,size_t size){if(RAND_bytes(dst,size)!=1)abort();}
static inline void bootloader_random_enable(void){}
static inline void bootloader_random_disable(void){}
static inline const void*mbedtls_md_info_from_type(int t){return (void*)1;}
static inline int mbedtls_md_hmac(const void*a,const unsigned char*k,size_t kl,const unsigned char*m,size_t ml,unsigned char*out){unsigned n;return HMAC(EVP_sha256(),k,kl,m,ml,out,&n)?0:-1;}
