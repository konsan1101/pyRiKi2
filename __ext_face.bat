@ECHO OFF
REM ------------------------------------------------
REM COPYRIGHT (C) 2014-2021 Mitsuo KONDOU.
REM This software is released under the MIT License.
REM https://github.com/konsan1101
REM Thank you for keeping the rules.
REM ------------------------------------------------

IF EXIST "C:\Python3"   GOTO PY
IF EXIST "C:\Python37"  GOTO PY
IF EXIST "C:\Python38"  GOTO PY
IF EXIST "C:\Python39"  GOTO PY

:DOS
ECHO;@%1@%2
GOTO ABORT

:PY
start /b python __ext_face.py %1 %2

:ABORT
rem ping localhost -w 1000 -n 3 >nul
EXIT
