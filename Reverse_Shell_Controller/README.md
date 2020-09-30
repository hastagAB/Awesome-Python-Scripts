# COMMAND AND CONTROL CENTER - REVERSE_SHELL AND HANDLER #

# 0) PLEASE READ FILES UNDER "USAGE GUIDE" !!!
# 1) server.py HANDLES THE CONTROLS OF THE PAYLOAD	-	MAIN CONTROL SCRIPT
# 2) CORRESPONDING reverse_shell.py SCRIPT		-	MAIN ATTACK SCRIPT (PAYLOAD)
# 3) DEPENDEDNT AND INCLUDED SCRIPTS - keyLogger.py ; soundRecorder.py ; camRecorder.py
# 4) All other requirements (to disguise the payload) are available in the Res folder

THIS SET OF SCRIPTS, THE HANDLER (handler) ALONG WITH ITS REVERSE_SHELL (AND OTHER DEPENDENT SCRIPTS)
ALLOWS REMOTE CONNECTIONS TO MULTIPLE TARGET MACHINES AND GAIN THEIR REMOTE ACCESS
BY MANAGING ALL THE CONNECTIONS THROUGH SESSIONS OR BY SENDING SOME COMMANDS TO ALL CONNECTED TARGETS AT ONCE
THE SET OF SCRIPTS TRIES TO CLOSELY IMITATE THE METASPLOT METERPRETER 

handler.py IS THE CONTROLLER (TO BE DEPLOYED ON THE ATTACKER MACHINE)
reverse_shell.py - "Online_Safety_Guide.png.exe" IS THE PAYLOAD (TO BE INJECTED INTO THE VICTIM AND NEEDS TO BE RUN BY THE USER)


================================================================================================================================================

# MANDATORY REQUIREMENTS:-

* python2.7
* wine

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
	> mss==4.0.2
	> PyAudio
	> wave
	> pynput
