@ECHO OFF

IF EXIST "C:\snkApps\SAAP_r545\RiKi�A�g��SAAP���؋L�^�p2013R544_azip�ڑ�_PGWK.accdb"  GOTO BEGIN

ECHO;�@�@"C:\snkApps\SAAP_r545\RiKi�A�g��SAAP���؋L�^�p2013R544_azip�ڑ�_PGWK.accdb"
ECHO;�@�@Not Found !
GOTO ABORT

:BEGIN
CD "C:\snkApps\SAAP_r545"

rem ----------------------------------------------------------------------------------------
ECHO start /b "" "C:\snkApps\SAAP_r545\RiKi�A�g��SAAP���؋L�^�p2013R544_azip�ڑ�_PGWK.accdb"
     start /b "" "C:\snkApps\SAAP_r545\RiKi�A�g��SAAP���؋L�^�p2013R544_azip�ڑ�_PGWK.accdb"
rem ----------------------------------------------------------------------------------------

:ABORT
ping localhost -w 1000 -n 3 >nul
EXIT


