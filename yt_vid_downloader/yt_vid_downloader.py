#A simple python program to download python programs.

from pytube import YouTube

def download_youtube_video(video_url, output_path):
    try:
        # Create a YouTube object using the provided video URL
        youtube = YouTube(video_url)
        
        # Select the highest resolution stream (first stream in the list)
        video_stream = youtube.streams.get_highest_resolution()
        
        # Download the video
        video_stream.download(output_path=output_path)
        
        print(f'Video downloaded successfully at: {output_path}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    # URL of the YouTube video you want to download
    youtube_video_url = input("Enter the YouTube video URL: ")
    
    # Path to save the downloaded video (including the file name and extension)
    output_video_path = input("Enter the output video path (e.g., video.mp4): ")
    
    # Download the YouTube video
    download_youtube_video(youtube_video_url, output_video_path)
