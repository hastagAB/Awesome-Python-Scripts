import urllib.request
import requests
import json
import re
import sys

def download(post_id):
    multiple_posts = False
    videos = []
    data = requests.get("https://instagram.com/p/{}".format(post_id))
    if data.status_code == 404:
        print("Specified post not found")
        sys.exit()
    json_data = json.loads(re.findall(r'window._sharedData\s=\s(\{.*\});</script>', data.text)[0])
    data = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    if 'edge_sidecar_to_children' in data.keys():
        multiple_posts = True
    caption = data['edge_media_to_caption']['edges'][0]['node']['text']
    media_url = data['display_resources'][2]['src']
    is_video = data['is_video']
    if not is_video and not multiple_posts:
        print("No Videos found")
        sys.exit()
    if is_video:
        videos.append(data['video_url'])
    if multiple_posts:
        for post in data['edge_sidecar_to_children']['edges']:
            if post['node']['is_video']:
                videos.append(post['node']['video_url'])
    print("Found total {} videos".format(len(videos)))
    for no, video in zip(list(range(len(videos))), videos):
        print("Downloading video {}".format(no))
        urllib.request.urlretrieve(video, "{}_{}.mp4".format(post_id, no))

if len(sys.argv) == 1:
    print("Please provide instagram post id")
else:
    download(sys.argv[1])