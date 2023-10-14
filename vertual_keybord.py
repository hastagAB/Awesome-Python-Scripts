import cv2 as cv 
import numpy as np 
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import time 
from timeit import default_timer as timer



cap=cv.VideoCapture(0)

detector_c=HandDetector(cap)


class handDetector():
    def __init__(self, mode=False, maxHands=1,modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        #self.mpHands.Hands(self.mode, self.maxHands,
                                        #self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                #if draw:
                    #cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList


class button():
    def __init__(self,pos,text,size=[75,75]):

        self.pos=pos
        self.size=size 
        self.text=text 

        
def draw(img,button_list,color=(255,0,255),alpha=0.50):
    try:
        for button in button_list:
            x,y=button.pos 
            h,w=button.size
            cv.rectangle(img,(x,y),(x+h,y+w),color,cv.FILLED)
            cv.putText(img,str(button.text),(x+19,y+55),cv.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,255),2,cv.LINE_4)
            

        return img
    except:
        x,y=button_list.pos 
        h,w=button_list.size
        cv.rectangle(img,(x,y),(x+h,y+w),color,cv.FILLED)
        cv.putText(img,str(button_list.text),(x+19,y+55),cv.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,255),2,cv.LINE_4)
        
        return img

def dist(lmlist,p1,p2,img):
    x_d=lmlist[p1][1]-lmlist[p2][1]

    cv.line(img,(lmlist[p2][1],lmlist[p2][2]),(lmlist[p1][1],lmlist[p1][2]),(0,255,0),1,cv.LINE_AA)
    cv.circle(img,(lmlist[p2][1],lmlist[p2][2]),7,(0,255,0),1,cv.LINE_AA)
    cv.circle(img,(lmlist[p1][1],lmlist[p1][2]),7,(0,255,0),1,cv.LINE_AA)
    return x_d
        



detector=handDetector(cap)  


key=[['Q','W','E','R','T','Y','U','I','O','P'],
    ['A','S','D','F','G','H','J','K','L',';'],
    ['Z','X','C','V','B','N','M',',','.','<-']]

button_key=[]
finaltext=[]


while True:
    succ,img=cap.read()
    
    img=cv.resize(img,(1100,650))
    img=detector.findHands(img)
    lmlist =detector.findPosition(img)
    
    


    for i in range(3):
        for j in range(len(key[i])):
            obj=button([100+j*90,100+i*100],key[i][j])
            button_key.append(obj)
        
    img=draw(img,button_key)


    if lmlist:
        
        for button_ in button_key:
            x,y=button_.pos 
            h,w=button_.size 
            i=0
            if x <lmlist[8][1]< x+w and y<lmlist[8][2] <y +h:
                draw(img,button_,(175,0,175))
                l=dist(lmlist,8,12,img)
                
                if l<50:
                    if button_.text=="<-":
                        img=draw(img,button_,(0,255,0))
                        
                        finaltext.pop()
                        time.sleep(0.055)
                        break
                    img=draw(img,button_,(0,255,0))
                    
                    finaltext.append(button_.text)
                    time.sleep(0.055)
                    break
                        

                        
        


    
    cv.rectangle(img,(50,400),(700,480),(175,0,173),cv.FILLED)
    for i in range(len(finaltext)):
        cv.putText(img,finaltext[i],(60+i*45,440),cv.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,255),2,cv.LINE_4)
        
            




            

    

    cv.imshow('keybord',img)

    if cv.waitKey(1)==ord('q'):
        break
        
