from flask import Flask, render_template, request, redirect, url_for
import datetime
import json

# json
with open("anime.json", "r", encoding="utf-8") as anime_json:
    data = anime_json.read()

anime_all = json.loads(data)['all']
animes = anime_all['animes']
animes_title = []

with open("home_anime.json", "r", encoding="utf-8") as home_anime_json:
    data = home_anime_json.read()

# home
home_anime_all = json.loads(data)['all']
days_animes = home_anime_all["animes"]
mon_animes = days_animes['mon']
tue_animes = days_animes['tue']
wed_animes = days_animes['wed']
thu_animes = days_animes['thu']
fri_animes = days_animes['fri']
sat_animes = days_animes['sat']
sun_animes = days_animes['sun']

# search
for anime in animes:
    title = anime['anime_block_subject']
    animes_title.append(title)

# flask
app = Flask(__name__)

today = datetime.date.today()
weekday = today.weekday()


@app.route('/layout')
def layout():
    return render_template('layout.html', weekday=weekday)


@app.route('/')
def hello_world():
    mon = mon_animes
    tue = tue_animes
    wed = wed_animes
    thu = thu_animes
    fri = fri_animes
    sat = sat_animes
    sun = sun_animes

    return render_template('home.html', mon=mon, tue=tue,
                           wed=wed,
                           thu=thu,
                           fri=fri,
                           sat=sat,
                           sun=sun)


@app.route('/word', methods=['POST', 'GET'])
def word():
    if request.method == 'POST':
        word = request.form['name_search']
        return redirect(url_for('search', word=word))
    else:
        word = request.args.get('name_search')
        return redirect(url_for('search', word=word))


@app.route('/search/<word>')
def search(word):
    searched_anime = []
    for title in animes_title:
        if word.lower() in title.lower():
            for anime in animes:
                if anime['anime_block_subject'] == title:
                    searched_anime.append(anime)
    count_anime = len(searched_anime)

    return render_template('search.html', word=word, animes=searched_anime, count=count_anime)


@app.route('/new')
def new_20():
    return render_template('new.html')


@app.route('/genre')
def genre_20():
    return render_template('genre.html')


@app.route('/quarter')
def quarter_20():
    return render_template('quarter.html')


@app.route('/year')
def year_20():
    return render_template('year.html')


@app.route('/finished')
def finished():
    return render_template('finished.html')


@app.route('/detail/<anime_id>')
def detail(anime_id):
    anime_data = []
    anime_list = []
    for anime in animes:
        if anime['anime_id'] == anime_id:
            anime_inner_data = anime['anime_inner_data']
            anime_title = anime['anime_block_subject']
            anime_inner_data['anime_block_subject'] = anime_title
            anime_list_data = anime['anime_list_data']
            anime_data.append(anime_inner_data)
            anime_list.append(anime_list_data)
    return render_template('detail.html', anime_data=anime_data, anime_list=anime_list)


@app.route('/anime_link/<anime_number>')
def anime_link(anime_number):
    animes_video_data = []
    next_anime = None
    pre_anime = None
    anime_big_number = None
    for anime in animes:
        anime_list = anime['anime_list_data']
        for anime_data in anime_list:
            anime_one_ids = anime_data['anime_one_id']
            if anime_one_ids == int(anime_number):
                animes_video_data.append(anime_data)
                anime_list_num = anime_list.index(anime_data)
                print(len(anime_list))

                # 다음
                if anime_list_num == 0:
                    next_video_id = anime_list_num
                else:
                    next_video_id = anime_list_num - 1
                next_video = anime_list[next_video_id]

                next_anime = next_video

                # 이전
                if anime_list_num == len(anime_list)-1:
                    pre_video_id = anime_list_num
                else:
                    pre_video_id = anime_list_num + 1
                pre_video = anime_list[pre_video_id]
                pre_anime = pre_video

                # go to 리스트
                anime_big_number = anime['anime_id']

    return render_template('anime_link.html', animes_video_data=animes_video_data, next_anime=next_anime, pre_anime=pre_anime, anime_big_number=anime_big_number)


if __name__ == '__main__':
    app.run()
