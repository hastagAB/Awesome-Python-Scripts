import time
from datetime import datetime as dt

host_temp = "hosts" #host file copied to the directory for ease.
host_path = r"/etc/hosts" #original host file address in linux
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"] #You can add your own list of websites

while True:
     if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): #You can choose your own working time period
         print("working hours...")
         with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
            else:
                file.write(redirect+" "+ website+"\n")
     else:
         with open(host_path,'r+') as file:
             content=file.readlines()
             file.seek(0)
             for line in content:
                 if not any(website in line for website in website_list):
                     file.write(line)
             file.truncate()
         print("fun hours...")
     time.sleep(10)
