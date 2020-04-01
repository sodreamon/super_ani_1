import json

# json
with open("anime.json", "r", encoding="utf-8") as anime_json:
    data = anime_json.read()

anime_all = json.loads(data)['all']

with open("home_anime.json", "r", encoding="utf-8") as home_anime_json:
    data = home_anime_json.read()

home_anime_all = json.loads(data)['all']
days_animes = home_anime_all["animes"]
mon_animes = days_animes['mon']
tue_animes = days_animes['tue']
wed_animes = days_animes['wed']
thu_animes = days_animes['thu']
fri_animes = days_animes['fri']
sat_animes = days_animes['sat']
sun_animes = days_animes['sun']

