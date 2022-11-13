# from typing import Optional
# import pybadges
# import asyncio
# from typing import Optional
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from requests_html import AsyncHTMLSession
# from requests_html import HTML
# from pyppeteer import launch


# import zipfile
# import os, subprocess
# import urllib.error
# import urllib.request

# file_url = "https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip"


# import tempfile

# prefix = tempfile.gettempdir()

# save_path = prefix+"/download.zip"

# with urllib.request.urlopen(file_url) as download_file:
#     data = download_file.read()
#     with open(save_path, mode='wb') as save_file:
#         save_file.write(data)
#     with zipfile.ZipFile(prefix+"/download.zip") as obj_zip:
#         # 指定ディレクトリにすべてを保存する
#         obj_zip.extractall(prefix)
#         subprocess.run(["chmod", "+x", prefix+"/headless-chromium"], check=True)

# # with urllib.request.urlopen(file_url) as download_file:
# #     data = download_file.read()
# #     with open(save_path, mode='wb') as save_file:
# #         save_file.write(data)
# #     with zipfile.ZipFile(prefix+"/download.zip") as obj_zip:
# #         # 指定ディレクトリにすべてを保存する
# #         obj_zip.extractall(prefix)
# #         subprocess.run(["chmod", "+x", prefix+"/headless-chromium"], check=True)

# # print(subprocess.call('ls'))





# # s3_bucket = boto3.resource("s3").Bucket("YOUR_BUCKET")
# # zip_file_path = "/tmp/chrome.zip"
# # if not os.path.exists(zip_file_path):
# #     # s3_bucket.download_file("S3_PATH", zip_file_path)
# #     with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
# #         zip_ref.extractall("/tmp")
# #         subprocess.run(["chmod", "+x", "/tmp/headless-chromium"], check=True)
# app = FastAPI()


# website_text = {
#     "clubdam-dx-point": "DAM-DX-Point",
#     "clubdam-dx-chart": "DAM-DX-Chart",
#     "clubdam-dx-ranking": "DAM-DX-Ranking",
#     "clubdam-dx-g-point": "DAM-DX-G-Point",
#     "clubdam-dx-g-chart": "DAM-DX-G-Chart",
#     "clubdam-dx-g-ranking": "DAM-DX-G-Ranking",
#     "clubdam-dx-g-ranking+": "DAM-DX-G-Ranking+",
# }

# async def get_clubdam_dx_point(user):
#     # asession = AsyncHTMLSession()
#     url = f"https://clubdam.info/user/{user}/song"



    
#     # セッション開始

#     # os.chdir("/tmp")
#     # print(subprocess.call('ls'))
#     # return ["100", "#FFFF00"]
#     browser = await launch(
#         userDataDir=prefix,
#         # executablePath=prefix+"/headless-chromium",
#         headless=False,
#         timeout=30000
#     )

#     # return ["100", "#FFFF00"]

#     page = await browser.newPage()
#     # await page.setViewport({"width": 1280, "height": 960})

#     await asyncio.wait([
#         page.goto(url),
#         page.waitForNavigation(),
#     ])
#     content = await page.content()
#     html = HTML(html=content)

#     await browser.close()





#     # r = await asession.get(url)
#     # await r.html.arender(wait=3, sleep=3, keep_page=True)
#     # return ["100", "#FFFF00"]

#     # スクレイピング
#     point = float(html.find("#data_1")[0].find(".table_point", first=True).text)

#     y = point
#     if (y < 80.000):
#         col = "#FFFFFF"
#     elif (80.000 <= y and y < 85.000):
#         col = "#FFCCDC"
#     elif (85.000 <= y and y < 90.000):
#         col = "#FFBBFF"
#     elif (90.000 <= y and y < 95.000):
#         col = "#CCCCFF"
#     elif (95.000 <= y and y < 98.000):
#         col = "#ABFFFF"
#     elif (98.000 <= y and y < 99.000):
#         col = "#CCFFCC"
#     elif (99.000 <= y and y < 100.000):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (100.000 <= y):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return ["{:.3f}".format(y), col]


