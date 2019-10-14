import requests, bs4
from helpers import *

choice = get_topic()    
print('\nGetting latest article links from %s...' % (choice))

article_list = extract_links('https://medium.com/topic/' + choice)
print('Total articles found: ' + str(len(article_list)))

for i in range(len(article_list)):
    heading = article_list[i].getText()
    artlink = article_list[i].get('href')
    artlink = artlink if artlink.startswith("https://") else "https://medium.com" + artlink
    print('Downloading article: ' + str(i+1))

    # remove invalid characters from filename
    file_name = f"{heading}.txt".replace(':', '').replace('?', '')
    file = open(file_name, 'w')

    article_text = medium_text(artlink)
    file.write(article_text)
    file.close()

print('Done.')