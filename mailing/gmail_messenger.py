#!/usr/bin/env python3

import smtplib                                      #import stmplib


try:                
    server = smtplib.SMTP("smtp.gmail.com", 587)    #establshing server connection
    server.ehlo()
    server.starttls()
    print("SERVER CONNECTED")
except:
    print("Could Not connect to Gmail")             #in case of failure

user = input("Enter User id\n")                     #YOUR ID
Pass_w = input("\nEnter your Password\n")           #YOUR Password
reciever_id = input("\nEnter reciever id\n")        #Reciever ID
msg = input("\nEnter message\n")                        #message

try:
    server.login(user, Pass_w)                      #user log in
    print("User Logged in")
except:
    print("Allow Less secure apps in GOOGLE ACCOUNT SETTINGS to use SMTP services")
    server.quit()
    exit()

server.sendmail(user, reciever_id, msg)
print("MAIL sent")                                  #confirmation


print("Closing Connection")
server.quit()                                       #closing server connection
print("Server closed")







