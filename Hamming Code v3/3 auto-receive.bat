@echo off
title HAMMING CODE AUTO RECEIVER
color 0a
REM Coded by Vinay K. Davda 7:56 PM 12/26/2019

REM -->It will automatically takes input from send.txt file and processes it to py/receive.py

SET /p rmsg=<send.txt

python py/receive.py %rmsg% > py/receive.txt

pause