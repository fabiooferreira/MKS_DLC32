#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
build_tools="${CNC_FFST_TOOLS_DIR:-/workspace/mks-environment}"
export PLATFORMIO_CORE_DIR="${PLATFORMIO_CORE_DIR:-$build_tools/platformio}"
bash "$project_dir/tools/build.sh"
python3 -m venv "$build_tools/image-venv"
PIP_CACHE_DIR="$build_tools/pip-cache" "$build_tools/image-venv/bin/python" -m pip install 'esptool==4.8.1'
framework="$PLATFORMIO_CORE_DIR/packages/framework-arduinoespressif32"
"$build_tools/image-venv/bin/python" -m esptool --chip esp32 merge_bin \
  --output "$project_dir/artifacts/CNC_FFST_0.3.0_FULL_4MB.bin" \
  --flash_mode dout --flash_freq 80m --flash_size 4MB --fill-flash-size 4MB \
  0x1000 "$framework/tools/sdk/bin/bootloader_dout_80m.bin" \
  0x8000 "$project_dir/Firmware/.pio/build/cnc_ffst_v2_1/partitions.bin" \
  0xe000 "$framework/tools/partitions/boot_app0.bin" \
  0x10000 "$project_dir/artifacts/firmware.bin"
python3 "$project_dir/tools/write_firmware_identity.py"
python3 "$project_dir/tools/bundle_python.py"
(cd "$project_dir/artifacts" && sha256sum CNC_FFST_0.3.0_FULL_4MB.bin > FULL_SHA256SUMS)