# async def get_clubdam_dx_chart(user):
#     asession = AsyncHTMLSession()
#     url = f"https://clubdam.info/user/{user}/song/index/max_chartSum/desc"
#     # セッション開始
#     r = await asession.get(url)
#     await r.html.arender()

#     # スクレイピング
#     chart = int(r.html.find("#data_1")[0].find(".table_chart_total", first=True).text)

#     y = chart
#     if (y < 320):
#         col = "#FFFFFF"
#     elif (320 <= y and y < 370):
#         col = "#FFCCDC"
#     elif (370 <= y and y < 420):
#         col = "#FFBBFF"
#     elif (420 <= y and y < 450):
#         col = "#CCCCFF"
#     elif (450 <= y and y < 470):
#         col = "#ABFFFF"
#     elif (470 <= y and y < 480):
#         col = "#CCFFCC"
#     elif (480 <= y and y < 490):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (490 <= y):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return [y, col]



# async def get_clubdam_dx_ranking(user):
#     asession = AsyncHTMLSession()
#     url = f"https://clubdam.info/user/{user}/others"
#     # セッション開始
#     r = await asession.get(url)
#     await r.html.arender()

#     # スクレイピング
#     point_index_text = r.html.find(".highcharts-axis-labels")[0].find("text")
#     point_times_text = r.html.find(".highcharts-stack-labels")[0].find("text")
    
#     point_index = []
#     point_times = []
#     for point in point_index_text:
#         point_index.append(point.text)
#     for point in point_times_text:
#         point_times.append(int(point.text.replace(",", "")))
#     idx = -1
#     if "100" in point_index:
#         idx = point_index.index("100")
    
#     y = 0
#     if idx != -1:
#         y += point_times[idx]
#     if (y == 0):
#         col = "#FFFFFF"
#     elif (1 <= y and y < 4):
#         col = "#FFCCDC"
#     elif (4 <= y and y < 10):
#         col = "#FFBBFF"
#     elif (10 <= y and y < 50):
#         col = "#CCCCFF"
#     elif (50 <= y and y < 100):
#         col = "#ABFFFF"
#     elif (100 <= y and y < 500):
#         col = "#CCFFCC"
#     elif (500 <= y and y < 1000):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (1000 <= y):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return [y, col]





# async def get_clubdam_dx_g_point(user):
#     asession = AsyncHTMLSession()
#     url = f"https://dx-g.clubdam.info/user/{user}/song"
#     # セッション開始
#     r = await asession.get(url)
#     await r.html.arender()

#     # スクレイピング
#     point = float(r.html.find("#data_1")[0].find(".table_point", first=True).text)
#     raw_point = float(r.html.find("#data_1")[0].find(".table_rawPoint", first=True).text)
#     y = point
#     if (y < 80.000):
#         col = "#FFFFFF"
#     elif (80.000 <= y and y < 85.000):
#         col = "#FFCCDC"
#     elif (85.000 <= y and y < 90.000):
#         col = "#FFBBFF"
#     elif (90.000 <= y and y < 95.000):
#         col = "#CCCCFF"
#     elif (95.000 <= y and y < 98.000):
#         col = "#ABFFFF"
#     elif (98.000 <= y and y < 99.000):
#         col = "#CCFFCC"
#     elif (99.000 <= y and y < 100.000):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (100.000 <= y and raw_point < 100.000):
#         col = "#FFF550"
#     elif (100.000 <= y and 100.000 <= raw_point):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return ["{:.3f}".format(y), col]


# async def get_clubdam_dx_g_chart(user):
#     asession = AsyncHTMLSession()
#     url = f"https://dx-g.clubdam.info/user/{user}/song/index/max_radarChartTotal/desc"
#     # セッション開始
#     r = await asession.get(url)
#     await r.html.arender()

#     # スクレイピング
#     chart = int(r.html.find("#data_1")[0].find(".table_chart_total", first=True).text)

