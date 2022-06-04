#!/usr/bin/python3
"""level 0  """


import requests
import sys

url = "http://158.69.76.135/level0.php"
id = "4291"

for i in range(0, 1024):
    data = {'id': id, 'holdthedoor': 'Submit'}
    r = requests.post(url, data=data)
