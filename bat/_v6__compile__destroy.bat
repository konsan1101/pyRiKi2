@ECHO OFF
REM ------------------------------------------------
REM COPYRIGHT (C) 2014-2021 Mitsuo KONDOU.
REM This software is released under the MIT License.
REM https://github.com/konsan1101
REM Thank you for keeping the rules.
REM ------------------------------------------------

cd ".."

ECHO;
IF EXIST "build" RD "build" /s /q
IF EXIST "dist"  RD "dist"  /s /q
PAUSE



ECHO;
ECHO ---------------------------
ECHO pyinstaller compile setting
ECHO ---------------------------
rem rem  python -m pip  install --upgrade setuptools
rem rem  python -m pip  uninstall -y      setuptools
rem rem  python -m pip  install           setuptools==56.0.0
rem rem  python -m pip  install --upgrade pyinstaller
rem rem  python -m pip  uninstall -y      pyinstaller
rem rem  python -m pip  install           pyinstaller==4.3
rem rem  python -m pip  install --upgrade numpy
rem      python -m pip  uninstall -y      numpy
rem      python -m pip  install           numpy==1.20.2
rem rem  python -m pip  install --upgrade matplotlib
         python -m pip  uninstall -y      matplotlib
         python -m pip  install           matplotlib==3.2.2
ECHO;



set pyname=_v6__destroy
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR --icon="_icons/RiKi_stop.ico"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_assistant\%pyname%.exe"
    copy "%pyname%.exe"        "C:\RiKi_speech\%pyname%.exe"
    copy "%pyname%.exe"        "C:\RiKi_camera\%pyname%.exe"
    copy "%pyname%.exe"        "C:\RiKi_recorder\%pyname%.exe"
    del  "%pyname%.exe"

ECHO;
IF EXIST "build" RD "build" /s /q
IF EXIST "dist"  RD "dist"  /s /q
PAUSE



