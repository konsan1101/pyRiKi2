@ECHO OFF
REM ------------------------------------------------
REM COPYRIGHT (C) 2014-2022 Mitsuo KONDOU.
REM This software is released under the MIT License.
REM https://github.com/konsan1101
REM Thank you for keeping the rules.
REM ------------------------------------------------

REM CALL __setpath.bat

ECHO;
ECHO ----------
ECHO 2021/06/26
ECHO ----------
ECHO Python==3.9.5
ECHO setuptools==57.0.0
ECHO pyinstaller==4.3
ECHO numpy==1.21.0
ECHO psutil==5.8.0
ECHO websocket-client==0.48.0
ECHO matplotlib==3.2.2
ECHO mojimoji==0.0.11

ECHO;
ECHO ----------
ECHO 2022/01/26
ECHO ----------
ECHO Python==3.9.5
ECHO setuptools==57.0.0
ECHO pyinstaller==4.3
ECHO numpy==1.21.0
ECHO psutil==5.8.0
ECHO websocket-client==0.48.0
ECHO matplotlib==3.2.2
ECHO mojimoji==0.0.11
ECHO opencv-python==4.4.0.46
ECHO opencv-contrib-python==4.4.0.46

ECHO;
ECHO ----------
ECHO 2022/04/04
ECHO ----------
ECHO Python==3.9.10
ECHO setuptools==61.2.0
ECHO pyinstaller==4.10
ECHO numpy==1.22.3
ECHO psutil==5.9.0
ECHO websocket-client==1.1.0
ECHO matplotlib==3.5.1
ECHO pandas==1.4.1
ECHO mojimoji==0.0.12
ECHO opencv-python==4.4.0.46
ECHO opencv-contrib-python==4.4.0.46

ECHO;
ECHO -----
ECHO tools
ECHO -----
rem           pip  install --upgrade pip
    python -m pip  install --upgrade pip
    python -m pip  install --upgrade wheel
    python -m pip  install --upgrade setuptools
    python -m pip  install --upgrade pyinstaller

ECHO;
ECHO Waiting...10s
ping localhost -w 1000 -n 10 >nul

rem  --------
rem  PAUSE
rem  --------



ECHO;
ECHO -------
ECHO etc
ECHO -------
    python -m pip  install --upgrade pywin32
    python -m pip  install --upgrade pyautogui
    python -m pip  install --upgrade rainbow-logging-handler
    python -m pip  install --upgrade pysimplegui
    python -m pip  install --upgrade pysimpleguiqt
    python -m pip  install --upgrade psutil
    python -m pip  install --upgrade pycryptodome
    python -m pip  install --upgrade pykakasi
rem ↓ use vs code
    python -m pip  install --upgrade pylint

ECHO;
ECHO -------------
ECHO communication
ECHO -------------
    python -m pip  install --upgrade requests
    python -m pip  install --upgrade requests_toolbelt
    python -m pip  install --upgrade uuid
    python -m pip  install --upgrade bs4
    python -m pip  install --upgrade pyopenssl
    python -m pip  install --upgrade feedparser
    python -m pip  install --upgrade selenium
    python -m pip  install --upgrade flask
    python -m pip  install --upgrade flask-login

ECHO;
ECHO -----
ECHO audio
ECHO -----
    python -m pip  install --upgrade wave
    python -m pip  install --upgrade sounddevice
    python -m pip  install --upgrade speechrecognition

ECHO;
ECHO ------
ECHO vision
ECHO ------
    python -m pip  install --upgrade pillow
    python -m pip  install --upgrade numpy
    python -m pip  install --upgrade opencv-python
    python -m pip  install --upgrade opencv-contrib-python
    python -m pip  install --upgrade pyqt5
    python -m pip  install --upgrade pyzbar

ECHO;
ECHO ----------
ECHO IBM Watson
ECHO ----------
rem python -m pip  install --upgrade watson-developer-cloud==1.0.2
rem python -m pip  install --upgrade watson-developer-cloud
    python -m pip  install --upgrade ibm-watson
    python -m pip  install --upgrade ibm_cloud_sdk_core

rem ECHO;
rem ECHO -------------------------
rem ECHO IBM Watson,version update
rem ECHO -------------------------
rem python -m pip  uninstall -y  websocket-client
rem python -m pip  install       websocket-client==0.48.0

ECHO;
ECHO ---------------
ECHO microsoft,azure
ECHO ---------------
rem python -m pip  install --upgrade mstranslator
    python -m pip  install --upgrade cognitive_face
rem python -m pip  install --upgrade azure-storage
    python -m pip  install --upgrade azure-storage-blob==2.1.0

ECHO;
ECHO ---------------
ECHO amazon,AWS
ECHO ---------------
    python -m pip  install --upgrade boto3

ECHO;
ECHO --------
ECHO google
ECHO --------
    python -m pip  install --upgrade google-cloud-core
    python -m pip  install --upgrade google-cloud-speech
    python -m pip  install --upgrade google-cloud-translate
    python -m pip  install --upgrade google-cloud-vision
    python -m pip  install --upgrade google-api-python-client
    python -m pip  install --upgrade gtts
    python -m pip  install --upgrade googletrans
    python -m pip  install --upgrade goslate
    python -m pip  install --upgrade ggtrans
    python -m pip  uninstall -y gtts-token
    python -m pip  install --upgrade gtts-token



rem  --------
     PAUSE
rem  --------

rem ECHO;
rem ECHO ---------------------------
rem ECHO pyinstaller compile setting
rem rem  setuptools==49.6.0, 44.0.0
rem ECHO ---------------------------
rem rem  python -m pip  install --upgrade setuptools
rem rem  python -m pip  uninstall -y      setuptools
rem rem  python -m pip  install           setuptools==49.6.0
rem rem  python -m pip  install --upgrade pyinstaller
rem rem  python -m pip  uninstall -y      pyinstaller
rem rem  python -m pip  install           pyinstaller==3.6
rem rem  python -m pip  install --upgrade numpy
rem      python -m pip  uninstall -y      numpy
rem      python -m pip  install           numpy==1.19
rem rem  python -m pip  install --upgrade matplotlib==3.2.2
rem      python -m pip  uninstall -y      matplotlib
rem      python -m pip  install           matplotlib==3.2.2
rem rem  python -m pip  install --upgrade pandas
rem      python -m pip  uninstall -y      pandas
rem      python -m pip  install           pandas==1.3.5
rem rem  python -m pip  install --upgrade opencv-python
rem      python -m pip  uninstall -y      opencv-python
rem      python -m pip  install           opencv-python==4.4.0.46
rem rem  python -m pip  install --upgrade opencv-contrib-python
rem      python -m pip  uninstall -y      opencv-contrib-python
rem      python -m pip  install           opencv-contrib-python==4.4.0.46



ECHO;
ECHO -------------------
ECHO pip list --outdated
ECHO -------------------
    python -m pip  list --outdated

ECHO;
ECHO Waiting...5s
ping localhost -w 1000 -n 5 >nul

ECHO;
ECHO --------
ECHO pip list
ECHO --------
    python -m pip  list

rem  --------
     PAUSE
rem  --------
