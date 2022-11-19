from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pybadges
from requests_html import HTMLSession
from requests_html import HTML
# from enum import Enum
import json
import time


app = FastAPI()


website_text = {
    "clubdam-dx-100points": "DAM-DX-100Points",
    "clubdam-dx-g-100points": "DAM-DX-G-100Points",
    "clubdam-dx-g-100points-plus": "DAM-DX-G-100Points+",
}


# """
# 採点機種クラス
# """
# class ScoringModel(Enum):
#     DX = 1
#     DX_G = 2
#     AI = 3


def get_clubdam_100points(user_name, scoring_model, including_bonus=True):
    """
    100点曲数をスクレイピングする関数

    Args:
        user_name (str): ユーザ名
        scoring_model (ScoringModel): 採点機種
        including_bonus (bool): ボーナス込みか否か

    Returns:
        [int, str]: Return [count, color]
    
    """

    if scoring_model == "DX":
        base_url = "https://clubdam.info/history/load_content_div/{}/date/desc".format(user_name)
    elif scoring_model == "DX_G":
        base_url = "https://dx-g.clubdam.info/history/load_content_div/{}/scoringDateTime/desc".format(user_name)
    page_index = 1
    highscore_by_song = {}
    raw_song_data_list = []
    st = time.time()
    while True:
        url = "{}/{}".format(base_url, page_index)
        req = HTMLSession().get(url)
        print("requests")
        raw_song_data = req.html.find("tbody")
        if len(raw_song_data) == 0: break
        raw_song_data_list.extend(raw_song_data)
        page_index += 1
        if page_index >= 5:
            break
    sf = time.time()
    print(sf-st)


    for raw_song_data in raw_song_data_list:
        song_data = json.loads(raw_song_data.attrs["data-object_data"])
        request_no = song_data["requestNo"]
        song_points = float(song_data["totalPoint"]) if including_bonus else float(song_data["rawPoint"])
        if highscore_by_song.get(request_no) == None: highscore_by_song[request_no] = 0.0
        highscore_by_song[request_no] = max(highscore_by_song[request_no], song_points)

    count = 0
    for points in highscore_by_song.values():
        if int(points) == 100:
            count += 1
    
    if (0 == count):
        color = "#FFFFFF"
    elif (1 <= count < 4):
        color = "#FFCCDC"
    elif (4 <= count < 10):
        color = "#FFBBFF"
    elif (10 <= count < 50):
        color = "#CCCCFF"
    elif (50 <= count < 100):
        color = "#ABFFFF"
    elif (100 <= count < 500):
        color = "#CCFFCC"
    elif (500 <= count < 1000):
        color = "#FFF550"
    elif (1000 <= count):
        color = "#FFCC11"
    else:
        color = "#FFFFFF"
    return [count, color]


def get_info(website, user_name):
    website = website.lower()
    if website == "clubdam-dx-100points":
        return get_clubdam_100points(user_name, "DX")
    elif website == "clubdam-dx-g-100points":
        return get_clubdam_100points(user_name, "DX_G", True)
    elif website == "clubdam-dx-g-100points-plus":
        return get_clubdam_100points(user_name, "DX_G", False)
    else:
        raise ValueError("wrong platform website name")


@app.get("/")
def index():
    return "This API is working."


@app.get("/{website}/{user_name}")
def get_badge(website, user_name):
    info = get_info(website, user_name)
    rating, color = str(info[0]), str(info[1])
    text = website_text[website.lower()]
    badge = pybadges.badge(left_text=text, right_text=rating, right_color=color)
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')