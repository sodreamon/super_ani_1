import json

# json
with open("anime.json", "r", encoding="utf-8") as anime_json:
    data = anime_json.read()

anime_all = json.loads(data)['all']
animes = anime_all['animes']
animes_title = []
for anime in animes:
    title = anime['anime_block_subject']
    animes_title.append(title)


# for anime in animes:
#     anime_info = {"link":anime[anime_link], "title":anime[anime_block_subject],
#     "thumbnail":anime[anime_block_thumbnail], "genre":anime[anime_block_genre], ""}
