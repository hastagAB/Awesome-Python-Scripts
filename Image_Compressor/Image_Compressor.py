import PIL
from PIL import Image
from tkinter.filedialog import *

file_path=askopenfilenames()
img = PIL.Image.open(file_path)
myHeight,myWidth = img.size

img=img.resize((myHeight,myWidth),Image.Resampling.LANCZOS)
save_path=asksaveasfile()

img.save(save_path+"_compressed.JPG")