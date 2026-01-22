import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
from numpy import asarray
import time

def click(key):
    pyautogui.keyDown(key)
    return

def isCollision(data):
# Check colison for birds
    for i in range(530,560):
        for j in range(80, 127):
            if data[i, j] < 171:
                click("down")
                return
 # Check colison for cactus
    for i in range(530, 620):
        for j in range(130, 160):
            if data[i, j] < 100:
                click("up")
                return
    return

if __name__ == "__main__":
    time.sleep(5)
    click('up') 
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)
        
        # # Draw the rectangle for cactus
        # for i in range(530, 610):
        #     for j in range(130, 160):
        #          data[i, j] = 0
        
        # # # Draw the rectangle for birds
        # for i in range(530, 560):
        #     for j in range(100, 125):
        #         data[i, j] = 171

        # image.show()
        # break
        