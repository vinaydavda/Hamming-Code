@echo off
title HAMMING CODE
color 0a
REM Coded by Vinay K. Davda 7:56 PM 12/26/2019
SET /p size=Enter Size : 
python py/random_binary_generator.py %size% > py/binary.txt

SET /p smsg=<py/binary.txt
python py/send.py %smsg% > send.txt

echo .
echo Done...!
echo .
echo .
echo Now check send.txt
echo .
echo Created : /py/binary.txt

pause