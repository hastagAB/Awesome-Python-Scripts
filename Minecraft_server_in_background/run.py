#!/usr/bin/env python3

import subprocess
import time

filename_script = './start.sh'  # the script that will be executed
filename_script_output = './log.txt'
filename_own_input = 'command.txt'  # the file this script periodically reads from
stop_command = b'stop\n'  # must be a binary string
exit_keyword = 'stop'

with open(filename_own_input, 'w') as f:
	f.write('')  # reset content of file and create it if needed

fd_script_output = open(filename_script_output, 'w')  # create file descriptor for script to write its stdout to
script_process = subprocess.Popen(  # start new process running script
	filename_script,
	stdin=subprocess.PIPE,  # needed for script_process.communicate() (see below)
	stdout=fd_script_output  # redirect output
)

while True:
	with open(filename_own_input, 'r') as f:
		if exit_keyword in f.read():  # check if we should exit
			script_process.communicate(input=stop_command)  # stop subprocess and wait for it to terminate
			break
	time.sleep(1)

fd_script_output.close()
