@echo off
title RECEIVER
color 0a
REM Coded by Vinay K. Davda 10:16 PM 8/27/2018
SET /p rmsg=Enter Received MSG :

python py/receive.py %rmsg% > py/receive.txt

pause