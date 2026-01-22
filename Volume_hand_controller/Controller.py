""" I have used pycaw by Andre Miras at https://github.com/AndreMiras/pycaw 
    To control audio. It is an open-source module which can be installed by --> pip install pycaw  
"""
import math
import cv2
import time
import numpy as np
import HTrack as ht
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

height = 720 # height of webwindow
width = 1080 # width of webwindow
cap = cv2.VideoCapture(0) # using default system web cam 0
cap.set(3, width) # 3 is a index specifying width
cap.set(4, height) # 4 is a index specifying height
prevTime = 0
detector = ht.handDetector(detectionCon=0.7) # we need to detect hand more precisely
devices = AudioUtilities.GetSpeakers() # instantiating system speakers as objects
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None) # activating the interface to control volume
volume = interface.QueryInterface(IAudioEndpointVolume)
rangeVol=volume.GetVolumeRange() # volume range for my system is found to be -96 to 0
volLeast=rangeVol[0]
volHigh=rangeVol[1] 
vol=volLeast #initialising volume to least volume
volBar=400 #initialising volume bar
while True:
    success, img = cap.read() # reading the image
    img=detector.drawHands(img) # detecting the hands
    lmList=detector.getPositions(img) # finding landmarks of detected hands
    if len(lmList)!=0:
        # print(lmList[8],lmList[12])
        x1,y1=lmList[8][1],lmList[8][2]
        x2,y2=lmList[12][1],lmList[12][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv2.circle(img,(x1,y1),10,(170,153,255),cv2.FILLED) # drawing circle around index finger
        cv2.circle(img,(x2,y2),10,(170,153,255),cv2.FILLED) # drawing circle around middle finger
        cv2.circle(img,(cx,cy),10,(170,153,255),cv2.FILLED) # drawing circle around center point of both fingers
        cv2.line(img,(x1,y1),(x2,y2),(25,102,180),2)
        distance=math.dist([x1,y1],[x2,y2])
        # print(distance) # range of distance found to be 25 and 150
        vol=np.interp(distance,[25,150],[volLeast,volHigh]) # To interpolate distance between index and middle fingers to the volume of system
        volBar=np.interp(distance,[25,150],[400,100]) # To interpolate distance between index and middle fingers to the volume bar length
        volume.SetMasterVolumeLevel(vol, None)
        print(int(distance),vol)
        if distance<25:
            cv2.circle(img,(cx,cy),10,(0,0,120),cv2.FILLED) # indicating volume is 0 bby changing color of center circle
    #drawing volume bar
    cv2.rectangle(img,(80,100),(60,400),(230,153,0),2) # outer rectangle
    cv2.rectangle(img,(80,int(volBar)),(60,400),(150,153,0),cv2.FILLED) # actual volume 
    cv2.putText(img,"Volume",(40,420),cv2.FONT_HERSHEY_SIMPLEX,0.5,(149,100,149),2) 

    currTime = time.time()
    fps = 1/(currTime - prevTime) # using time to get timestamp of previous iteration and current iteration to know the frames per second
    prevTime = currTime
    cv2.putText(img, str(int(fps)), (30, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 3) # writing FPS on screen
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
