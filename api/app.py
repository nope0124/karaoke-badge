from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pybadges
import requests

# from enum import Enum
import json


app = FastAPI()


# DX or DX_G or AI
# charts or points
# score
# including bonus


# """
# 採点機種クラス
# """
# class ScoringModel(Enum):
#     DX = 1
#     DX_G = 2
#     AI = 3


get_color = {
    "countRaw100": "#FFCC11",
    "countRawOver99": "#FFF550",
    "countRawOver98": "#CCFFCC",
    "countRawOver95": "#ABFFFF",
    "countRawOver90": "#CCCCFF",
    "countRawOver85": "#FFBBFF",
    "countRawOver80": "#FFCCDC",
    "count100": "#FFCC11",
    "countOver99": "#FFF550",
    "countOver98": "#CCFFCC",
    "countOver95": "#ABFFFF",
    "countOver90": "#CCCCFF",
    "countOver85": "#FFBBFF",
    "countOver80": "#FFCCDC",
    "countChart500": "#FFCC11",
    "countChart499": "#FFCC11",
    "countChart498": "#FFF550",
    "countChart497": "#CCFFCC",
    "countChart495": "#ABFFFF",
    "countChart490": "#CCCCFF",
}

website = {
    "clubdam-dx-g": "DX-G",
    "countRaw100": "100",
    "countRawOver99": "99",
    "countRawOver98": "98",
    "countRawOver95": "95",
    "countRawOver90": "90",
    "countRawOver85": "85",
    "countRawOver80": "80",
    "count100": "100",
    "countOver99": "99",
    "countOver98": "98",
    "countOver95": "95",
    "countOver90": "90",
    "countOver85": "85",
    "countOver80": "80",
    "countChart500": "500",
    "countChart499": "499",
    "countChart498": "498",
    "countChart497": "497",
    "countChart495": "495",
    "countChart490": "490",
    "rawPoint": "RawPoints",
    "totalPoint": "Points",
    "chartTotal": "Charts", 
}



def get_info(scoring_model, user_name, evaluation, score_text):
    
    if scoring_model == "clubdam-dx-g":
        url = "https://seimitsukensaku-app.onrender.com/api/v1/{}/counts".format(user_name)
    req_get = requests.get(url)
    if req_get.status_code != 200:
        print("Wrong platform website name")
        return [0, "#000000"]
    score = req_get.json()["result"][evaluation][score_text]
    color = get_color[score_text]
    print(req_get.json()["result"][evaluation])
    print(score, color)
    if score < 1:
        print("A badge with a score of 0 cannot be displayed")
        return [0, "#000000"]
    return [score, color]


@app.get("/")
def index():
    return "This API is working."


@app.get("/{scoring_model}/{user_name}/{evaluation}/{score_text}")
def get_badge(scoring_model, user_name, evaluation, score_text):
    info = get_info(scoring_model, user_name, evaluation, score_text)
    # if info == "A badge with a score of 0 cannot be displayed":
    #     return
    score, color = str(info[0]), str(info[1])
    text = "{}-{}{}".format(website[scoring_model], website[score_text], website[evaluation])
    badge = pybadges.badge(left_text=text, right_text=score, right_color=color)
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')