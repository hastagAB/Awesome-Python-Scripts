# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Process signatures to remove background.
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

from PIL import Image, ImageOps
import argparse

inFile = ''
outFile = ''


def binarize(img, threshold=127):
    """Utility function to binarize an image."""

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) > threshold:
                img.putpixel((i, j), 255)
            else:
                img.putpixel((i, j), 0)

    return img


def make_transparent(img):
    """Utility function to make transparent background from image."""

    img = img.convert("RGBA")
    data = img.getdata()

    transparent = []
    for item in data:
        if item[:3] == (255, 255, 255):
            transparent.append((255, 255, 255, 0))
        else:
            transparent.append(item)

    img.putdata(transparent)
    return img


def main(inFile, outFile, threshold=190):
    """Main function to process image."""

    img = Image.open(inFile).convert('L')
    img = binarize(img, threshold=threshold)
    img = make_transparent(img)
    img.save(outFile)

    return True


def parser():
    """Argument parser function."""

    # Construct the argument parser:
    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--input",
                    required=True,
                    type=str,
                    default="result.png",
                    help="Input image.")

    ap.add_argument("-o", "--output",
                    type=str,
                    default="result.png",
                    help="Output image.")

    ap.add_argument("-th", "--threshold",
                    type=int,
                    default=127)

    args = vars(ap.parse_args())

    return args['input'], args['output'], args['threshold']


if __name__ == "__main__":
    inFile, outFile, threshold = parser()
    main(inFile, outFile, threshold=threshold)
