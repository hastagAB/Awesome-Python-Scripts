import sys
from PIL import Image
from PIL.ExifTags import TAGS

image_file = sys.argv[1]
image_name = image_file.split(".")[0]

try:
    image = Image.open(image_file)
except IOError:
    print("Error in loading image!!")
    sys.exit(1)
    
bw_image = image.convert('L')
bw_image.save("bw_"+image_name+".png")
