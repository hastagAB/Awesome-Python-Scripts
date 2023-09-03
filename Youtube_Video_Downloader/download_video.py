import os
import string
from pytube import Playlist, YouTube
from moviepy.editor import AudioFileClip


def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

def download_youtube_video(url, folder_path, quality, media_type,j):
    # Create a YouTube object
    yt = YouTube(url)
    # Remove invalid characters from the title
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    title = ''.join(c for c in yt.title if c in valid_chars)

    # Get the streams based on the media type
    if media_type == 'audio':
        audio_stream = yt.streams.get_audio_only()
        # Check if the stream is not None
        if audio_stream is not None:
            # Download the stream
            try:
                print(f"Downloading...")
                audio_stream.download(output_path=folder_path, filename="temp_file.mp4")
                print(f"Download completed!")

                input_file = os.path.join(folder_path, f"temp_file.mp4")
                output_file = os.path.join(folder_path, f"{title}.mp3")
                print("Converting to mp3...")
                MP4ToMP3(input_file, output_file)
                print("Conversion completed!")
                
                os.rename(output_file,f'{folder_path}\{title}.mp3')
                os.remove(input_file)
            
            except Exception as e:
                print(e) 
        else:
            print("No audio stream was found.")

    else:
        streams = yt.streams.filter(progressive=True)

        # Get the stream based on the quality
        stream = streams.filter(resolution=quality).first()

        # Check if the stream is not None
        if stream is not None:
            # Download the stream
            print(f"Downloading...")
            stream.download(output_path=folder_path)
            print(f"Download completed!")
        else:
            print(f"No stream with quality {quality} was found.")

def download_youtube_playlist(playlist_url,folder_path,quality,media_type):
    try:
        playlist = Playlist(playlist_url)
        i = 0
        for url in playlist:
            video_title = YouTube(url).title
            video_size = YouTube(url).streams.filter(resolution=quality).first().filesize/(1024*1024)
            print(f"Video title: {video_title} \nVideo size: {'%.2f' % video_size} MB")
            download_youtube_video(url,folder_path,quality,media_type,i)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            i += 1
    except Exception as e:
        print(e)

playlist_url = input('Enter the URL of the YouTube playlist: ')
folder_path = input('Enter the path of the folder where you want to save the videos: ')
media_type = input('Enter the media type (audio or video): ')
if media_type == 'video':
    quality = input('Enter the quality of the video (e.g. 720p, 1080p): ')
else:
    quality = None

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Download the playlist
download_youtube_playlist(playlist_url,folder_path,quality,media_type)
