'''TODOs
more reliable and caching alert meethods (eg phone calls or sms)
server resourses
time taken to respond ping
to know wheather gone down for sometime and come up after sometime 
'''
from twilio.rest import Client
from telethon import TelegramClient
import requests
from telethon.tl.types import InputPeerChat
from telethon.tl.functions.messages import ImportChatInviteRequest
#your telegram api_id & hash 
#for more details get from telethon
def main():
    j
    api_id = #####
    api_hash = '######################'

# Your Account Sid and Auth Token from twilio.com/console
    account_sid = '###############'
    auth_token = '################'
    clients = Client(account_sid, auth_token)


#telegram_Side
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
#print(client.get_me().stringify())
#updates = client(ImportChatInviteRequest('FDVzKw8BPHTp2wyhwNqT2Q'))
    siteList=[site_list]
    for i in siteList:
        print(i)
        r = requests.head(i)
        if r.status_code == 200:
            message=i +"  returned  200"
            chat = InputPeerChat(chatID)
            client.send_message(chat, message)
            sms= clients.messages.create(to="#####",from_="##########",body="the  "+i+"   is not responding now  ")
            call = clients.calls.create(url='http://demo.twilio.com/docs/voice.xml',to='############',from_='#############')
            print(call.sid)
        else:
            chat = InputPeerChat(chatID)
            message="oops  " + i + "   not available at the moment"
            client.send_message(chat, message)


if __name__ == '__main__':
main()
