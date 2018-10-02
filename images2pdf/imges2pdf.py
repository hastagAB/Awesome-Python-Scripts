
### img2pdf ####
import os 
import sys
from fpdf import FPDF 
from PIL import Image
import glob



images_path = raw_input("Enter the path of the folder containing images : ")
images =images_path+"/*.*"

assert os.path.exists(images_path), "this diretory doesn't exist, "+str(images_path)
f = os.chdir(images_path)
print("Hooray we found your directory!")

image_list = []
for filename in glob.glob(images): 
    
    image_list.append(filename)

pdf = FPDF( unit = 'mm')

imnames = [i.split("\\") for i in image_list] 
imnames = [i[-1] for i in imnames ]
imnums = [i.split('.') for i in imnames]
imnums = [i[0] for i in imnums]
imnums = [int(i) for i in imnums]



pos = 0 
images_dict = dict(zip(image_list, imnums))
sorted_images = sorted(images_dict , key = images_dict.get)

for i in list(sorted_images):
    pdf.add_page()
    im = Image.open(i)
    pdf.image(i,pos,pos,200,250)

pdf_name = raw_input("Enter the pdf name : ")
pdf_name = pdf_name+".pdf"
pdf.output(pdf_name)






