#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Credit for base code goes to: yodiaditya
# https://github.com/yodiaditya/slideshare-downloader/blob/master/convertpdf.py

"""SlideShare Downloader.

Usage:
    slideshare_downloader.py [options]

Options:
    -h, --help  Show this screen
    -f <file>   Specify output filename
    -u <url>    URL to download
"""

import img2pdf
from docopt import docopt

from os import walk, mkdir, chdir, getcwd
from os.path import join

from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get


class SlideShare:
    """ Download slides from SlideShare and convert them into a PDF. """
    def __init__(self):
        self.TOP_DIR = getcwd()

    def get_slides(self, download_url=None, filename=None):
        if download_url:
            i_dir = self.download_images(download_url)
        else:
            i_dir = self.download_images(input('SlideShare full URL (including "http://"): '))
        if filename:
            self.create_pdf(i_dir, filename + '.pdf')
        else:
            self.create_pdf(i_dir, i_dir + '.pdf')

    @staticmethod
    def download_images(page_url):
        html = urlopen(page_url).read()
        soup = BeautifulSoup(html, 'html.parser')
        images = soup.findAll('img', {'class': 'slide_image'})  # Parse out the slide images
        image_dir = soup.title.string.strip(' \t\r\n').lower().replace(' ', '-')  # Get name of the slide deck
        try:
            mkdir(image_dir)  # Create the folder for our images
        except FileExistsError:
            print("The directory '%s' already exists. Assuming PDF rebuild, continuing with existing contents...\n"
                  "Delete the directory to re-download the slide images." % image_dir)
            return image_dir
        chdir(image_dir)  # Change to image folder so we don't pollute starting folder
        for image in images:
            image_url = image.get('data-full').split('?')[0]
            with open(urlparse(image_url).path.split('/')[-1], "wb") as file:
                response = get(image_url)
                file.write(response.content)
        return image_dir

    def create_pdf(self, image_dir, filename):
        chdir(join(self.TOP_DIR, image_dir))
        files = next(walk(join(self.TOP_DIR, image_dir)))[2]
        with open(join(self.TOP_DIR, filename), "wb") as file:
            img2pdf.convert(*files, title=filename, outputstream=file)

if __name__ == "__main__":
    arguments = docopt(__doc__)
    ss = SlideShare()
    ss.get_slides(arguments['-u'], arguments['-f'])
