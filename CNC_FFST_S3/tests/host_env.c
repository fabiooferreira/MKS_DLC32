#include "host_env.h"
#include "ffst_auth.h"
#include <openssl/hmac.h>
struct host_grbl grbl;
struct host_hal hal;
bool host_isr;
static char output[16384],last_command[256];
static unsigned executed,rt_executed,random_seed;
static int state;
static bool inject;
static int nested_status;
static void write_out(const char *s) {if(strlen(output)+strlen(s)<sizeof(output))strcat(output,s);}
const esp_partition_t *esp_ota_get_running_partition(void) {static int partition;return &partition;}
int esp_partition_get_sha256(const esp_partition_t *p,uint8_t *hash){memset(hash,0x11,32);return 0;}
void esp_fill_random(void *data,size_t size) {unsigned char *dst=data;for(size_t i=0;i<size;i++)dst[i]=++random_seed;}
int mbedtls_md_hmac(const void *a,const unsigned char *key,size_t kl,const unsigned char *msg,size_t ml,unsigned char *out){unsigned length;return HMAC(EVP_sha256(),key,kl,msg,ml,out,&length)?0:-1;}
sys_state_t state_get(void){return state;}
bool spindle_is_on(void){return false;}
status_code_t gc_execute_block(char *line){if(!ffst_auth_trusted())return Status_AccessDenied;if(inject){inject=false;char raw[]="$H";nested_status=ffst_auth_input_system(raw,write_out);}
executed++;strncpy(last_command,line,255);return Status_OK;}
status_code_t system_execute_line(char *line,void (*write)(const char *)){status_code_t result;if(ffst_auth_system(line,&result))return result;executed++;strncpy(last_command,line,255);return Status_OK;}
bool protocol_enqueue_realtime_command(uint8_t c){if(ffst_auth_rx(c)||!ffst_auth_realtime_allowed(c))return true;if(c=='~'||c==0x81||c>=0x90)rt_executed++;return true;}
void host_init(void){memset(&grbl,0,sizeof(grbl));memset(&hal,0,sizeof(hal));hal.stream.write=write_out;output[0]=last_command[0]=0;executed=rt_executed=0;host_isr=false;state=0;ffst_auth_init();ffst_auth_reset();}
void host_clear(void){output[0]=0;}
const char *host_output(void){return output;}
unsigned host_executed(void){return executed;}
unsigned host_rt_executed(void){return rt_executed;}
const char *host_last_command(void){return last_command;}
int host_line(const char *text){char line[800];snprintf(line,sizeof(line),"%s",text);return line[0]=='$'?system_execute_line(line,write_out):gc_execute_block(line);}
int host_rt_allowed(unsigned c){host_isr=true;bool allowed=ffst_auth_realtime_allowed(c);host_isr=false;return allowed;}
void host_frame(const unsigned char *data,unsigned n){for(unsigned i=0;i<n;i++){host_isr=true;protocol_enqueue_realtime_command(data[i]);host_isr=false;}ffst_auth_poll();}
void host_reset(void){host_isr=true;grbl.on_reset();host_isr=false;}
void host_state(int s){state=s;}

void host_inject_raw_during_command(void){inject=true;nested_status=-1;}
int host_nested_status(void){return nested_status;}
