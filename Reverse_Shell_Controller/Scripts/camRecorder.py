#!/usr/bin/python

import cv2
import os


def captureVideo(stop_thread):
	
	#Capture video from webcam
	vid_capture = cv2.VideoCapture(0)
	vid_cod = cv2.VideoWriter_fourcc(*'XVID')

	try:
		vid_path = os.environ["appdata"] + "\\Vid.mp4"
	except:
		vid_path = os.environ["HOME"] + "/Vid.mp4"


	output = cv2.VideoWriter(vid_path, vid_cod, 20.0, (640,480))
	while not stop_thread.is_set():
		# Capture each frame of webcam video
		ret,frame = vid_capture.read()
#		cv2.imshow("My cam video", frame)
		output.write(frame)
		
	# close the already opened camera
	vid_capture.release()
	# close the already opened file
	output.release()
	# close the window and de-allocate any associated memory usage
	cv2.destroyAllWindows()
	

def imgCapture():
	
	try:
		img_path = os.environ["appdata"] + "\\Image.png"
	except:
		img_path = os.environ["HOME"] + "/Image.png"
	
	img_capture = cv2.VideoCapture(0)	
	ret, frame = img_capture.read()
	
	cv2.imwrite(img_path, frame)
	
	img_capture.release()

