@echo off
title HAMMING CODE AUTO SENDER
color 0a
REM Coded by Vinay K. Davda 7:56 PM 12/26/2019

SET /p smsg=Enter Send MSG :
echo %smsg% > py/binary.txt
python py/send.py %smsg% > send.txt

echo .
echo Done...!
echo .
echo .
echo Now check send.txt (in current directory... | it is encrypted...)
echo.
echo.
echo Created: py/binary.txt

pause