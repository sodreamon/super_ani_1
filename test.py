import requests
import json
from bs4 import BeautifulSoup
from collections import OrderedDict

# JSON 영역

with open("anime.json", "r", encoding="utf-8") as myfile:
    data = myfile.read()

data = json.loads(data)
all = data["all"]
animes = all["animes"]


def new_20():
    url = "https://ani24do.com/ani/top10.html"
    page_all = requests.get(url).text
    soup = BeautifulSoup(page_all, "html.parser")
    anime_boxes = soup.find_all("a", "top_info")

    for anime_box in anime_boxes:
        a = anime_box.find('div', 'ani_info_right')
        b = a.find('div', 'subject')
        c = b.text
        for anime in animes:
            if anime['anime_block_subject'] == c:
                print(anime['anime_block_subject'])


new_20()
