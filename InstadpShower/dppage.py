from bs4 import BeautifulSoup
import requests
import webbrowser as wb


username = input("Enter the instagram user-id: ")

try:
    a = requests.get("https://www.instagram.com/"+username)
    co = a.content
    soup = BeautifulSoup(co,'html.parser')
    link = soup.find_all('meta' , property="og:image")
    print(link)
    print(type(soup))

    imagelink=(str(link[0])[15:])
    imagelink=imagelink[:len(imagelink)-23]
    print(imagelink)
    wb.open_new_tab(imagelink)

except :
    print("No such username exists")


