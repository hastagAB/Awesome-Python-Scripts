#!/usr/bin/python3
# Created by Sam Ebison ( https://github.com/ebsa491 )
# If you have found any important bug or vulnerability,
# contact me pls, I love learning ( email: ebsa491@gmail.com )

"""
Some urls are really long, you should short them with this script!
This script uses ``requests`` for sending HTTP requests and
uses ``BeautifulSoup`` from ``bs4`` for web scraping.
"""

import sys
import argparse
import requests
from bs4 import BeautifulSoup

RED_COLOR = "\033[1;31m"
GREEN_COLOR = "\033[1;32m"
NO_COLOR = "\033[0m"

API_URL = "https://www.shorturl.at/shortener.php"
API_PARAM = "u"
# Creadit => www.shorturl.at

class API:
    """A class for managing the API results."""

    def __init__(self):
        """ __init__ """
        self.__long_url = ""

    def set_url(self, url):
        """This method sets the self.__long_url = url (self.__long_url setter)."""
        self.__long_url = url

    def get_short_url(self):
        """This method returns the self.__short_url (self.__short_url getter)."""
        return self.__short_url

    def request_short_url(self):
        """This method sends a POST request to the API and returns the result text."""

        prarams = {API_PARAM: self.__long_url}

        try:
            result = requests.post(API_URL, data = prarams)
        except ConnectionError as err:
            return -1, err

        return 1, result.text

    def extract_data_from_html(self, html_page):
        """
        This method parses the html text
        and finds the input tag with id=\'shortenurl\' for shorten url.
        """

        # Response sample =>
        # <input id="shortenurl" onclick="this.select();" type="text" value="shorturl.at/SOME_CODE"/>

        soup = BeautifulSoup(html_page, 'html.parser')
        input_tag = soup.find("input", attrs={"id": "shortenurl"})

        try:
            self.__short_url = input_tag.attrs["value"]
            return 1
        except:
            return -1

def main():
    """The main function of the program."""

    if args.url == '' or args.url is None:
        args.url = input("Enter the url> ")

    api_manager = API()

    api_manager.set_url(args.url)
    response_stauts, result = api_manager.request_short_url() # Sends the request to the API

    if response_stauts == -1:
        # Can't connect to the API

        print(f"[{RED_COLOR}-{NO_COLOR}] Error in connecting to the API server...")
        ans = input("Do you want to know the error? [Y/n] ") # For more information about thr error
        if ans.lower() != 'n':
            print(result)

        sys.exit(1)
        return

    if api_manager.extract_data_from_html(result) == -1:
        # Can't parse the html_page

        print(f"[{RED_COLOR}-{NO_COLOR}] Error in parsing the response...")
        sys.exit(1)
        return

    print("=========================")
    print(GREEN_COLOR + api_manager.get_short_url() + NO_COLOR)
    print("=========================")

    sys.exit(0)
    return

if __name__ == '__main__':
    global args # The program arguments

    parser = argparse.ArgumentParser(description="URL Shortener")

    # -u | --url URL
    parser.add_argument(
        '-u',
        '--url',
        metavar='url',
        type=str,
        default='',
        help='the URL'
    )

    args = parser.parse_args()

    main()
