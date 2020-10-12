import sys

import requests

from src.util import *


def show_info():

    url = str(input("Enter a stream URL: "))

    fetch_from_url(url)
    

def fetch_from_url(url):

    #Temporary user agent
    HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
 
    try:
        req = requests.get(url, headers=HEADER, timeout=5)

    except Exception:
        print("Connection timeout")
        sys.exit()

    if req.status_code != 200:
        print("An error occured!")
        sys.exit()

    text_list = req.text.split('\n')[380:455]

    #Delete null element and escape charactors and space in text_list
    text_list = tuple(map(lambda s: s.replace(' ', ''), text_list))
    text_list = tuple(map(lambda s: s.replace('\r', ''), text_list))
    text_list = tuple(map(lambda s: s.replace(' ', ''), text_list))

