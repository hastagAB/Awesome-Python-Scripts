from pytube import YouTube
link = input('link to youtube video: ')
yt = Youtube(link)
yt.streams.first().download()
print('downloaded', link)
    





