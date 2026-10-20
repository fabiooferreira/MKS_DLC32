/* CNC_FFST HMAC v1 adapter for grblHAL. GPL-3.0-or-later. */
#pragma once
#ifdef FFST_HOST_TEST
#include "host_env.h"
#else
#include "grbl/hal.h"
#endif
#define FFST_FIRMWARE_VERSION "CNC_FFST-S3-0.1.0"
void ffst_auth_init(void);
bool ffst_auth_trusted(void);
bool ffst_auth_system(char *line, status_code_t *result);
bool ffst_auth_rx(uint8_t c);
bool ffst_auth_realtime_allowed(uint8_t c);
void ffst_auth_poll(void);
void ffst_auth_reset(void);

status_code_t ffst_auth_input_system(char *line, stream_write_ptr write);
status_code_t ffst_auth_input_gcode(char *line);
