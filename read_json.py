import json
from copy_page import home_copy

with open("anime.json", "r", encoding="utf-8") as myfile:
    data = myfile.read()

data = json.loads(data)
all = data["all"]
animes = all["animes"]
anime_1 = animes[0]
anime_1_info = anime_1["anime_block_subject"]


home_copied_data = home_copy()


def test():
    if home_copied_data['mon'] == '헤야캠프':
        return "ok"


print(home_copied_data['mon'])
