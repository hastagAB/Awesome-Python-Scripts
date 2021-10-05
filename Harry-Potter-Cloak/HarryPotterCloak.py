import cv2
import numpy

def hello(x):
	print("")

if __name__=='__main__':
	cap = cv2.VideoCapture(0)
	bars = cv2.namedWindow("bars")

	cv2.createTrackbar("upper_hue","bars",110,180,hello)
	cv2.createTrackbar("upper_saturation","bars",255, 255, hello)
	cv2.createTrackbar("upper_value","bars",255, 255, hello)
	cv2.createTrackbar("lower_hue","bars",68,180, hello)
	cv2.createTrackbar("lower_saturation","bars",55, 255, hello)
	cv2.createTrackbar("lower_value","bars",54, 255, hello)

	#Capturing the initial frame for creation of background
	while(True):
		cv2.waitKey(1000)
		ret,init_frame = cap.read()
		if(ret):
			break

	while(True):
		ret,frame = cap.read()
		inspect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		#getting the HSV values for masking the cloak
		upper_hue = cv2.getTrackbarPos("upper_hue", "bars")
		upper_saturation = cv2.getTrackbarPos("upper_saturation", "bars")
		upper_value = cv2.getTrackbarPos("upper_value", "bars")
		lower_value = cv2.getTrackbarPos("lower_value","bars")
		lower_hue = cv2.getTrackbarPos("lower_hue","bars")
		lower_saturation = cv2.getTrackbarPos("lower_saturation","bars")

		#Kernel to be used for dilation
		kernel = numpy.ones((3,3),numpy.uint8)

		upper_hsv = numpy.array([upper_hue,upper_saturation,upper_value])
		lower_hsv = numpy.array([lower_hue,lower_saturation,lower_value])

		mask = cv2.inRange(inspect, lower_hsv, upper_hsv)
		mask = cv2.medianBlur(mask,3)
		mask_inv = 255-mask 
		mask = cv2.dilate(mask,kernel,5)
		
		#The mixing of frames in a combination to achieve the required frame
		b = frame[:,:,0]
		g = frame[:,:,1]
		r = frame[:,:,2]
		b = cv2.bitwise_and(mask_inv, b)
		g = cv2.bitwise_and(mask_inv, g)
		r = cv2.bitwise_and(mask_inv, r)
		frame_inv = cv2.merge((b,g,r))

		b = init_frame[:,:,0]
		g = init_frame[:,:,1]
		r = init_frame[:,:,2]
		b = cv2.bitwise_and(b,mask)
		g = cv2.bitwise_and(g,mask)
		r = cv2.bitwise_and(r,mask)
		blanket_area = cv2.merge((b,g,r))

		final = cv2.bitwise_or(frame_inv, blanket_area)

		cv2.imshow("Harry's Cloak",final)

		if(cv2.waitKey(3) == ord('q')):
			break;

	cv2.destroyAllWindows()
	cap.release()