from bs4 import BeautifulSoup
import requests

s=requests.get('https://in.bookmyshow.com/bengaluru/movies/kannada')
h=requests.get('https://in.bookmyshow.com/bengaluru/movies/hindi')

soup = BeautifulSoup(s.content,"html.parser")


houp= BeautifulSoup(h.content,"html.parser")


print ("KANNADA MOVIES FOR THE WEEKEND")
print ('==========================================================')
g_movy=soup.find_all("div",{"class":"card-container wow fadeIn movie-card-container"})      #looks for particular class
for link in g_movy:
    string=link.find('a')['href'][18:]
    pos=string.find('/')
    print (string[:pos])

    
print ('\n')


print ('HINDI MOVIES FOR THE WEEKEND') 
print ('=========================================================')
h_movy=houp.find_all("div",{"class":"card-container wow fadeIn movie-card-container"})
for link in h_movy:
    string=link.find('a')['href'][18:]
    pos=string.find('/')
    print (string[:pos])
