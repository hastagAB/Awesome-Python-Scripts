import requests
from bs4 import BeautifulSoup

class SimpleWebpageParser():

	def __init__(self, url):
		self.url = url

	def getHTML(self):
		r  = requests.get(self.url)
		data = r.text
		soup = BeautifulSoup(data,"lxml")
		return soup