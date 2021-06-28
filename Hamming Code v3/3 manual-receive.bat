@echo off
title RECEIVER
color 0a
REM Coded by Vinay K. Davda 7:56 PM 12/26/2019
SET /p rmsg=Enter Received MSG :

python py/receive.py %rmsg% > py/receive.txt

pause