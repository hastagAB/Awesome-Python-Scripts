#!/bin/python   
# -*- coding: utf-8 -*-

# <Summary>Create a pseudo random password with alphanumeric, numbers, and special characters</summary>  

import secrets #implemented in python version 3.6+

#String of characters
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+`~[]{]\|;:,<.>/?'

#2 for loops should be O(n²) runtime
def create(number_of_passwords, pass_length):
    for i in range(number_of_passwords):
        list = [] # create new empty list
        for i in range(pass_length):
            select = secrets.choice(chars) #the secret sauce to select a pseudo random character
            list.append(select) #add pseudo random char to list
        l = ''.join(list) #concatenate list to string for every ''
        print(l) #<-- comment me out for faster computing
    return l

#Run function
create(int(5),int(20)) #number_of_passwords, pass_length