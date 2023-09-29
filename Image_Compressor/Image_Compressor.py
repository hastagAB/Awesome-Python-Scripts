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