#     y = chart
#     if (y < 320):
#         col = "#FFFFFF"
#     elif (320 <= y and y < 370):
#         col = "#FFCCDC"
#     elif (370 <= y and y < 420):
#         col = "#FFBBFF"
#     elif (420 <= y and y < 450):
#         col = "#CCCCFF"
#     elif (450 <= y and y < 470):
#         col = "#ABFFFF"
#     elif (470 <= y and y < 480):
#         col = "#CCFFCC"
#     elif (480 <= y and y < 490):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (490 <= y):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return [y, col]



# async def get_clubdam_dx_g_ranking(user):
#     asession = AsyncHTMLSession()
#     url = f"https://dx-g.clubdam.info/user/{user}/others"
#     # セッション開始
#     r = await asession.get(url)
#     await r.html.arender()

#     # スクレイピング
#     point_index_text = r.html.find(".highcharts-axis-labels")[0].find("text")
#     point_times_text = r.html.find(".highcharts-stack-labels")[0].find("text")
    
#     point_index = []
#     point_times = []
#     for point in point_index_text:
#         point_index.append(point.text)
#     for point in point_times_text:
#         point_times.append(int(point.text.replace(",", "")))
#     idx = -1
#     idx_plus = -1
#     if "100" in point_index:
#         idx = point_index.index("100")
#     if "100+" in point_index:
#         idx_plus = point_index.index("100+")
    
#     y = 0
#     if idx != -1:
#         y += point_times[idx]
#     if idx_plus != -1:
#         y += point_times[idx_plus]
#     if (y == 0):
#         col = "#FFFFFF"
#     elif (1 <= y and y < 4):
#         col = "#FFCCDC"
#     elif (4 <= y and y < 10):
#         col = "#FFBBFF"
#     elif (10 <= y and y < 50):
#         col = "#CCCCFF"
#     elif (50 <= y and y < 100):
#         col = "#ABFFFF"
#     elif (100 <= y and y < 500):
#         col = "#CCFFCC"
#     elif (500 <= y and y < 1000):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (1000 <= y):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return [y, col]







# async def get_clubdam_dx_g_ranking_plus(user):
#     asession = AsyncHTMLSession()
#     url = f"https://dx-g.clubdam.info/user/{user}/others"
#     # セッション開始
#     r = await asession.get(url)
#     await r.html.arender()

#     # スクレイピング
#     point_index_text = r.html.find(".highcharts-axis-labels")[0].find("text")
#     point_times_text = r.html.find(".highcharts-stack-labels")[0].find("text")
    
#     point_index = []
#     point_times = []
#     for point in point_index_text:
#         point_index.append(point.text)
#     for point in point_times_text:
#         point_times.append(int(point.text.replace(",", "")))

#     idx_plus = -1
#     if "100+" in point_index:
#         idx_plus = point_index.index("100+")
    
#     y = 0
#     if idx_plus != -1:
#         y += point_times[idx_plus]

#     if (y == 0):
#         col = "#FFFFFF"
#     elif (1 <= y and y < 4):
#         col = "#FFCCDC"
#     elif (4 <= y and y < 10):
#         col = "#FFBBFF"
#     elif (10 <= y and y < 50):
#         col = "#CCCCFF"
#     elif (50 <= y and y < 100):
#         col = "#ABFFFF"
#     elif (100 <= y and y < 500):
#         col = "#CCFFCC"
#     elif (500 <= y and y < 1000):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (1000 <= y):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return [y, col]






# async def get_info(handle, website):
#     website = website.lower()
#     if website == "clubdam-dx-point":
#         return await get_clubdam_dx_point(handle)
#     elif website == "clubdam-dx-chart":
#         return await get_clubdam_dx_chart(handle)
#     elif website == "clubdam-dx-ranking":
#         return await get_clubdam_dx_ranking(handle)
#     elif website == "clubdam-dx-g-point":
#         return await get_clubdam_dx_g_point(handle)
#     elif website == "clubdam-dx-g-chart":
#         return await get_clubdam_dx_g_chart(handle)
#     elif website == "clubdam-dx-g-ranking":
#         return await get_clubdam_dx_g_ranking(handle)
#     elif website == "clubdam-dx-g-ranking+":
#         return await get_clubdam_dx_g_ranking_plus(handle)
#     else:
#         raise ValueError("wrong platform website name")
    




