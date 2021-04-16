import os
import json
import shelve
import random
import subprocess

def read_json():
	json_file = 'files/locked_folders.json'
	if os.path.exists(json_file):
		with open(json_file, 'r') as file:
			dct = json.load(file)
	else:
		dct = {}

	return dct

def write_to_json(data):
	json_file = 'files/locked_folders.json'
	with open(json_file, 'w') as file:
		json.dump(data, file)

def get_from_json(fname):
	dct = read_json()
	return dct.get(fname, None)

# Locker/Unlocker ----------------------------------------------------------------

def generate_key():
	string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	keygen = random.sample(string, 12)
	return ''.join(keygen)

def lock(fpath, password):
	key = generate_key()

	fname = os.path.basename(fpath)
	cwd = '/'.join(fpath.split('/')[:-1]) + '/'
	command1 = 'ren ' + fname + ' "Control Panel.{21EC2020-3AEA-1069-A2DD-' + key + '}"'
	command2 = 'attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-' + key + '}"'

	dct = read_json()

	if not fname in dct.keys():
		dct[fname] = [fpath, key]
		write_to_json(dct)

		with shelve.open('files/pwd') as pwd_manager:
			pwd_manager[fname] = password

			subprocess.call(command1, shell=True, cwd=cwd)
			subprocess.call(command2, shell=True, cwd=cwd)

			status = 'locked'	
	else:
		status = 'failed'

	return status


def unlock(fpath, password, key):
	fname = os.path.basename(fpath)
	cwd = '/'.join(fpath.split('/')[:-1]) + '/'
	command1 = 'attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-' + key + '}"'
	command2 = 'ren "Control Panel.{21EC2020-3AEA-1069-A2DD-' + key + '}" ' + fname

	with shelve.open('files/pwd') as pwd_manager:
		pass_ = pwd_manager[fname]

	if pass_ == password:
		dct = read_json()
		del dct[fname]
		write_to_json(dct)

		subprocess.call(command1, shell=True, cwd=cwd)
		subprocess.call(command2, shell=True, cwd=cwd)

		with shelve.open('files/pwd') as pwd_manager:
			del pwd_manager[fname]

		status = 'unlocked'
	else:
		status = 'failed'

	return status