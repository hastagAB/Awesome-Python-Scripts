import urllib3
import json
http = urllib3.PoolManager()
r = http.request('GET', 'http://ipinfo.io/json')
data = json.loads(r.data.decode('utf-8'))
city=data['city']
loc=data['loc']
print(city,loc)
from twilio.rest import Client

client = Client("TWILO SSID", "AUTH TOKEN")
client.messages.create(to="PHONE NO YOU WANT TO SEND SMS",
                       from_="YOUR TWILLO PHONE NUMBER",
body="hi amma i am in  "+city+"   now and my cordinates are  " +loc)
