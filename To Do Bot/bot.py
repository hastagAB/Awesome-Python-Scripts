import json
import requests
import time
import urllib
from dbhelper import DBHelper
import datetime
import os

db = DBHelper()

TOKEN = os.environ['TOKEN']
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def handle_updates(updates):
    text = ""
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
        except Exception as e:
            pass
        chat = update["message"]["chat"]["id"]
        if text.startswith("/delete"):
            t = text.split(" ")
            if len(t) < 2:
                send_message("Delete Item Properly.", chat)
            else:
                items = db.get_items(chat)
                if items == []:
                    send_message("Nothing to Delete.", chat)
                elif t[1] in items[0]:
                    db.delete_item(t[1], chat)
                    send_message("Item " + t[1] + " Deleted Successfully.", chat)
                else:
                    send_message("Item Not Found.", chat)
        elif text == "/start":
            send_message("Send /help to show help.", chat)
        elif text == "/help":
            message = "Send /add item_name due_date(dd-mm-yyyy) to add an item.\nSend /show to display items in to-do list.\nSend /due to check remaining days of each item.\nSend /delele to delete item."
            send_message(message, chat)
        elif text == "/show":
            items = db.get_items(chat)
            if items == []:
                send_message("Nothing to show.", chat)
            for i in range(len(items)):
                message = items[i][0] + " " + items[i][1]
                send_message(message, chat)
        elif text == "/due":
            items = db.get_items(chat)
            due = [0 for _ in range(0, len(items))]
            if items == []:
                send_message("Nothing to show.", chat)
            today = datetime.datetime.today().strftime("%d-%m-%Y")
            for i in range(0, len(items)):
                due[i] = (datetime.datetime.strptime(items[i][1], "%d-%m-%Y") -
                          datetime.datetime.strptime(today, "%d-%m-%Y")).days
                message = items[i][0] + " " + str(due[i]) + " days Remaining"
                send_message(message, chat)
        elif text.startswith("/add"):
            t = text.split(" ")
            if len(t) < 3:
                send_message("Insert Item Properly.\nSend /add item_name due_date to add an item.", chat)
            elif len(t[1]) < 1 or len(t[2]) < 1:
                send_message("Insert Item Properly.\nSend /add item_name due_date to add an item.", chat)
            else:
                db.add_item(t[1], t[2], chat)
                send_message("Item " + t[1] + " Inserted Successfully.", chat)
        else:
            send_message("Not a valid Input.", chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return text, chat_id


def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def main():
    db.setup()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()

