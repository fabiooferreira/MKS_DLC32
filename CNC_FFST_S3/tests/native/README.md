# Native core/auth review

Developer test only. This runs the project's real grblHAL parser, planner, stepper/state machine and ffst_auth.c in grblHAL/Simulator at commit 150e3f935e4b7cab7b90263b6b90b78912d9158d. The simulator pins Plugin_SD_card via its submodule (d0fe753d622e79a60e54e729ba83f7207276114c).

Requirements: Linux, GCC, CMake, make, OpenSSL development headers/libcrypto, Git/network and Python with pyserial and Pillow. The project core is copied from this repository; it is not replaced with upstream main. All setup changes are confined to a disposable simulator directory. No board, eFuses or production credential is used.

```
python CNC_FFST_S3/tools/build_native_review.py --workdir /tmp/ffst-native
python CNC_FFST_S3/tests/run_native_review.py --binary /tmp/ffst-native/simulator/build/grblHAL_sim
```

`host_env.h` adapts ESP random/hash/HMAC and RTOS primitives to OpenSSL/pthreads. It uses a public fixture key of 32 K bytes and a simulated hash of 32 0x11 bytes; these are intentionally unrelated to production. No ESP32 image or Secure Boot validation is implied. The ESP32 UART/USB ISR, actual flash writes, pinout, motor signals, limits wiring and emergency circuit still need hardware tests. The simulation's EEPROM is disposable, and its settings writes do not target real hardware.