# @app.get("/{website}/{handle}")
# async def get_badge(handle, website):

#     loop = asyncio.get_event_loop()
#     # asyncio.set_event_loop(loop)
#     # x = loop.run_until_complete(get_info(handle, website))
    
#     x = await asyncio.gather(
#         get_info(handle, website)
#     )
#     # x = [["100", "#FFFF00"]]
#     rating, color = str(x[0][0]), str(x[0][1])
#     text = website_text[website.lower()]
#     badge = pybadges.badge(left_text=text, right_text=rating, right_color=color)
#     return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')


# @app.get("/")
# def index():
#     return "This API is working."






from typing import Optional
import pybadges
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from requests_html import HTMLSession
from requests_html import HTML
from pyppeteer import launch
import json



# with urllib.request.urlopen(file_url) as download_file:
#     data = download_file.read()
#     with open(save_path, mode='wb') as save_file:
#         save_file.write(data)
#     with zipfile.ZipFile(prefix+"/download.zip") as obj_zip:
#         # 指定ディレクトリにすべてを保存する
#         obj_zip.extractall(prefix)
#         subprocess.run(["chmod", "+x", prefix+"/headless-chromium"], check=True)

# print(subprocess.call('ls'))





# s3_bucket = boto3.resource("s3").Bucket("YOUR_BUCKET")
# zip_file_path = "/tmp/chrome.zip"
# if not os.path.exists(zip_file_path):
#     # s3_bucket.download_file("S3_PATH", zip_file_path)
#     with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
#         zip_ref.extractall("/tmp")
#         subprocess.run(["chmod", "+x", "/tmp/headless-chromium"], check=True)
app = FastAPI()


website_text = {
    "clubdam-dx-ranking": "DAM-DX-Ranking",
    "clubdam-dx-g-ranking": "DAM-DX-G-Ranking",
    "clubdam-dx-g-ranking-plus": "DAM-DX-G-Ranking+",
}




# def get_clubdam_dx_ranking(user):
#     session = HTMLSession()
#     url = "https://clubdam.info/repranking"
#     # セッション開始
#     r = session.get(url)

#     # スクレイピング
#     point_index_text = r.html.find("tbody", first=True).find("tr")
#     point_times_text = r.html.find("tbody", first=True).find("tr")
    
#     point_index = []
#     point_times = []
#     for point in point_index_text:
#         point_index.append(point.find("td")[1].text)
#     for point in point_times_text:
#         point_times.append(point.find("td")[2].text)


#     idx = -1
#     if user in point_index:
#         idx = point_index.index(user)
    
#     y = "***"
#     if idx != -1:
#         y = point_times[idx]
    
#     if (y == "***"):
#         col = "#FFFFFF"
#     elif (0 == int(y)):
#         col = "#FFFFFF"
#     elif (1 <= int(y) < 4):
#         col = "#FFCCDC"
#     elif (4 <= int(y) < 10):
#         col = "#FFBBFF"
#     elif (10 <= int(y) < 50):
#         col = "#CCCCFF"
#     elif (50 <= int(y) < 100):
#         col = "#ABFFFF"
#     elif (100 <= int(y) < 500):
#         col = "#CCFFCC"
#     elif (500 <= int(y) < 1000):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (1000 <= int(y)):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return [y, col]





