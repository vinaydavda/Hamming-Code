This Program of Hamming Code made by Vinay K. Davda

-> The Full program is made in Python 3.
-> For making tasks easy batch files used.

FILE Description:
=================

py/binary.txt	=> Original Message
send.txt	=> Hamming Code Encrypted Message
py/receive.txt	=> Hamming Code Decrypted Message means Original Message Decrypted by py/receive.py


Process : 
=========

-> Please Do Process Step by step.
-> First send message part then receive message part will come and sequence should be followed.

>>>SEQUENCE:
------------
-> Step [1+2] or Step1,Step2
-> Step 3
-> Step 4
-> For any query or major bug or review submit me at vinaydavda2604@gmail.com

[Here python 3.6.4 used in making this prg]

<<<================SEND MESSAGE================>>>

[AUTO]
Step [1+2] : "[1+2] generate_and_autosend.bat"
	-> This file will generate Given Sized binary and sends it.
	-> It will create a py/binary.txt
	-> Then Encrypts it using py/send.py and makes send.txt

	----------------OR----------------

[MANUAL]
Step 1: "1 binary_generate.bat"
	-> In this step we have to choose size of binary we want to generate.
	-> py/binary.txt file generated and ready to be Encrypted and send.

[AUTO]
Step 2: "2 auto-send.bat"
	-> IMPORTANT: It requires py/binary.txt file.
	-> It will automatically take py/binary file as input and Encrypts it.
	-> Then it will Generates send.txt as Output which is Encryption of py/binary.txt

[MANUAL]
Step 2: "2 manual-send.bat"
	-> It will takes input and encrypts it using py/send.py
	-> Then it will Generates send.txt as Output
	-> Also it will generate py/binary.txt as original message which user has given.

<<<================RECEIVE MESSAGE================>>>

IMPORTANT: send.txt and py/binary.txt files should be there for further process...!

[AUTO]
Step 3: "3 auto-receive.bat"
	-> It will takes send.txt as input
	-> Processes on it using py/receive.py and generates file py/receive.txt as Decrypted Message.

[MANUAL]
Step 3: "3 manual-receive.bat"
	-> It will takes user input, you can refer send.txt file which have sent data.
	-> You can modify it for checking purpose.
	-> It will generate py/receive.txt as Decrypted Message.

<<<================CHECK RECEIVED MESSAGE WITH ORIGINAL MESSAGE================>>>

Step 4: Check
	-> In this step the checking program automatically verify these files...
	1] py/binary.txt (Original Sent msg)
	2] py/receive.txt (Decrypted msg)
	-> If Sent and Received Data havn't any Error it will Display "No Error Found"
	-> In case of error it will display received string's error bit, error bit place, left two bits and right two bits...

<<<================RESET WHOLE PROCESS================>>>

Step 4: Reset
	-> The file reset.bat will remove all created files.
	1] py/binary.txt
	2] send.txt
	3] py/receive.txt


NOTE:
-----
-> In case of Custom inputs(without cmd) on each step use Hamming Code v1
-> joint.py file is for understand hamming code in one file

>>> Coded by Vinay K. Davda
10:17 PM 8/27/2018
>>> All files updated at 7:55 PM 12/26/2019 by Vinay K. Davda