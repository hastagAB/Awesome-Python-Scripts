import random
import pygame, sys
from pygame.locals import *
import cv2 as cv
import numpy as np 
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import time 
import pandas as pd
from timeit import default_timer as timer
import os
from joblib import dump, load

cap=cv.VideoCapture(0)

detector_c=HandDetector(cap)





pygame.init()
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [0,0]
ball_vel = [0,0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    horz = random.randrange(2,4)
    vert = random.randrange(1,3)
    
    if right == False:
        horz = - horz
        
    ball_vel = [horz,-vert]

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,l_score,r_score  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH - 1,HEIGHT/2]
    paddle2_pos = [WIDTH +1 - HALF_PAD_WIDTH,HEIGHT/2]
    l_score = 0
    r_score = 0
    if random.randrange(0,2) == 0:
        ball_init(True)
    else:
        ball_init(False)



def collect_data(ball_pos,paddle_1,paddle_2,ball_vel):
    data = pd.DataFrame(columns=np.array([ball_pos[0], ball_pos[1], ball_vel[0], ball_vel[1],paddle_2,paddle_1]))
    
    data.to_csv("data.csv",mode="a")
    

    

#draw function of canvas

def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score
           
    canvas.fill(BLACK)
    pygame.draw.line(canvas, WHITE, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel
    
    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel





    #update ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])
    if ball_pos[0]<270 and ball_vel[0]<0 :
        #collect_data(ball_pos,paddle1_pos[1],paddle2_pos[1],ball_vel) 
        #print("ball position : ",ball_pos)
        #print("ball velocity : ",ball_vel)
        #print("paddle_1 position",paddle1_pos[1])
        #print("paddle_2 position",paddle2_pos[1])
        pass


    #draw paddles and ball
    pygame.draw.circle(canvas, RED, ball_pos, 20, 0)
    pygame.draw.polygon(canvas, GREEN, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
    pygame.draw.polygon(canvas, GREEN, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)

    #ball collision check on top and bottom walls
    if round(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if round(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    #ball collison check on gutters or paddles
    if round(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and round(ball_pos[1]) in range(round(paddle1_pos[1] - HALF_PAD_HEIGHT),round(paddle1_pos[1]+ HALF_PAD_HEIGHT),1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif round(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
        r_score += 1
        ball_init(True)
        
    if round(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and round(ball_pos[1]) in range(round(paddle2_pos[1] - HALF_PAD_HEIGHT),round(paddle2_pos[1]+ HALF_PAD_HEIGHT),1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif round(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
        l_score += 1
        ball_init(False)

    #update scores
    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score "+str(l_score), 1, (255,255,0))
    canvas.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score "+str(r_score), 1, (255,255,0))
    canvas.blit(label2, (470, 20))  
    
    
#keydown handler
def keydown(event):
    global paddle1_vel, paddle2_vel
    
    
    if event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8

#keyup handler
def keyup(event):
    global paddle1_vel, paddle2_vel
    
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    

init()

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


def dist(lmlist,p1,p2,img):
    x_d=lmlist[p1][1]-lmlist[p2][1]

    cv.line(img,(lmlist[p2][1],lmlist[p2][2]),(lmlist[p1][1],lmlist[p1][2]),(0,255,0),1,cv.LINE_AA)
    cv.circle(img,(lmlist[p2][1],lmlist[p2][2]),7,(0,255,0),1,cv.LINE_AA)
    cv.circle(img,(lmlist[p1][1],lmlist[p1][2]),7,(0,255,0),1,cv.LINE_AA)
    return x_d

detector=handDetector(cap)  

global model
model=load("model_v1.joblib")

def predictor():
    global paddle1_vel,model
    data=np.array((ball_pos[0],ball_pos[1],ball_vel[0],ball_vel[1])).reshape((1,4))
    if ball_pos[0]<270 and ball_vel[0]<0 :
        prediction= model.predict(data)

        pos_1=paddle1_pos[1]

        i=0
        if prediction >=pos_1 :
            while (prediction>=pos_1):
                print(prediction)
                paddle1_vel=8
                i+=1
                if i>=1:
                    break
        elif prediction <=pos_1 :
            while (prediction<=pos_1):
                print(prediction)
                paddle1_vel=-8
                i+=1
                if i>=1:
                    break

   





#game loop
while True:
    
    draw(window)
    succ,image=cap.read()
    
    img=cv.resize(image,(WIDTH, HEIGHT))
    imgd=detector.findHands(img)
    lmlist =detector.findPosition(imgd)
    
    try:
        l=dist(lmlist,8,12,img)
        if l< 50:
            cv.circle(img,(lmlist[8][1]-10,lmlist[12][2]+10),15,(0,255,0),cv.FILLED)
            if lmlist[8][2]<150:
                paddle2_vel = -5

            elif lmlist[8][2]>150:
                paddle2_vel = 5

    except:
        pass
    
    
    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    predictor()        
    pygame.display.update()
    fps.tick(60)
    cv.imshow('keybord',img)

    if cv.waitKey(1)==ord('q'):
        break
