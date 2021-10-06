# Website URL Detector

## Description
A python script that detects URLs on a given website.

## Usage

```py
>>> python detect_urls.py --website [website_url]
```

### Example

```py
>>> python detect_urls.py --website https://en.wikipedia.org/wiki/Guido_van_Rossum
https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Guido-portrait-2014-drc.jpg/1200px-Guido-portrait-2014-drc.jpg
https://creativecommons.org/licenses/by-sa/3.0/
https://en.wikipedia.org/wiki/Guido_van_Rossum
https://gvanrossum.github.io/
http://mail.python.org/pipermail/python-dev/2007-January/070849.html
https://web.archive.org/web/20090908131440/http://mail.python.org/pipermail/python-dev/2007-January/070849.html
http://www.computerhistory.org/atchm/2018-chm-fellow-guido-van-rossum-python-creator-benevolent-dictator-for-life/
https://web.archive.org/web/20180724114116/http://www.computerhistory.org/atchm/2018-chm-fellow-guido-van-rossum-python-creator-benevolent-dictator-for-life/
https://web.archive.org/web/20081031103755/http://wiki.codecall.net/Guido_van_Rossum
http://wiki.codecall.net/Guido_van_Rossum
...
```