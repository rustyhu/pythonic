# fly scratch

import requests

url = "http://xkcd.com/info.0.json"
page = requests.get(url)
if page.status_code != 200:
    print(f"unexpected response status code - {page.status_code}")

comicinfo = page.json()
desc: str = comicinfo["alt"]
title: str = comicinfo["title"]
img = requests.get(comicinfo["img"])
fname = title + ".png"

print(f"Get today's comic - {title}, caption: {desc}")
print(f"Write as [{fname}]")
with open(fname, 'wb+') as f:
    f.write(img.content)
