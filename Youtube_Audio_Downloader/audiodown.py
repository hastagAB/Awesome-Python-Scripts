import os
character = 'Y'
while character == 'Y' or character == 'y':
    urlink = input("Enter the URL of the Video : ")
    command = "youtube-dl -f 140 "+urlink
    os.system(command)
    character = input("Video Downloaded! Press Y to download another : ")
