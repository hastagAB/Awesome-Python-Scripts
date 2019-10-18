import requests, os, bs4
url = 'http://xkcd.com'
os.mkdir('xkcdcomics')
while not url.endswith('#'):    # Download the page.    
    print('Downloading page %s...' % url)    
    res = requests.get(url)    
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # Find the URL of the comic image.    
    comicElem = soup.select('#comic img')    
    if comicElem == []:
        print('Could not find comic image.')    
    else:        
        comicUrl = 'http:' + comicElem[0].get('src')       
        # Download the image.        
        print('Downloading image %s...' % (comicUrl))        
        res = requests.get(comicUrl)        
        res.raise_for_status()
        imageFile = open(os.path.join('xkcdcomics', os.path.basename(comicUrl)), 'wb')        
        for chunk in res.iter_content(100000): 
            imageFile.write(chunk)        
        imageFile.close()
    # Get the Prev button's url.    
    prevLink = soup.select('a[rel="prev"]')[0]    
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
 
