import requests
import os
import json
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


os.makedirs('torrents', exist_ok=True)
check_path = os.path.join('torrents')
cache = os.listdir(check_path)


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


def download_torrent(bin_content, movie_name, type):
    torrent_name = movie_name + type + '.torrent'
    if '/' in torrent_name:
        torrent_name = torrent_name.split('/')[0]
    if torrent_name in cache:
        print("{} already downloaded".format(torrent_name))
    path = os.path.join('torrents', torrent_name)
    with open(path, 'wb') as f:
        f.write(bin_content)


# write the torrents json file names here.
torrent_list = ['torrents1.json', 'torrents2.json', 'torrents3.json', 'torrents5.json',
                'torrents6.json', 'torrents7.json', 'torrents8.json', 'torrents9.json',
                'torrents10.json', 'torrents11.json', 'torrents12.json', 'torrents13.json']
for torrent_json_file in torrent_list:
    if not os.path.isfile(torrent_json_file):
        print("{} does not exist. Run yts_am_api.py script "
              "to create json files with torrent links to download".format(
                  torrent_json_file))
        continue
    print(torrent_json_file)
    with open(torrent_json_file, 'r') as f:
        content = json.load(f)
    movies = list(content.keys())
    print("no. of movies: {}".format(len(movies)))
    for movie in movies:
        torrents = content[movie]
        bluray_1080 = torrents.get('1080_bluray')
        bluray_720 = torrents.get('720_bluray')
        web_1080 = torrents.get('1080_web')
        web_720 = torrents.get('720_web')
        movie = movie.encode('utf-8').decode('utf-8')
        print('movie', movie)
        time.sleep(0.01)
        if bluray_1080 is not None:
            response = requests_retry_session().get(bluray_1080, timeout=3)
            download_torrent(response.content, movie, 'bluray_1080p')
            continue
        elif web_1080 is not None:
            response = requests_retry_session().get(web_1080, timeout=3)
            download_torrent(response.content, movie, 'web_1080p')
            continue
        elif bluray_720 is not None:
            response = requests_retry_session().get(bluray_720, timeout=3)
            download_torrent(response.content, movie, 'bluray_720p')
            continue
        elif web_720 is not None:
            response = requests_retry_session().get(web_720, timeout=3)
            download_torrent(response.content, movie, 'web_720p')
            continue
        else:
            print('not any torrent')
