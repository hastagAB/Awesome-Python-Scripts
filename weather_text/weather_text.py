import requests
import json
import os

from twilio.rest import Client


api_key = os.environ['API_KEY']
base_url = os.environ['BASE_URL']

zip_code = input("Enter your Zip code: ")
region = input("Enter your region: ")
complete_url = base_url + "zip=" + zip_code + "," + region + "&appid=" + api_key
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404" :
    y = x["main"]
    current_temp = y["temp"]

conversion_temp = (current_temp - 273.15) * 9/5 + 32

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)

numFrom = input("Enter your number: ")
numTo = input("Enter your sender number: ")


message = client.messages \
                .create(
                        body="Temperature is: " + str(conversion_temp),
                        from_=numFrom,
                        to= numTo
                        )
print(message.sid)
