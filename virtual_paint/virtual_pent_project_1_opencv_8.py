import cv2 as cv 
import numpy as np

framew=600
frameh=400
#facecascade=cv.CascadeClassifier("archive\haarcascade_frontalface_alt.xml")
cap=cv.VideoCapture(0)
cap.set(3,framew)
cap.set(4,frameh)

mycolore=[[5,107,0,18,255,255],[133,56,0,159,156,255],[57,76,0,100,255,255]]#[0,27,7,179,255,72]]

mycolorvalue=[[51,153,255],[255,0,255],[0,255,0]]  #BGR
x,y=0,0
mypoint= []    #[x,y,colorid]

def empty():
    pass

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars",640,240)

cv.createTrackbar("hue min","Trackbars",0,179,empty)
cv.createTrackbar("hue max","Trackbars",0,179,empty)
cv.createTrackbar("sat min","Trackbars",0,255,empty)
cv.createTrackbar("sat max","Trackbars",0,255,empty)
cv.createTrackbar("val min","Trackbars",0,255,empty)
cv.createTrackbar("val max","Trackbars",0,255,empty)


def findcolore(img,mycolore,mycolorvalue):
    
    imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min=cv.getTrackbarPos("hue min","Trackbars")
    h_max=cv.getTrackbarPos("hue max","Trackbars")
    s_min=cv.getTrackbarPos("sat min","Trackbars")
    s_max=cv.getTrackbarPos("sat max","Trackbars")
    v_min=cv.getTrackbarPos("val min","Trackbars")
    v_max=cv.getTrackbarPos("val max","Trackbars")

    count =0
    newpoint=[]
    

    for colore in mycolore:
        

        lower=np.array(colore[0:3])
        upper=np.array(colore[3:6])
        mask=cv.inRange(imghsv,lower,upper)
        x,y=getcontours(mask)
        cv.circle(imgcontuor,(x,y),10,mycolorvalue[count],cv.FILLED)
        
        if x!=0 and y!=0:
            newpoint.append([x,y,count])

        count+=1
        #cv.imshow(str(colore[0]),mask)
    #lower=np.array([h_min,s_min,v_min])
   # upper=np.array([h_max,s_max,v_max])
    #mask=cv.inRange(imghsv,lower,upper)
    return newpoint
    

    

        
    
     
def getcontours(img):
    contours,hierachy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv.contourArea(cnt)
        
        

        if area >500:
            #cv.drawContours(imgcontuor,cnt,-1,mycolorvalue,3)
            
            per1=cv.arcLength(cnt,True)
            
            approx=cv.approxPolyDP(cnt,0.02*per1,True)
            
            
            x, y, w, h = cv.boundingRect(approx)
            
            if cv.waitKey(1)  ==  ord('q'):
                break
           

    return (x+w//2,y)


            
            
            
def drawoncanvas(mypoint,mycolorvalue):
    
    for point in mypoint:
        cv.circle(imgcontuor,(point[0],point[1]),10,mycolorvalue[point[2]],cv.FILLED)
    



while True:
    succ,img=cap.read()
    #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgcontuor=img.copy()
    

    newpoint=findcolore(img,mycolore,mycolorvalue)
    if len(newpoint)!=0:
        for nwp in newpoint:
            mypoint.append(nwp)
    if len(mypoint)!=0:
        drawoncanvas(mypoint,mycolorvalue)


    #face dectection by casked files
    #face=facecascade.detectMultiScale(img,1.1,4)
    #for (x,y,w,h) in face:
        #cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #cv.imshow("video img",img)
    cv.imshow("video",imgcontuor)
    if cv.waitKey(1)  ==  ord('q'):
        break


    