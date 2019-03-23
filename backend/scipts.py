import re

import requests
from bs4 import BeautifulSoup


def pars():
    url = "https://boardgamegeek.com/collection/user/PegaKrakow?own=1&subtype=boardgame&ff=1&fbclid=IwAR3fTr8OcrF1hyQIPi-El1nMRPQy5qW-fC-bqp0bS3b84rVcCyYALkhJ1C4"
    req = requests.get(url)
    text = req.text
    html = BeautifulSoup(text, 'html.parser')
    tds = html.findAll("a", href=re.compile("^\/boardgame\/[0-9]"))

    for href in tds:
        link = href['href']
        name = href.text
        url = "https://boardgamegeek.com" + link
        req = requests.get(url)
        text = req.text
        html = BeautifulSoup(text, 'html.parser')

        images = html.find("meta", property="og:image")
        print("hi")
        print(images["content"])

        img_data = requests.get(str(images["content"])).content
        with open('resources/game_photos/' + name.lower() + '.jpg', 'wb+') as handler:
            handler.write(img_data)


pars()
