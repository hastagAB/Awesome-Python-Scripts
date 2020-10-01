# importing libraries 
import cv2 
import numpy as np 
import argparse

aq = argparse.ArgumentParser()

aq.add_argument('-i', '--input', required=True, help="input image path")

aq.add_argument('-o', '--output', help="path where you want to download the image")

args = vars(aq.parse_args())
# reading image  
img = cv2.imread(args['input']) 
   
# Edges 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.medianBlur(gray, 5) 
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  
                                         cv2.THRESH_BINARY, 9, 9) 
   
# Cartoonization 
color = cv2.bilateralFilter(img, 2, 250, 250) 
cartoon = cv2.bitwise_or(color, color, mask=edges) 
 
if(args['output']):
	cv2.imwrite(args['output'], cartoon)


cv2.imshow("Cartoon", cartoon) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 