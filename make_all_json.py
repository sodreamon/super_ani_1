import requests
import csv
import json
from collections import OrderedDict
from bs4 import BeautifulSoup

home_url = "https://ani24do.com"
all_anime_url = home_url+"/ani/search.php?query=%27%27"
test_url = "https://ani24do.com/ani/search.php?query=go"
test_url2 = "https://ani24do.com/ani/search.php?query=working"
test_url3 = "https://ani24do.com/ani/search.php?query=%EC%97%AD%EC%A0%84%EC%9E%AC%ED%8C%90"


def anime_1():
    paga_all = requests.get(all_anime_url)
    plane_page = paga_all.text
    soup = BeautifulSoup(plane_page, "html.parser")
    anime_blocks_box = soup.find("div", "ani_search_list_box")
    anime_blocks = anime_blocks_box.find_all("div", "ani_search_info_box")
    datas_all = []
    n = len(datas_all)
    for anime_block in anime_blocks:
        n = n + 1
        print(n)
        href = anime_block.find("a", "thumbnail")["href"]
        anime_block_thumbnail = anime_block.find(
            "a", "thumbnail").find("img")["src"]
        anime_block_subject = anime_block.find("a", "subject")["title"]
        print(f'{anime_block_subject}')
        anime_block_genre = anime_block.find("div", "genre")["title"]
        anime_inner_data = []
        anime_list_data = []
        anime_link = home_url + href
        anime_id_1 = href.replace('/ani_list/', '')
        anime_detail_id = anime_id_1.replace('.html', '')

        # anime_block_done = {"anime_link": anime_link, "anime_block_subject": anime_block_subject, "anime_block_thumbnail": anime_block_thumbnail,
        #                     "anime_block_genre": anime_block_genre, "anime_inner_data": anime_inner_data, "anime_list_data": anime_list_data}
        # datas_all.append(anime_block_done)
        page_all_2 = requests.get(anime_link)
        plane_page_2 = page_all_2.text
        soup2 = BeautifulSoup(plane_page_2, "html.parser")

    # 애니 설명
        if soup2.find("div", "ani_info") is not None:
            anime_data = soup2.find("div", "ani_info")
            anime_data_left = anime_data.find_all("div")[0]
            anime_data_left_image = anime_data_left.find("img")["src"]
            anime_data_right = anime_data.find_all("div")[1]
            anime_data_right_rating = anime_data_right.find(
                "span", "score_block_right").text
            anime_data_right_original = anime_data_right.find_all(
                "div", "info_line")[0].find_all("span")[1].text
            anime_data_right_original_story = anime_data_right.find_all(
                "div", "info_line")[1].find_all("span")[1].text
            anime_data_right_director = anime_data_right.find_all(
                "div", "info_line")[2].find_all("span")[1].text
            anime_data_right_script = anime_data_right.find_all(
                "div", "info_line")[3].find_all("span")[1].text
            anime_data_right_design = anime_data_right.find_all(
                "div", "info_line")[4].find_all("span")[1].text
            anime_data_right_music = anime_data_right.find_all(
                "div", "info_line")[5].find_all("span")[1].text
            anime_data_right_production_company = anime_data_right.find_all(
                "div", "info_line")[6].find_all("span")[1].text
            anime_data_right_genre = anime_data_right.find_all(
                "div", "info_line")[7].find_all("span")[1].text
            anime_data_right_class = anime_data_right.find_all(
                "div", "info_line")[8].find_all("span")[1].text
            anime_data_right_country = anime_data_right.find_all(
                "div", "info_line")[9].find_all("span")[1].text
            anime_data_right_date = anime_data_right.find_all(
                "div", "info_line")[10].find_all("span")[1].text
            anime_data_right_age = anime_data_right.find_all(
                "div", "info_line")[11].find_all("span")[1].text
            anime_data_right_total_count = anime_data_right.find_all(
                "div", "info_line")[12].find_all("span")[1].text
            anime_data_done = {
                "anime_data_image": anime_data_left_image,
                "anime_data_rating": anime_data_right_rating,
                "anime_data_original": anime_data_right_original,
                "anime_data_original_story": anime_data_right_original_story,
                "anime_data_director": anime_data_right_director,
                "anime_data_script": anime_data_right_script,
                "anime_data_design": anime_data_right_design,
                "anime_data_music": anime_data_right_music,
                "anime_data_production_company": anime_data_right_production_company,
                "anime_data_genre": anime_data_right_genre,
                "anime_data_class": anime_data_right_class,
                "anime_data_country": anime_data_right_country,
                "anime_data_date": anime_data_right_date,
                "anime_data_age": anime_data_right_age,
                "anime_data_total_count": anime_data_right_total_count
            }
            anime_inner_data.append(anime_data_done)

    # 애니 리스트
        anime_list = soup2.find("div", "ani_video_list")
        anime_ones = anime_list.find_all("a")
        for anime_one in anime_ones:
            if 'ani24show' in anime_one["href"]:
                anime_one["href"].replace("//ani24show.com", "")
            else:
                anime_one_href = anime_one["href"]
            anime_one_link = home_url + anime_one_href
            anime_one_thumbnail = anime_one.find(
                "div", "ani_video_thumbnail").find("img")["src"]
            anime_one_title = anime_one.find(
                "div", "ani_upload_info").find("div", "subject").text
            anime_one_updated_date = anime_one.find(
                "div", "ani_upload_info").find("div", "date").text
            # 애니
            anime_id = anime_one_href.replace("/ani_view/", "")
            anime_id = anime_id.replace(".html", "")
            anime_id = int(anime_id)
            if 1 <= anime_id <= 4000:
                anime_view_link = "https://new2.filegroupa.com/files/0/1~4000/id_" + \
                    str(anime_id)+".mp4"
            elif 4001 <= anime_id <= 8000:
                anime_view_link = "https://new1.filegroupa.com/files/0/4001~8000/id_" + \
                    str(anime_id)+".mp4"
            elif 8001 <= anime_id <= 12000:
                anime_view_link = "https://new1.filegroupa.com/files/1/8001~12000/id_" + \
                    str(anime_id)+".mp4"
            elif 12001 <= anime_id <= 16000:
                anime_view_link = "https://new1.filegroupa.com/files/1/12001~16000/id_" + \
                    str(anime_id)+".mp4"
            elif 16001 <= anime_id <= 20000:
                anime_view_link = "https://new1.filegroupa.com/files/2/16001~20000/id_" + \
                    str(anime_id)+".mp4"
            elif 20001 <= anime_id <= 24000:
                anime_view_link = "https://new2.filegroupa.com/files/2/20001~24000/id_" + \
                    str(anime_id)+".mp4"
            elif 24001 <= anime_id <= 28000:
                anime_view_link = "https://new2.filegroupa.com/files/2/24001~28000/id_" + \
                    str(anime_id)+".mp4"
            elif 28001 <= anime_id <= 32000:
                anime_view_link = "https://new2.filegroupa.com/files/1/28001~32000/id_" + \
                    str(anime_id)+".mp4"
            elif 32001 <= anime_id <= 36000:
                anime_view_link = "https://new2.filegroupa.com/files/1/32001~36000/id_" + \
                    str(anime_id)+".mp4"
            elif 36001 <= anime_id <= 38765:
                anime_view_link = "https://new1.filegroupa.com/files/0/new/id_" + \
                    str(anime_id)+".mp4"
            elif 38766 <= anime_id <= 40399:
                anime_view_link = "https://new0.filegroupa.com/files/0/new/id_" + \
                    str(anime_id)+".mp4"
            elif 40400 <= anime_id:
                anime_view_link = "https://sorotoa.com/l/" + \
                    str(anime_id)+".jpg"
            anime_one_data_dir = {
                "anime_one_id": str(anime_id), "anime_one_thumbnail": anime_one_thumbnail, "anime_one_title": anime_one_title, "anime_one_updated_date": anime_one_updated_date, "anime_view_link": anime_view_link
            }
            anime_list_data.append(anime_one_data_dir)

            # data = {
            #     "anime_block_subject": anime_block_subject,
            #     "anime_block_thumbnail": anime_block_thumbnail,
            #     "anime_block_genre": anime_block_genre,
            #     "anime_data_image": anime_data_left_image,
            #     "anime_data_rating": anime_data_right_rating,
            #     "anime_data_original": anime_data_right_original,
            #     "anime_data_original_story": anime_data_right_original_story,
            #     "anime_data_director": anime_data_right_director,
            #     "anime_data_script": anime_data_right_script,
            #     "anime_data_design": anime_data_right_design,
            #     "anime_data_music": anime_data_right_music,
            #     "anime_data_production_company": anime_data_right_production_company,
            #     "anime_data_genre": anime_data_right_genre,
            #     "anime_data_class": anime_data_right_class,
            #     "anime_data_country": anime_data_right_country,
            #     "anime_data_date": anime_data_right_date,
            #     "anime_data_age": anime_data_right_age,
            #     "anime_data_total_count": anime_data_right_total_count,
            #     "anime_one_link": anime_one_link,
            #     "anime_one_thumbnail": anime_one_thumbnail,
            #     "anime_one_title": anime_one_title,
            #     "anime_one_updated_date": anime_one_updated_date,
            #     "anime_view_link": anime_view_link
            # }
            # datas_all.append(data)
        # return anime_list_data
        anime_block_done = {"anime_id": str(anime_detail_id), "anime_block_subject": anime_block_subject, "anime_block_thumbnail": anime_block_thumbnail,
                            "anime_block_genre": anime_block_genre, "anime_inner_data": anime_data_done, "anime_list_data": anime_list_data}
        datas_all.append(anime_block_done)
    return datas_all


for_json = {
    "animes": anime_1()
}


file_data = OrderedDict()

file_data["all"] = for_json

with open('anime.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


# def save_to_file(animes):
#     file = open('data_all.csv', mode='w', newline='')
#     writer = csv.writer(file)
#     writer.writerow(['subject', 'thumbnail', 'genre', 'image', 'rating', 'original', 'original_story', 'director', 'script', 'design', 'music',
#                      'company', 'genre', 'class', 'country', 'date', 'age', 'total_count', 'link', 'one_thumbnail', 'one_title', 'updated_date', 'video'])
#     for anime in animes:
#         writer.writerow(list(anime.values()))
#     return
