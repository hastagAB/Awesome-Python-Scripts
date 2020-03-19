# yts_torrents

Download all torrents from yts.am (yify movies). Uses yify api.

## Usage

-   Create a virtualenv:

```
python3 -m venv venv
```

-   Activate it on Linux:

```
. venv/bin/activate
```

-   Or on Windows cmd:

```
venv\Scripts\activate.bat
```

-   Install requirements

```
pip install -r requirements
```

run `python yts_am_api.py` to make json files containing torrent links of the movies. Then run `python linkdownload.py`
to parse the created json files and download the torrents.

## Priority

The torrents will be downloaded according to the following priority:

1080p bluray> 1080p web> 720p bluray> 720p web

## Disclaimer

Downloading copyright movies may be illegal in your country. This tool is for educational purposes only and was created only to experiment with [yify api](https://yts.am/api)

## Original Repository

Check out the original repository at https://github.com/makkoncept/yts_torrents.

This project was used to create [movie_torrents](https://github.com/makkoncept/movie_torrents)[repository of 10k+ movie torrents].
