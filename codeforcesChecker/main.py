"""
Written By: Jinesh Parakh

This is the main script file which involves gathering data from the entered URL of codeforces website and saving the data into respective folders.
MOTIVE:
The main motive of this project is to help users save time while solving the problems and reduce the hassels of checking validity of their sample outputs with the expected sample outputs
"""
#import all the necessary libraries or modules
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import bs4
import requests
import os
import shutil
import filecmp
import sys
from termcolor import colored, cprint
from colorama import Fore, Back, Style

def getUrlforContest(): #function to get URL for contests
    print('Enter the URL of the page(Example:https://codeforces.com/contest/1328):  ', end='')
    url=input()
    if len(url)<30:
        cprint('Invalid URL', 'red',attrs=['bold'])
        sys.exit()
    return url
    
def getUrlforSingleProblem(): #function to get URL for a  problem from problemset
    print('Enter the URL of the page(Example:https://codeforces.com/problemset/problem/1333/E):  ', end='')
    url=input()
    if len(url)<43:
        cprint('Invalid URL', 'red',attrs=['bold'])
        sys.exit()
    return url

    
    
def getInputFiles(input):   #function to get sample inputs
    j=0
    for i in range(len(input)):
        print("Getting sample input " +str(i))
        x=input[i].text
        #print(x)
        x='\n'.join(x.split('\n')[1:])
        fileName='input'+ str(j)+'.txt'
        file=open(fileName,"w+")
        file.write(x)
        file.close()
        j+=1
def getOutputFiles(output): #function to get sample outputs
    k=0
    for i in range(len(output)):
        print("Getting sample output "+str(i))
        x=output[i].text
        #print(x)
        x='\n'.join(x.split('\n')[1:])
        fileName='output'+ str(k)+'.txt'
        file=open(fileName,"w+")
        file.write(x)
        file.close()
        k+=1
        

#The main menu for the project
print("---------MAIN MENU---------")
print("1.Enter 1 for live or virtual contests or to clone complete contest")
print("2.Enter 2 for a single problem from problemset")
print("Enter choice: ",end='')
choice=int(input())
if choice==1:  #for complete contest
    url=getUrlforContest()
    tp="'"+url[len(url)-13:]
    final='//a[contains(@href,'+tp+"/problem/'" + ')]'
    browser = webdriver.Chrome()
    browser.get(url)
    elements = browser.find_elements_by_xpath(final)  #get all required elements by xpath
    #print(elements)
    length=len(elements)
    length=length//2
    intialDirectory=os.getcwd()
    contestFolder='Contest '+url[len(url)-4:]
    os.makedirs(os.path.join(os.getcwd(),contestFolder)) #make directory for the contest
    os.chdir(os.path.join(os.getcwd(),contestFolder))
    for i in range(0,len(elements),2):
        currentDirectory=os.getcwd()
        toadd='Problem'+elements[i].text
        print("Getting essentials for Problem"+elements[i].text)
        res=requests.get(url+'/problem/'+elements[i].text)
        os.makedirs(os.path.join(currentDirectory,toadd)) #make directory for individual problems
        os.chdir(os.path.join(currentDirectory,toadd))
        soup=bs4.BeautifulSoup(res.text,'html.parser')  #using beautiful soup to parse HTML
        input=soup.find_all('div',{'class':'input'})
        output=soup.find_all('div',{'class':'output'})
        j=0
        #The next two shutil's are used to copy your template.cpp file and the checker script to all the problem folders
        shutil.copy(os.path.join(intialDirectory,'template.cpp'),os.path.join(os.getcwd(),'soln.cpp'))
        shutil.copy(os.path.join(intialDirectory,'checker.py'),os.path.join(os.getcwd(),'checker.py'))
        getInputFiles(input)
        getOutputFiles(output)
            
        os.chdir(currentDirectory)
        print()

    browser.quit() #quitting the browser window
    
else: #for a single problem
    url=getUrlforSingleProblem()
    browser = webdriver.Chrome()
    browser.get(url)
    intialDirectory=os.getcwd()
    problemFolder='Problem '+url[len(url)-6:len(url)-2]+url[len(url)-1:]
    os.makedirs(os.path.join(os.getcwd(),problemFolder))
    os.chdir(os.path.join(os.getcwd(),problemFolder))
    res=requests.get(url)
    soup=bs4.BeautifulSoup(res.text,'html.parser') #using beautiful soup to parse HTML
    input=soup.find_all('div',{'class':'input'})
    output=soup.find_all('div',{'class':'output'})
    #The next two shutil's are used to copy your template.cpp file and the checker script to all the problem folders
    shutil.copy(os.path.join(intialDirectory,'template.cpp'),os.path.join(os.getcwd(),'soln.cpp'))
    shutil.copy(os.path.join(intialDirectory,'checker.py'),os.path.join(os.getcwd(),'checker.py'))
    getInputFiles(input)
    getOutputFiles(output)
    browser.quit() #quitting the browser window
