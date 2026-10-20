#pragma once
#ifdef CNC_FFST_AUTH
#include <stdint.h>
enum class Error : uint8_t;
bool ffst_auth_handle(char* line, uint8_t client, Error& result);
bool ffst_auth_trusted(uint8_t client);
bool ffst_auth_setting(const char* number, const char* value, uint8_t client);
bool ffst_auth_command(const char* number, uint8_t client);
bool ffst_auth_realtime(uint8_t command, uint8_t client);
void ffst_auth_reset();
void ffst_auth_init();
bool ffst_auth_rx(uint8_t data, uint8_t client);
#endif
