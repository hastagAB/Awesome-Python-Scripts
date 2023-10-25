<<<<<<< HEAD
import PIL
from PIL import Image
from tkinter.filedialog import *

file_path=askopenfilenames()
img = PIL.Image.open(file_path)
myHeight,myWidth = img.size

img=img.resize((myHeight,myWidth),PIL.Image.ANTILIAS)
save_path=asksaveasfile()

img.save(save_path+"_compressed.JPG")
=======
import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilenames()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), PIL.Image.ANTILIAS)
save_path = asksaveasfile()

img.save(save_path + "_compressed.JPG")

import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilenames()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), PIL.Image.ANTILIAS)
save_path = asksaveasfile()

img.save(save_path + "_compressed.JPG")

import PIL
from PIL import Image
from tkinter.filedialog import *

file_paths = askopenfilenames()

if len(file_paths) == 0:
    print("No Files Selected")

for file in file_paths:
    file_name = file.split('/')[-1]
    file_name, extension = file_name.split('.')

    img = PIL.Image.open(file)
    height, width = img.size
    img = img.resize((height, width), Image.Resampling.LANCZOS)

    save_path = askdirectory()
    img.save(save_path + f"/{file_name}_compressed.{extension}")



import PIL
from PIL import Image
from tkinter.filedialog import *

file_paths = askopenfilenames()

if len(file_paths) == 0:
    print("No Files Selected")

for file in file_paths:
    file_name = file.split('/')[-1]
    file_name, extension = file_name.split('.')

    img = PIL.Image.open(file)
    height,width = img.size
    img=img.resize((height,width),Image.Resampling.LANCZOS)

    save_path=askdirectory()
    img.save(save_path+f"/{file_name}_compressed.{extension}")
>>>>>>> 06c603fe31712b13e986e2f388b82a8ab3703308
