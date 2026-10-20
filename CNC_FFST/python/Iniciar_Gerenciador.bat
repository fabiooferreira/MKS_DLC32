@echo off
chcp 65001 >nul
cd /d "%~dp0"
py -3.12 Gerenciador_ESP32_DLC32.py
if errorlevel 1 (
  echo.
  echo Confira se o Python 3.12 foi instalado com Tkinter e o launcher py.
  pause
)
