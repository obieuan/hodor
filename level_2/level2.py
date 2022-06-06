#!/usr/bin/python3
"""level 0  """

import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level2.php"
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
              "Gecko/20100101 Firefox/64.0")
header = {
    "User-Agent": user_agent,
    "referer": url
}
datos = {
    "id": "4291",
    "holdthedoor": "holdthedoor",
    "key": ""
}
contador = 4080

if __name__ == "__main__":
    for i in range(0, contador):
        session = requests.session()
        page = session.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        hidden_value = soup.find("form", {"method": "post"})
        hidden_value = hidden_value.find("input", {"type": "hidden"})
        datos["key"] = hidden_value["value"]

        session.post(url, data=datos)
