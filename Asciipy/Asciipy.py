import cv2
import sys
sys.path.insert(1, 'clear/')
from cleaner import clean
from PIL import Image
import requests
from io import BytesIO
import time
import urllib.request
import os

class AsciiText :
    
    def GenerateText(self, text, font):
        
        q = text.replace(" ","+")
        r = requests.get('http://artii.herokuapp.com/make?text='+q+'&font='+font)
        print(r.text)
        return r.text
        
    def FontList(self):
        r = requests.get('http://artii.herokuapp.com/fonts_list')
        print(r.text)
        return r.text

class AsciiImage :

    def GenerateFromUrl(self, url):


        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
            
    

        width, height = img.size
        aspect_ratio = height/width
        new_width = 200
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))

        img = img.convert('L')

        pixels = img.getdata()

        chars = ["B","S","#","&","@","$","%","*","!",":","."]
        n_pixels = [chars[pixel//25] for pixel in pixels]
        n_pixels = ''.join(n_pixels)

        new_pixels_count = len(n_pixels)
        ascii_image = [n_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        print(ascii_image)

        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
        return ascii_image
            
    def GenerateFromPath(self,path):

        img = Image.open(path)
            
    

        width, height = img.size
        aspect_ratio = height/width
        new_width = 200
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))

        img = img.convert('L')

        pixels = img.getdata()

        chars = ["B","S","#","&","@","$","%","*","!",":","."]
        n_pixels = [chars[pixel//25] for pixel in pixels]
        n_pixels = ''.join(n_pixels)

        new_pixels_count = len(n_pixels)
        ascii_image = [n_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        print(ascii_image)

        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
        return ascii_image
class AsciiVideo :

    def VideoFromPath(self, path):
        clean.cleanframes()
        vidObj = cv2.VideoCapture(path) 
        count = 0  
        success = 1
        completeVideo = ""
  
        while success: 
          try:
            success, image = vidObj.read()
            cv2.imwrite("gen/frames/frame%d.jpg" % count, image)
            try:
                img = Image.open("gen/frames/frame%d.jpg" % count)
            except IOError:
                print("")
                #print('File is not accessible')
            #img = Image.open("bin/frames/frame%d.jpg" % count)
            width, height = img.size
            aspect_ratio = height/width
            new_width = 200
            new_height = aspect_ratio * new_width * 0.55
            img = img.resize((new_width, int(new_height)))
            
            img = img.convert('L')

            pixels = img.getdata()

            chars = ["B","S","#","&","@","$","%","*","!",":","."]
            n_pixels = [chars[pixel//25] for pixel in pixels]
            n_pixels = ''.join(n_pixels)

            new_pixels_count = len(n_pixels)
            ascii_image = [n_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
            ascii_image = "\n".join(ascii_image)
            #os.system('cls' if os.name == 'nt' else 'clear')
            completeVideo = completeVideo + ascii_image
            print(ascii_image, end='\r')
            #return ascii_image
            count += 1
          except KeyboardInterrupt:
               clean.cleanframes()
               clean.cleanVids()
               print("KeyboardInterrupt")
               sys.exit(0)
        clean.cleanframes()
        return completeVideo
    
    def VideoFromUrl(self, url):
       #urllib.request.urlretrieve(url, 'gen/vids/video.mp4')
       clean.cleanframes()
               
       myfile = requests.get(url)   
       open('gen/vids/video.mp4', 'wb').write(myfile.content)
       vidObj = cv2.VideoCapture("gen/vids/video.mp4") 
       count = 0  
       success = 1
       completeVideo = ""
  
       while success: 
          try:
            success, image = vidObj.read()
            cv2.imwrite("gen/frames/frame%d.jpg" % count, image)
            try:
                img = Image.open("gen/frames/frame%d.jpg" % count)
            except IOError:
                print("")
                #print('File is not accessible')
            #img = Image.open("bin/frames/frame%d.jpg" % count)
            width, height = img.size
            aspect_ratio = height/width
            new_width = 200
            new_height = aspect_ratio * new_width * 0.55
            img = img.resize((new_width, int(new_height)))
            
            img = img.convert('L')

            pixels = img.getdata()

            chars = ["B","S","#","&","@","$","%","*","!",":","."]
            n_pixels = [chars[pixel//25] for pixel in pixels]
            n_pixels = ''.join(n_pixels)

            new_pixels_count = len(n_pixels)
            ascii_image = [n_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
            ascii_image = "\n".join(ascii_image)
            #os.system('cls' if os.name == 'nt' else 'clear')
            completeVideo = completeVideo + ascii_image
            print(ascii_image, end='\r')
            #return ascii_image
            count += 1
          except KeyboardInterrupt:
              
              clean.cleanframes()
              print("KeyboardInterrupt")       
              sys.exit(0)    
       #clean.cleanframes()
       clean.cleanVids()
       return completeVideo
class AsciiHelp:
    
    def help(self):
        print('AsciiPy v0.1 tool help\n','-u generates a Ascii art image from url : py AsciiPy.py -u https://r4yan.ga/images-videos/python-logo.png\n')
        print('-p generates a Ascii art image from path : py AsciiPy.py -p /path/to/my/image.png\n')
        print('-f give you all the fonts you can use\n')
    
if __name__ == '__main__':
    asciiImage = AsciiImage()
    asciiText = AsciiText()
    if sys.argv[1].startswith('-u'):
        asciiImage.GenerateFromUrl(sys.argv[2])
    elif sys.argv[1].startswith('-p'):
        asciiImage.GenerateFromPath(sys.argv[2])
    elif sys.argv[1].startswith('-t'):
         asciiText.GenerateText(sys.argv[2], sys.argv[3])
    elif sys.argv[1].startswith('-f'):
        asciiText.FontList()
    elif sys.argv[1].startswith('-vid-path'):
        clean.cleanframes()
        AsciiVideo().VideoFromPath(sys.argv[2])
    elif sys.argv[1].startswith('-vid-url'):
        clean.cleanframes()
        clean.cleanVids()
        AsciiVideo().VideoFromUrl(sys.argv[2])
    elif sys.argv[1].startswith('-h'):
        AsciiHelp().help()
