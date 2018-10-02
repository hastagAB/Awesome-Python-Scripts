#!/usr/bin/env python3

import hashlib
import os
import requests
import glob
import argparse

from os.path import expanduser

FILE_TYPES = ["*.mp4", "*.avi", "*.mkv"]

class ManualError(Exception):
    def __init__(self, args):
        self.args = args
    def display(self):
        print(''.join(self.args))

def get_hash(filename):
    """
    The hash is composed by taking the first and the last 64kb of the video file,
    putting all together and generating a md5 of the resulting data (128kb).
    """
    read_size = 64 * 1024
    with open(filename, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()

class SubDownloader:
    def __init__(self):
        self.file_types = FILE_TYPES

    def download(self, filename):
        """
        This API: http://thesubdb.com/api/  is used in a nutshell
        """
        try:
            splitted = os.path.splitext(filename)
            print()
            print("=== Trying to fetch subtitle for : {} ".format(filename))
            headers = {'User-Agent': 'SubDB/1.0 (paradoxical-sub/1.0; https://github.com/NISH1001/subtitle-downloader)'}
            url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(filename) + "&language=en"

            # streaming is enabled for raw bytes
            #response = requests.get(url, headers=headers, stream=True)

            response = requests.get(url, headers=headers)

            if(response.status_code != 200):
                raise ManualError("*** Error downloading subtitle for {} ***".format(filename))

            with open(splitted[0] + ".srt", "w") as sub:
                """
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        sub.write(response.raw.data)
                """
                sub.write(response.text)
        except ManualError as merr:
            merr.display()
            return
        except KeyboardInterrupt:
            print("Cancelling downloads...")
            return
        except:
            print("Error downloading subtitle for {}".format(filename))
            return

    def get_files(self, directory, file_types):
        if not directory:
            directory = os.getcwd()
        os.chdir(directory)
        files = []
        for extension in file_types:
            files.extend(glob.glob(extension))
        return files

    def download_from_directory(self, directory=""):
        files = self.get_files(directory, FILE_TYPES)
        for f in files:
            self.download(f)

def cli():
    parser = argparse.ArgumentParser(description="A simple script to download english subtitles for videos")
    parser.add_argument("-c", "--current",
            help = "download all from current directory",
            action = "store_true"
            )

    parser.add_argument("-d", "--dir",
            help = "download from the directory provided"
            )

    """
    parser.add_argument("-f", "--file",
            help = "download subtile for the filename"
            )
    """

    args = parser.parse_args()

    downloader = SubDownloader()
    if args.current and not args.dir:
        downloader.download_from_directory()
    elif args.dir and not args.current:
        downloader.download_from_directory(args.dir)
    else:
        print("LOL! type --help")

def test():
    downloader = SubDownloader()
    #downloader.download_from_directory(directory=expanduser("~/Videos/youtube/"))
    downloader.download_from_directory()

def main():
    cli()


if __name__ == "__main__":
main()
