import psutil
import time
import pyttsx3
from win10toast import ToastNotifier # also need to install win32api
import threading

toaster = ToastNotifier()
x=pyttsx3.init()
x.setProperty('rate',110)
x.setProperty('volume',3)
count = 0

def show_notification(show_text):
   toaster.show_toast(show_text,
                       icon_path='battery_indicator.ico',
                       duration=10)
   # loop the toaster over some period of time
   while toaster.notification_active():
      time.sleep(0.005)

def monitor():
   while (True):
      time.sleep(1)
      battery = psutil.sensors_battery()
      plugged = battery.power_plugged
      percent = int(battery.percent)

      if percent < 35:
         if plugged == False:
            processThread = threading.Thread(target=show_notification, args=("Your Battery at "+str(percent)+"% Please plug the cable",))  # <- note extra ','
            processThread.start()
            x.say("Your battery is getting low so charge it right now")
            x.runAndWait()

      elif percent >= 98:
         if plugged == True:
            processThread = threading.Thread(target=show_notification, args=("Charging is getting complete",))  # <- note extra ','
            processThread.start()
            x.say("Charging is getting complete")
            x.runAndWait()
if __name__ == "__main__":
   monitor()
