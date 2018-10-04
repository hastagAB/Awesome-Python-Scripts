# Slideshare-Downloader
Download slides from slideshows shared on SlideShare (Now LinkedIn SlideShare) as a PDF.

# Usage
This was written for Python 3, but it should work with Python 2.7 as well.

## Installation 
### Linux/Mac
```bash
python3 -m pip install --user -U -r requirements.txt
python3 slideshare_downloader.py --help
```

### Windows
```powershell
py -3 -m pip install --user -U -r requirements.txt
py -3 slideshare_downloader.py --help
```

## Running
```bash
slideshare_downloader.py -f some_slides -u http://www.slideshare.net/codeblue_jp/igor-skochinsky-enpub
```