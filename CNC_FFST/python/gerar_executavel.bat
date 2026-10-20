@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
python -m pip install pyserial==3.5 pillow==11.3.0 pyinstaller==6.16.0
if errorlevel 1 exit /b 1
python -m PyInstaller --noconfirm --clean --onefile --windowed --name CNC_FFST_Controlador "CNC_FFST_Unico.py"
if errorlevel 1 exit /b 1
echo Executavel em dist\CNC_FFST_Controlador.exe
echo Chave compartilhada incluida no executavel via BIN correspondente.
pause
