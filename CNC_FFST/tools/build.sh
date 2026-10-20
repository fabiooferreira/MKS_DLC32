#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
build_tools="${CNC_FFST_TOOLS_DIR:-/workspace/mks-environment}"
export PLATFORMIO_CORE_DIR="${PLATFORMIO_CORE_DIR:-$build_tools/platformio}"
export PIP_CACHE_DIR="$build_tools/pip-cache"
mkdir -p "$build_tools" "$project_dir/artifacts"
python3 "$project_dir/tools/prepare_shared_key.py"
if [ ! -x "$build_tools/venv/bin/python" ]; then
  python3 -m venv "$build_tools/venv"
fi
"$build_tools/venv/bin/python" -m pip install -r "$project_dir/tools/requirements-build.txt"
"$build_tools/venv/bin/pio" run -d "$project_dir/Firmware" -e cnc_ffst_v2_1 -j "${CNC_FFST_JOBS:-2}" 2>&1 | tee "$project_dir/artifacts/build.log"
cp "$project_dir/Firmware/.pio/build/cnc_ffst_v2_1/firmware.bin" "$project_dir/artifacts/firmware.bin"
cp "$project_dir/Firmware/.pio/build/cnc_ffst_v2_1/firmware.elf" "$project_dir/artifacts/firmware.elf"
"$build_tools/venv/bin/pio" pkg list -d "$project_dir/Firmware" -e cnc_ffst_v2_1 > "$project_dir/artifacts/packages.txt"
(cd "$project_dir/artifacts" && sha256sum firmware.bin firmware.elf > SHA256SUMS)
