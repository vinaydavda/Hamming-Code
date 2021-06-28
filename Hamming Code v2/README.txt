This Program of Hamming Code made by Vinay K. Davda

-> The Full program is made in Python 3.
-> For making tasks easy batch files used.

Process : 
=========

[Here python 3.6.4 used in making this prg]

Step 1: Start
	-> In this step we have to choose size of binary we want to generate and send...
	-> Two files created...
	1] send.txt >>> Contains hamming code encoded binary...
	2] py/binary.txt >>> Contains random generated binary...

Step 2: Receive
	-> In this step we have to input the binary we received...reference file is send.txt...
	-> For checking Purpose we can change a bit in this step too...
	-> Receiver decodes the file and make py/receive ad decoded file...

Step 3: Check
	-> In this step the checking program automatically verify these files...
	1] py/binary.txt
	2] py/receive.txt
	-> If Sent and Received Data havn't any Error it will Display "No Error Found"
	-> In case of error it will display received string's error bit, error bit place, left two bits and right two bits...

Step 4: Reset
	-> The file reset.bat will remove all created files...


NOTE:
-----
-> In case of Custom inputs on each step use Hamming Code v1
-> joint.py file is for understand hamming code in one file

>>> Coded by Vinay K. Davda
10:17 PM 8/27/2018