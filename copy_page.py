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

# 홈 카피


def home_copy():
    url = "https://ani24do.com"
    page_all = requests.get(url).text
    soup = BeautifulSoup(page_all, "html.parser")
    day_boxes = soup.find_all("div", "main_ani_day_list")
    # 월
    mon_box = day_boxes[0]
    mon_animes = mon_box.find_all("a", "main_ani_layout")
    mon_titles = []
    for mon_anime in mon_animes:
        title = mon_anime.find("div", "subject")["title"]
        title_dict = {'title': title}
        mon_titles.append(title_dict)
    # 화
    tue_box = day_boxes[1]
    tue_animes = tue_box.find_all("a", "main_ani_layout")
    tue_titles = []
    for tue_anime in tue_animes:
        title = tue_anime.find("div", "subject")["title"]
        title_dict = {'title': title}
        tue_titles.append(title_dict)
    # 수
    wed_box = day_boxes[2]
    wed_animes = wed_box.find_all("a", "main_ani_layout")
    wed_titles = []
    for wed_anime in wed_animes:
        title = wed_anime.find("div", "subject")["title"]
        title_dict = {'title': title}
        wed_titles.append(title_dict)
    # 목
    thu_box = day_boxes[3]
    thu_animes = thu_box.find_all("a", "main_ani_layout")
    thu_titles = []
    for thu_anime in thu_animes:
        title = thu_anime.find("div", "subject")["title"]
        title_dict = {'title': title}
        thu_titles.append(title_dict)
    # 금
    fri_box = day_boxes[4]
    fri_animes = fri_box.find_all("a", "main_ani_layout")
    fri_titles = []
    for fri_anime in fri_animes:
        title = fri_anime.find("div", "subject")["title"]
        title_dict = {'title': title}
        fri_titles.append(title_dict)
    # 토
    sat_box = day_boxes[5]
    sat_animes = sat_box.find_all("a", "main_ani_layout")
    sat_titles = []
    for sat_anime in sat_animes:
        title = sat_anime.find("div", "subject")["title"]
        title_dict = {'title': title}
        sat_titles.append(title_dict)
    # 일
    sun_box = day_boxes[6]
    sun_animes = sun_box.find_all("a", "main_ani_layout")
    sun_titles = []
    for sun_anime in sun_animes:
        title = sun_anime.find("div", "subject")["title"]
        title_dict = {'title': title}
        sun_titles.append(title_dict)
    days_titles = {"mon": mon_titles,
                   "tue": tue_titles,
                   "wed": wed_titles,
                   "thu": thu_titles,
                   "fri": fri_titles,
                   "sat": sat_titles,
                   "sun": sun_titles}
    days_titles_ver_2 = mon_titles + tue_titles + wed_titles + \
        thu_titles + fri_titles + sat_titles + sun_titles
    # JOSN에서 찾기
    animes_title = []
    for anime_pre in animes:
        title = anime_pre['anime_block_subject']
        animes_title.append(title)
        # 요일 전체
    infos = []
    home_titles = []
    for title_dict in days_titles_ver_2:
        title = title_dict['title']
        if title in animes_title:
            for anime in animes:
                json_anime_title = anime['anime_block_subject']
                if json_anime_title == title:
                    anime_title = anime['anime_block_subject']
                    home_titles.append(anime_title)
                    anime_thumb = anime['anime_block_thumbnail']
                    anime_genre = anime['anime_block_genre']
                    anime_data = anime['anime_inner_data']
                    anime_id = anime['anime_id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    infos.append(anime_info)

    # 월요일
    mon_infos = []
    for title_dict in mon_titles:
        title = title_dict['title']
        if title in home_titles:
            for info in infos:
                info_title = info['title']
                if info_title == title:
                    anime_title = info['title']
                    anime_thumb = info['thumbnail']
                    anime_genre = info['genre']
                    anime_data = info['data']
                    anime_id = info['id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    mon_infos.append(anime_info)
        # 화요일
    tue_infos = []
    for title_dict in tue_titles:
        title = title_dict['title']
        if title in home_titles:
            for info in infos:
                info_title = info['title']
                if info_title == title:
                    anime_title = info['title']
                    anime_thumb = info['thumbnail']
                    anime_genre = info['genre']
                    anime_data = info['data']
                    anime_id = info['id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    tue_infos.append(anime_info)
        # 수요일
    wed_infos = []
    for title_dict in wed_titles:
        title = title_dict['title']
        if title in home_titles:
            for info in infos:
                info_title = info['title']
                if info_title == title:
                    anime_title = info['title']
                    anime_thumb = info['thumbnail']
                    anime_genre = info['genre']
                    anime_data = info['data']
                    anime_id = info['id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    wed_infos.append(anime_info)
        # 목요일
    thu_infos = []
    for title_dict in thu_titles:
        title = title_dict['title']
        if title in home_titles:
            for info in infos:
                info_title = info['title']
                if info_title == title:
                    anime_title = info['title']
                    anime_thumb = info['thumbnail']
                    anime_genre = info['genre']
                    anime_data = info['data']
                    anime_id = info['id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    thu_infos.append(anime_info)
        # 금요일
    fri_infos = []
    for title_dict in fri_titles:
        title = title_dict['title']
        if title in home_titles:
            for info in infos:
                info_title = info['title']
                if info_title == title:
                    anime_title = info['title']
                    anime_thumb = info['thumbnail']
                    anime_genre = info['genre']
                    anime_data = info['data']
                    anime_id = info['id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    fri_infos.append(anime_info)
        # 토요일
    sat_infos = []
    for title_dict in sat_titles:
        title = title_dict['title']
        if title in home_titles:
            for info in infos:
                info_title = info['title']
                if info_title == title:
                    anime_title = info['title']
                    anime_thumb = info['thumbnail']
                    anime_genre = info['genre']
                    anime_data = info['data']
                    anime_id = info['id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    sat_infos.append(anime_info)
        # 일요일
    sun_infos = []
    for title_dict in sun_titles:
        title = title_dict['title']
        if title in home_titles:
            for info in infos:
                info_title = info['title']
                if info_title == title:
                    anime_title = info['title']
                    anime_thumb = info['thumbnail']
                    anime_genre = info['genre']
                    anime_data = info['data']
                    anime_id = info['id']
                    anime_info = {'title': anime_title,
                                  'thumbnail': anime_thumb,
                                  'genre': anime_genre,
                                  'data': anime_data,
                                  'id': anime_id}
                    sun_infos.append(anime_info)
    home_animes = {'mon': mon_infos,
                   'tue': tue_infos,
                   'wed': wed_infos,
                   'thu': thu_infos,
                   'fri': fri_infos,
                   'sat': sat_infos,
                   'sun': sun_infos}
    return home_animes


for_json = {
    "animes": home_copy()
}


file_data = OrderedDict()

file_data["all"] = for_json

with open('home_anime.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
