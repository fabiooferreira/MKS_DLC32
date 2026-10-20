@echo off
setlocal
cd /d "%~dp0"
python -m pip install pyserial==3.5 pillow==11.3.0 pyinstaller==6.16.0
if errorlevel 1 exit /b 1
python -m PyInstaller --noconfirm --clean --onefile --windowed --name CNC_FFST_Controlador --add-data "firmware_identity.json;." --add-data "CNC_FFST_0.3.0_FULL_4MB.bin;." "Fabricação Laser Fresa.py"
if errorlevel 1 exit /b 1
echo Executavel em dist\CNC_FFST_Controlador.exe
echo Chave compartilhada incluida no executavel via BIN correspondente.
pause
