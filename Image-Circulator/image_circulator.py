#!/usr/bin/env python3

from PIL import Image, ImageOps, ImageDraw
from argparse import ArgumentParser


parser = ArgumentParser()
inputfile = parser.add_argument('-i', '--inputfile', help='input file path')
outputfile = parser.add_argument('-o', '--outputfile', help='output file path')
diameter = parser.add_argument('-d', '--diameter', help='output file diameter')

args = parser.parse_args()


print('Input file is '+ str(args.inputfile))
print('Output file is '+ str(args.outputfile))
print('Image diameter will be '+ str(args.diameter))

im = Image.open(args.inputfile)

width, height = im.size
        
left = (width - int(args.diameter))/2
top = (height - int(args.diameter))/2
right = (width + int(args.diameter))/2
bottom = (height + int(args.diameter))/2
  
im = im.crop((left, top, right, bottom));
  
bigsize = (im.size[0] * 3, im.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(im.size, Image.ANTIALIAS)
im.putalpha(mask)
  
output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)
output.save(args.outputfile)

print('Done!')