def get_clubdam_dx_g_ranking(user):
    session = HTMLSession()
    base_url = "https://dx-g.clubdam.info/history/load_content_div/{}/scoringDateTime/desc".format(user)
    # セッション開始
    idx = 1
    highscore = {}
    li_list = []
    while True:
        url = "{}/{}".format(base_url, idx)
        r = session.get(url)
        if r.html.text == "歌唱履歴がありません": break
        # break
        
        point_index_text = r.html.find("tbody")
        if idx == 20: break
        # print(point_index_text)
        li_list.extend(point_index_text)
        
        idx += 1
    for i in li_list:
        str_data = i.attrs["data-object_data"]
        dict_data = json.loads(str_data)
        request_no = dict_data["requestNo"]
        raw_point = float(dict_data["rawPoint"])
        if highscore.get(request_no) == None: highscore[request_no] = float(0)
        highscore[request_no] = max(highscore[request_no], raw_point)


    # print("Success!!")
    y = 0
    for key, value in highscore.items():
        if int(value) == 100:
            y += 1

    # スクレイピング
    # point_index_text = r.html.find("tbody", first=True).find("tr")
    # point_times_text = r.html.find("tbody", first=True).find("tr")
    
    # point_index = []
    # point_times = []
    # for point in point_index_text:
    #     point_index.append(point.find("td")[1].text)
    # for point in point_times_text:
    #     point_times.append(point.find("td")[2].text)


    # idx = -1
    # if user in point_index:
    #     idx = point_index.index(user)
    
    # if idx != -1:
    #     y = point_times[idx]
    
    if (0 == int(y)):
        col = "#FFFFFF"
    elif (1 <= int(y) < 4):
        col = "#FFCCDC"
    elif (4 <= int(y) < 10):
        col = "#FFBBFF"
    elif (10 <= int(y) < 50):
        col = "#CCCCFF"
    elif (50 <= int(y) < 100):
        col = "#ABFFFF"
    elif (100 <= int(y) < 500):
        col = "#CCFFCC"
    elif (500 <= int(y) < 1000):
        # col = "#FFFFAA"
        col = "#FFF550"
    elif (1000 <= int(y)):
        col = "#FFCC11"
    else:
        col = "#FFFFFF"
    # print([y, col])
    return [y, col]




# def get_clubdam_dx_g_ranking_plus(user):
#     session = HTMLSession()
#     url = "https://dx-g.clubdam.info/history/load_content_div/nope0421/scoringDateTime/desc/1"
#     # セッション開始
#     r = session.get(url)

#     # スクレイピング
#     point_index_text = r.html.find("tbody", first=True).find("tr")
#     point_times_text = r.html.find("tbody", first=True).find("tr")
    
#     point_index = []
#     point_times = []
#     for point in point_index_text:
#         point_index.append(point.find("td")[1].text)
#     for point in point_times_text:
#         point_times.append(point.find("td")[2].text)


#     idx = -1
#     if user in point_index:
#         idx = point_index.index(user)
    
#     y = "***"
#     if idx != -1:
#         y = point_times[idx]
    
#     if (y == "***"):
#         col = "#FFFFFF"
#     elif (0 == int(y)):
#         col = "#FFFFFF"
#     elif (1 <= int(y) < 4):
#         col = "#FFCCDC"
#     elif (4 <= int(y) < 10):
#         col = "#FFBBFF"
#     elif (10 <= int(y) < 50):
#         col = "#CCCCFF"
#     elif (50 <= int(y) < 100):
#         col = "#ABFFFF"
#     elif (100 <= int(y) < 500):
#         col = "#CCFFCC"
#     elif (500 <= int(y) < 1000):
#         # col = "#FFFFAA"
#         col = "#FFF550"
#     elif (1000 <= int(y)):
#         col = "#FFCC11"
#     else:
#         col = "#FFFFFF"
#     return [y, col]





def get_info(handle, website):
    website = website.lower()
    # if website == "clubdam-dx-ranking":
    #     return get_clubdam_dx_ranking(handle)
    if website == "clubdam-dx-g-ranking":
        return get_clubdam_dx_g_ranking(handle)
    # elif website == "clubdam-dx-g-ranking-plus":
    #     return get_clubdam_dx_g_ranking_plus(handle)
    else:
        raise ValueError("wrong platform website name")




@app.get("/{website}/{handle}")
def get_badge(handle, website):

    # loop = asyncio.get_event_loop()
    # asyncio.set_event_loop(loop)
    # x = loop.run_until_complete(get_info(handle, website))
    
    x = get_info(handle, website)
    
    # x = [["100", "#FFFF00"]]
    rating, color = str(x[0]), str(x[1])
    text = website_text[website.lower()]
    badge = pybadges.badge(left_text=text, right_text=rating, right_color=color)
    return HTMLResponse(content=badge, status_code=200, media_type='image/svg+xml')


@app.get("/")
def index():
    return "This API is working."
