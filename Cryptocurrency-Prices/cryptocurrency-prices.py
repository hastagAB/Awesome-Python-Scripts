#!python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import sys
import os

#get the price
def get_price():
	#response from the url
	response = requests.get(url)

	#soup object of the html content
	soup = BeautifulSoup(response.content,'html.parser')

	#for bitcoin
	if asset == 'btc':
		price = soup.find('span',{'class':'price'}).text #bitcoin works faster with the price class

	#for other altcoins
	else:
		price = soup.find('span',{'class':'woobJfK-Xb2EM1W1o8yoE'}).text #other altcoins only work with this class

	return float(price.replace(",",""))

#asset choice
asset = input('Abbreviation of the asset: ')
url = 'https://cryptowat.ch/assets/' + asset

#catching the NoneType AttributeError error for coins that cant be found
try:
	price = get_price()

except AttributeError:
	print("The asset doesn't exist or it's not supported!")
	sys.exit()

#visual
if sys.platform == 'win32':
	os.system('cls')
else:
	os.system('clear')

#since the last price must be something from the start its set to 0
price = 0

#loop
while True:

	#getting the price
	last_price = price
	price = get_price()

	#coloring the price according to the change
	if price > last_price:
		color = Fore.GREEN
	elif last_price > price:
		color = Fore.RED
	else:
		color = Style.RESET_ALL

	#printing the price
	print('$ ',end='')
	print(color + str(price) + Style.RESET_ALL)