================================================================================================================================================

# MANDATORY REQUIREMENTS:-

# python2.7
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

# ==============================================================================================================================================

# USAGE FOR THE PYTHON SCRIPTS DIRECTLY:-
----------------------------------------------------------------
# !!! READ THE "PS" PART OF THIS README POSITIVELY !!!
----------------------------------------------------------------

### FOR UPDATED AUTOMATIC USAGE, SEE README_AUTOMATIC.txt ###
________________________________________________________________
----------------------------------------------------------------


# TESTED ON KALI LINUX (FOR LINUX SYSTEMS) #
--------------------------------------------
# RUN THE COMMAND :-
# chmod +x handler.py
#
# THEN YOU CAN EXECUTE THE SCRIPT WITH -
# ./handler.py
# YOUR handler IS UP AND RUNNING
#
#
#
# TO RUN THE handler FROM A WINDOWS MACHINE #
--------------------------------------------
# RUN THE COMMAND :-
# python handler.py
# THIS SHOULD GET THE handler RUNNING
#
#
#
# TO RUN THE REVERSE_SHELL IN LINUX TARGET #
--------------------------------------------
# RUN COMMAND :-
# chmod +x reverse_shell.py
#
# EXECUTE WITH : ./reverse_shell.py 
# CONNECTION SHOULD BE ESTABLISHED
#
# FOR WINDOWS TARGET #
----------------------
# python reverse_shell.py
# CONNECTION SHOULD BE UP



================================================================================================================================================

# PS:-
#-----
# THE handler AS WELL AS THE REVERSE_SHELL SCRIPTS REQUIRE THE 
# IP ADDRESS AND PORT NUMBER OF THE LISTENING MACHINE
# THESE FIELDS MUST BE CHANGED ACCORDINGLY IN BOTH THE SCRIPTS
# BEFORE USE FOR CORRECT FUNCTIONING OF THE SCRIPTS
#
# HOW TO :-
#-----------
# IN handler.py :
#----------------
# GO TO THE BOTTOM OF THE SCRIPT, IN THE init_handler() FUNCTION
# LOOK FOR THE FOLLOWING FIELDS UNDER COMMENT "# details of the listening machine" - 
# attack_ip = "<SOME_IP_ADDRESS>"
# listen_port = <SOME_PORT_NUMBER>
# CHANGE THE VALUES WITHIN THE ANGLE BRACKETS 
#
# IN reverse_shell.py :
#----------------------
# GO TO THE BOTTOM OF THE CODE
# LOOK FOR THE FOLLOWING FIELDS UNDER "# details of the listening machine (connect to)" - 
# connect_ip = "<SOME_IP_ADDRESS>"
# conn_port = <SOME_PORT_NUMBER>
# CHANGE THE VALUES WITHIN THE ANGLE BRACKETS 

================================================================================================================================================

