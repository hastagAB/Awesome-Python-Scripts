"""
This file uses mediapipe - a framework by google to detect the landmarks of hand (21)
in the image captured from webcam using openCV
The functionality wrapped as handDetector class containing methods drawHands() and getPositions()
drawHands() --> To draw land marks of detected hands
getPositions() --> To return the found landmarks as a list
"""
import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.hands = mp.solutions.hands.Hands(static_image_mode=self.mode,max_num_hands= self.maxHands,min_detection_confidence=self.detectionCon,min_tracking_confidence= self.trackCon)
    def drawHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res = self.hands.process(imgRGB)
        if self.res.multi_hand_landmarks:
            for handLms in self.res.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,mp.solutions.hands.HAND_CONNECTIONS)
        return img

    def getPositions(self, img, handId=0):
        self.xList=[]
        self.yList=[]
        self.lmList = []
        if self.res.multi_hand_landmarks:
            decHand = self.res.multi_hand_landmarks[handId]
            for index, lmark in enumerate(decHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lmark.x * w), int(lmark.y * h)
                self.xList.append(cx)
                self.yList.append(cy)
                self.lmList.append([index, cx, cy])
        return self.lmList

def main():
    prevTime = 0
    currTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        _, img = cap.read()
        img = detector.drawHands(img)
        lms= detector.getPositions(img)
        print(lms)
        currTime = time.time()
        fps = 1 / (cTime - pTime)
        prevTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(51, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
