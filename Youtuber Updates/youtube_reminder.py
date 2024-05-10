import urllib.request
import json
from selenium import webdriver
import time


def look_for_new_videos():
    api_key = "" # Whatever API key you get from https://console.developers.google.com
    channel_id = "LaterClips"# From https://www.youtube.com/c/LaterClips

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
    inp = urllib.request.urlopen(url).read()
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']

    video_exists = False
    with open('videoId.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            driver = webdriver.Edge
            driver.get(base_video_url + vidID)
            video_exists = True

    if video_exists:
        with open('videoId.json', 'w') as json_file:
            data = {'videoId': vidID}
            json.dump(data, json_file)


try:
    while True:
        print("Starting...")
        look_for_new_videos()
        time.sleep(10)
except KeyboardInterrupt:
    print("Stopping")
