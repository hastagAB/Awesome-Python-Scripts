import requests
import json
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def create_json_file(json_file_number):
    name = 'torrents' + str(json_file_number) + '.json'
    with open(name, 'w') as f:
        content = {}
        json.dump(content, f)


def add_torrent_to_json_file(json_file_number):
    name = 'torrents' + str(json_file_number) + '.json'
    with open(name, 'r') as f:
        content = json.load(f)
    content[title_long] = {'720_bluray': torrent_720_bluray, '1080_bluray': torrent_1080_bluray,
                           '720_web': torrent_720_web, '1080_web': torrent_1080_web}
    with open(name, 'w') as f:
        json.dump(content, f)


json_file_number = 1
create_json_file(json_file_number)
url = "https://yts.am/api/v2/list_movies.json?limit=50&page="

count = 0
movie_count = 0
for page in range(1, 424):
    count += 1
    api_url = url + str(page)
    time.sleep(1)
    print(api_url)
    response = requests_retry_session().get(api_url, timeout=3).json()
    time.sleep(2)
    data = response.get('data')
    movies = data.get('movies')
    if movies is None:
        print("No more torrents on this page")
        exit()
    for movie in movies:
        movie_count += 1
        title_long = movie.get('title_long')
        print(title_long)
        print('movie_count', movie_count)
        torrents = movie.get('torrents')
        if torrents is None:
            print("no torrent for this movie")
            continue
        torrent_720_web = None
        torrent_1080_web = None
        torrent_720_bluray = None
        torrent_1080_bluray = None
        for torrent in torrents:
            if torrent.get('quality') == "720p":
                if torrent.get('type') == "web":
                    torrent_720_web = torrent.get('url')
                elif torrent.get('type') == "bluray":
                    torrent_720_bluray = torrent.get('url')
            elif torrent.get('quality') == "1080p":
                if torrent.get('type') == "web":
                    torrent_1080_web = torrent.get('url')
                elif torrent.get('type') == "bluray":
                    torrent_1080_bluray = torrent.get('url')
        if count < 20:
            add_torrent_to_json_file(json_file_number)
        else:
            count = 1
            json_file_number += 1
            create_json_file(json_file_number)
            add_torrent_to_json_file(json_file_number)
