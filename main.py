import flask
import pybadges
import signal
import asyncio
import time
# from data import get_info
from flask import request
from requests_html import AsyncHTMLSession

app = flask.Flask(__name__)
app.url_map.strict_slashes = False


website_text = {
    "clubdam-dx-point": "DAM-DX-Point",
    "clubdam-dx-chart": "DAM-DX-Chart",
    "clubdam-dx-ranking": "DAM-DX-Ranking",
    "clubdam-dx-g-point": "DAM-DX-G-Point",
    "clubdam-dx-g-chart": "DAM-DX-G-Chart",
    "clubdam-dx-g-ranking": "DAM-DX-G-Ranking",
    "clubdam-dx-g-ranking+": "DAM-DX-G-Ranking+",
}

async def get_clubdam_dx_point(user):
    asession = AsyncHTMLSession()
    url = f"https://clubdam.info/user/{user}/song"
    # セッション開始
    r = await asession.get(url)
    await r.html.arender()

    # スクレイピング
    point = float(r.html.find("#data_1")[0].find(".table_point", first=True).text)

    y = point
    if (y < 80.000):
        col = "#FFFFFF"
    elif (80.000 <= y and y < 85.000):
        col = "#FFCCDC"
    elif (85.000 <= y and y < 90.000):
        col = "#FFBBFF"
    elif (90.000 <= y and y < 95.000):
        col = "#CCCCFF"
    elif (95.000 <= y and y < 98.000):
        col = "#ABFFFF"
    elif (98.000 <= y and y < 99.000):
        col = "#CCFFCC"
    elif (99.000 <= y and y < 100.000):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (100.000 <= y):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    return ["{:.3f}".format(y), col]


async def get_clubdam_dx_chart(user):
    asession = AsyncHTMLSession()
    url = f"https://clubdam.info/user/{user}/song/index/max_radarChartTotal/desc"
    # セッション開始
    r = await asession.get(url)
    await r.html.arender()

    # スクレイピング
    chart = int(r.html.find("#data_1")[0].find(".table_chart_total", first=True).text)

    y = chart
    if (y < 320):
        col = "#FFFFFF"
    elif (320 <= y and y < 370):
        col = "#FFCCDC"
    elif (370 <= y and y < 420):
        col = "#FFBBFF"
    elif (420 <= y and y < 450):
        col = "#CCCCFF"
    elif (450 <= y and y < 470):
        col = "#ABFFFF"
    elif (470 <= y and y < 480):
        col = "#CCFFCC"
    elif (480 <= y and y < 490):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (490 <= y):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    return [y, col]



async def get_clubdam_dx_ranking(user):
    asession = AsyncHTMLSession()
    url = f"https://clubdam.info/user/{user}/others"
    # セッション開始
    r = await asession.get(url)
    await r.html.arender()

    # スクレイピング
    point_index_text = r.html.find(".highcharts-axis-labels")[0].find("text")
    point_times_text = r.html.find(".highcharts-stack-labels")[0].find("text")
    
    point_index = []
    point_times = []
    for point in point_index_text:
        point_index.append(point.text)
    for point in point_times_text:
        point_times.append(int(point.text))
    idx = -1
    if "100" in point_index:
        idx = point_index.index("100")
    
    y = 0
    if idx != -1:
        y += point_times[idx]
    if (y == 0):
        col = "#FFFFFF"
    elif (1 <= y and y < 4):
        col = "#FFCCDC"
    elif (4 <= y and y < 10):
        col = "#FFBBFF"
    elif (10 <= y and y < 50):
        col = "#CCCCFF"
    elif (50 <= y and y < 100):
        col = "#ABFFFF"
    elif (100 <= y and y < 500):
        col = "#CCFFCC"
    elif (500 <= y and y < 1000):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (1000 <= y):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    return [y, col]





async def get_clubdam_dx_g_point(user):
    asession = AsyncHTMLSession()
    url = f"https://dx-g.clubdam.info/user/{user}/song"
    # セッション開始
    r = await asession.get(url)
    await r.html.arender()

    # スクレイピング
    point = float(r.html.find("#data_1")[0].find(".table_point", first=True).text)
    raw_point = float(r.html.find("#data_1")[0].find(".table_rawPoint", first=True).text)
    y = point
    if (y < 80.000):
        col = "#FFFFFF"
    elif (80.000 <= y and y < 85.000):
        col = "#FFCCDC"
    elif (85.000 <= y and y < 90.000):
        col = "#FFBBFF"
    elif (90.000 <= y and y < 95.000):
        col = "#CCCCFF"
    elif (95.000 <= y and y < 98.000):
        col = "#ABFFFF"
    elif (98.000 <= y and y < 99.000):
        col = "#CCFFCC"
    elif (99.000 <= y and y < 100.000):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (100.000 <= y and raw_point < 100.000):
        col = "#FFF550"
    elif (100.000 <= y and 100.000 <= raw_point):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    return ["{:.3f}".format(y), col]


