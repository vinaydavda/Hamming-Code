@echo off
color 0a
title CHECK
REM Coded by Vinay K. Davda 7:57 PM 12/26/2019
SET /p str1=<py/binary.txt
SET /p str2=<py/receive.txt

python py/checking.py %str1% %str2%

pause