import pyautogui as pg
import webbrowser as wb
import time
import sys
links = ["www.youtube.com/Pranked03"]
string = "Thank you for subscribing to my channel"
string = list(string)
dire = "./assets/"
for link in links:
    
    wb.open_new_tab(link)
    find_sub = pg.locateCenterOnScreen(dire+"subscribe.png")
    find_sub_dark = pg.locateCenterOnScreen(dire+"subscribed_black.png")
    find_sub_light = pg.locateCenterOnScreen(dire+"subscribed_light.png")

    while find_sub == None and find_sub_dark == None and find_sub_light == None:
        find_sub = pg.locateCenterOnScreen(dire+"subscribe.png")
        find_sub_dark = pg.locateCenterOnScreen(dire+"subscribed_black.png")
        find_sub_light = pg.locateCenterOnScreen(dire+"subscribed_light.png")

    if find_sub != None:
        pg.click(find_sub)
        time.sleep(1)
    elif find_sub_dark != None:
        pass
    elif find_sub_light != None:
        pass
    else:
        print("Nope")
        
wb.open_new_tab("www.google.com")
google = pg.locateCenterOnScreen(dire+"google.png")
google_dark = pg.locateCenterOnScreen(dire+"google_black.png")

while google == None and google_dark == None:
    google = pg.locateCenterOnScreen(dire+"google.png")
    google_dark = pg.locateCenterOnScreen(dire+"google_black.png")
    
pg.typewrite(string, interval=0.05)
try:
    while True:
        pg.hotkey("ctrl", "w")
except:
    pass
sys.exit()
exit()
