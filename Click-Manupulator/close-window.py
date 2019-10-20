from pynput.mouse import Button, Controller
import time
mouse = Controller()



def close_tab_clicker():
    time.sleep(3)
    mouse.position=(1901,9)
    mouse.press=(Button.left,1)
    mouse.release=(Button.left,1)
    print("Current screen is closed for full screen windows tabs.")


close_tab_clicker();