async def get_clubdam_dx_g_chart(user):
    asession = AsyncHTMLSession()
    url = f"https://dx-g.clubdam.info/user/{user}/song/index/max_radarChartTotal/desc"
    # セッション開始
    r = await asession.get(url)
    await r.html.arender()

    # スクレイピング
    chart = int(r.html.find("#data_1")[0].find(".table_chart_total", first=True).text)

    y = chart
    if (y < 320):
        col = "#FFFFFF"
    elif (320 <= y and y < 370):
        col = "#FFCCDC"
    elif (370 <= y and y < 420):
        col = "#FFBBFF"
    elif (420 <= y and y < 450):
        col = "#CCCCFF"
    elif (450 <= y and y < 470):
        col = "#ABFFFF"
    elif (470 <= y and y < 480):
        col = "#CCFFCC"
    elif (480 <= y and y < 490):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (490 <= y):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    return [y, col]



async def get_clubdam_dx_g_ranking(user):
    asession = AsyncHTMLSession()
    url = f"https://dx-g.clubdam.info/user/{user}/others"
    # セッション開始
    r = await asession.get(url)
    await r.html.arender()

    # スクレイピング
    point_index_text = r.html.find(".highcharts-axis-labels")[0].find("text")
    point_times_text = r.html.find(".highcharts-stack-labels")[0].find("text")
    
    point_index = []
    point_times = []
    for point in point_index_text:
        point_index.append(point.text)
    for point in point_times_text:
        point_times.append(int(point.text))
    idx = -1
    idx_plus = -1
    if "100" in point_index:
        idx = point_index.index("100")
    if "100+" in point_index:
        idx_plus = point_index.index("100+")
    
    y = 0
    if idx != -1:
        y += point_times[idx]
    if idx_plus != -1:
        y += point_times[idx_plus]
    if (y == 0):
        col = "#FFFFFF"
    elif (1 <= y and y < 4):
        col = "#FFCCDC"
    elif (4 <= y and y < 10):
        col = "#FFBBFF"
    elif (10 <= y and y < 50):
        col = "#CCCCFF"
    elif (50 <= y and y < 100):
        col = "#ABFFFF"
    elif (100 <= y and y < 500):
        col = "#CCFFCC"
    elif (500 <= y and y < 1000):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (1000 <= y):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    return [y, col]







async def get_clubdam_dx_g_ranking_plus(user):
    asession = AsyncHTMLSession()
    url = f"https://dx-g.clubdam.info/user/{user}/others"
    # セッション開始
    r = await asession.get(url)
    await r.html.arender()

    # スクレイピング
    point_index_text = r.html.find(".highcharts-axis-labels")[0].find("text")
    point_times_text = r.html.find(".highcharts-stack-labels")[0].find("text")
    
    point_index = []
    point_times = []
    for point in point_index_text:
        point_index.append(point.text)
    for point in point_times_text:
        point_times.append(int(point.text))

    idx_plus = -1
    if "100+" in point_index:
        idx_plus = point_index.index("100+")
    
    y = 0
    if idx_plus != -1:
        y += point_times[idx_plus]

    if (y == 0):
        col = "#FFFFFF"
    elif (1 <= y and y < 4):
        col = "#FFCCDC"
    elif (4 <= y and y < 10):
        col = "#FFBBFF"
    elif (10 <= y and y < 50):
        col = "#CCCCFF"
    elif (50 <= y and y < 100):
        col = "#ABFFFF"
    elif (100 <= y and y < 500):
        col = "#CCFFCC"
    elif (500 <= y and y < 1000):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (1000 <= y):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    return [y, col]






async def get_info(handle, website):
    website = website.lower()
    if website == "clubdam-dx-point":
        return await get_clubdam_dx_point(handle)
    elif website == "clubdam-dx-chart":
        return await get_clubdam_dx_chart(handle)
    elif website == "clubdam-dx-ranking":
        return await get_clubdam_dx_ranking(handle)
    elif website == "clubdam-dx-g-point":
        return await get_clubdam_dx_g_point(handle)
    elif website == "clubdam-dx-g-chart":
        return await get_clubdam_dx_g_chart(handle)
    elif website == "clubdam-dx-g-ranking":
        return await get_clubdam_dx_g_ranking(handle)
    elif website == "clubdam-dx-g-ranking+":
        return await get_clubdam_dx_g_ranking_plus(handle)
    else:
        raise ValueError("wrong platform website name")
    




@app.route("/<website>/<handle>")
def get_badge(handle, website):
    q = None or request.args.get("logo")
    display_logo = True if (q and q.lower() == "true") else False
    logo = "https://clubdam.info/img/favicon.png"
    link = None or request.args.get("link")
    display_link = True if (len(str(link)) > 4) else False

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    x = loop.run_until_complete(get_info(handle, website))  

    rating, color = str(x[0]), str(x[1])
    text = website_text[website.lower()]
    if display_logo:
        if display_link:
            badge = pybadges.badge(left_text=text, right_text=rating,
                                   right_color=color, logo=logo, embed_logo=True, left_link=link)
        else:
            badge = pybadges.badge(
                left_text=text, right_text=rating, right_color=color, logo=logo, embed_logo=True)
    else:
        if display_link:
            badge = pybadges.badge(
                left_text=text, right_text=rating, right_color=color, left_link=link)
        else:
            badge = pybadges.badge(
                left_text=text, right_text=rating, right_color=color)
    response = flask.make_response(badge)
    response.content_type = "image/svg+xml"
    return response


@app.route("/")
def home():
    return "This API is working."


@app.errorhandler(404)
def page_not_found(error):
    return "This user doesn't exists."


if __name__ == "__main__":
    # app.debug = True
    app.run(threaded=False)