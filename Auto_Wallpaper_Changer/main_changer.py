import os
import requests
import wget
import subprocess
import time

def get_wallpaper():
	url = 'https://api.unsplash.com/photos/random?client_id=ZQfcb7DPk5z8ZH5W7Zaij6xG33M9U9BJ8ddfYifV6_E'
	params = {
		'query': 'HD wallpapers',
		'orientation': 'landscape'
	}

	response = requests.get(url, params=params).json()
	image_source = response['urls']['full']

	image = wget.download(image_source, 'D:\\Abdul Rehman\\AI Automations\\Unsplash_Images_API\\Images')
	return image

def change_wallpaper():
	wallpaper = get_wallpaper()
	cmd = """/usr/bin/osascript<<END
	tell application "Finder"
	set desktop picture to POSIX file "%s"
	end tell
	END"""

	subprocess.Popen(cmd%wallpaper, shell=True)
	subprocess.call(["killall Dock"], shell=True)

def main():
	try:
		while True:
			change_wallpaper()
			time.sleep(10)

	except KeyboardInterrupt:
		print("\nHope you like this one! Quitting.")
	except Exception as e:
		pass
	

if __name__ == "__main__":
	main()