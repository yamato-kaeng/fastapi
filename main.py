# Author: Yamato Kaeng
# Date: 02/11/2020.

import re
import json
import urllib
# import pymongo
import uvicorn
# import requests
# import datetime
# import numpy as np
from fastapi import FastAPI
# from bs4 import BeautifulSoup
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# root_path="/yamato" run on vm setpath

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def result(res):
    return {"result": res}
# <---------------------------------------------------------> #


@app.get("/")
async def main():
    return 'Hello Wellcome To Yamato-Kaeng'
# <---------------------------------------------------------> #


@app.get("/test")
async def test():
    return 'Test Tutorial'
# <---------------------------------------------------------> #

@app.get("/bmi")
def bmi(h: int = 1, w: int = 0):

    h = (h/100) ** 2
    bmi = w/h

    des = ""

    if(bmi < 18.5):
        des = "ต่ำกว่าเกณฑ์"

    jsonout = {'bmi': f'{bmi:.2f}', 'des': des}

    return jsonout
# <---------------------------------------------------------> #

@app.get("/datatimes")
def datetimes(t: str = '+1'):
    dateout = str(datetime.datetime.now() + datetime.timedelta(days=int(t)))
    return dateout
# <---------------------------------------------------------> #

@app.get("/add")
async def add(a: int = 0, b: int = 0):
    return a+b
# <---------------------------------------------------------> #

@app.get("/mul")
async def mul(a: int = 0, b: int = 0):
    return a*b
# <---------------------------------------------------------> #

def tonumlist(li):
    ls = li.split(',')
    for i in range(len(ls)):
        ls[i] = float(ls[i])
    return list(ls)

@app.get("/asc")
async def asc(li):
    ls = tonumlist(li)
    ls.sort()
    return ls
# <---------------------------------------------------------> #

@app.get("/desc")
async def desc(li):
    ls = tonumlist(li)
    ls.sort(reverse=True)
    return ls
# <---------------------------------------------------------> #

@app.get("/sum")
async def sum(li):
    ls = tonumlist(li)
    return np.sum(np.array(ls))
# <---------------------------------------------------------> #

@app.get("/avg")
async def avg(li):
    ls = tonumlist(li)
    return np.average(ls)
# <---------------------------------------------------------> #

@app.get("/mean")
async def mean(li):
    ls = tonumlist(li)
    return np.mean(ls)
# <---------------------------------------------------------> #

@app.get("/max")
async def max(li):
    ls = tonumlist(li)
    return np.amax(ls)
# <---------------------------------------------------------> #


@app.get("/min")
async def min(li):
    ls = tonumlist(li)
    return np.amin(ls)
# <---------------------------------------------------------> #

@app.get("/validation-ctzid")
async def validation_ctzid(text):
    if(len(text) != 13):
        return False

    sum = 0
    listdata = list(text)

    for i in range(12):
        sum += int(listdata[i])*(13-i)

    d13 = sum % 11

    d13 = 1 if d13 == 0 else 0 if d13 == 1 else 11-d13

    if d13 == int(listdata[12]):
        return True
    else:
        return False
# <---------------------------------------------------------> #


# @app.get("/validation-email")
# async def validation_email(text):
#     regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#     if re.search(regex, text):
#         return True
#     else:
#         return False
# # <---------------------------------------------------------> #


# @app.get("/google-search", response_class=PlainTextResponse)
# def google_search(text):
#     # ค้นหา cat ==> head + url
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate',
#         'DNT': '1',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1'
#     }
#     url = 'https://www.google.com/search?q=' + urllib.parse.quote(str(text))
#     res = requests.get(url, headers=headers)
#     soup = BeautifulSoup(res.content, 'html.parser')

#     t = soup.findAll('div', {'class': "r"})
#     i = 0
#     result = ''
#     for a in t:
#         href = a.a['href']
#         head = a.h3.text
#         result = result + head + '<br>' + href + '<br><br>'
#         i += 1
#         if(i >= 5):
#             break

#     return(result)
# # <---------------------------------------------------------> #


# @app.get("/google-search-youtube", response_class=PlainTextResponse)
# def google_search_youtube(text):

#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate',
#         'DNT': '1',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1'
#     }
#     # url = 'https://www.google.com/search?q=' + str(text) + '&tbm=vid&hl=en-US' ----> แบบนี้อาจจะแย่มากไปนะจ๊ะ
#     url = 'https://www.google.com/search?q=site:youtube.com ' + \
#         urllib.parse.quote(str(text))
#     res = requests.get(url, headers=headers)
#     soup = BeautifulSoup(res.content, 'html.parser')

#     t = soup.findAll('a')
#     listcheck = list()
#     result = ''
#     for a in t:
#         try:
#             if('https://www.youtube.com/watch?' in a['href']):
#                 href = a['href']
#                 head = a.text.strip()
#                 if(href not in listcheck):
#                     listcheck.append(href)
#                     #result = result + head + '<br>' + href + '<br><br>'
#                     result = result + href + '<br><br>'
#                 if(len(listcheck) == 5):
#                     return result
#         except KeyError as e:
#             continue
# # <---------------------------------------------------------> #


# @app.get("/text-tokenize", response_class=PlainTextResponse)
# def text_tokenize(text):
#     tr1 = ''
#     tr2 = ''
#     tr3 = ''
#     tr4 = ''
#     textout = ''

#     if('"' in text or "'" in text):
#         tr1 = text.replace('"', '~')
#     if("'" in text):
#         tr2 = text.replace("'", '~')
#     if('“' in text and '”' in text):
#         tr3 = text.replace('“', '~')
#         tr3 = tr3.replace('”', '~')
#     if("‘" in text and "’" in text):
#         tr4 = text.replace("‘", '~')
#         tr4 = tr4.replace("’", '~')

#     if(len(tr1) != 0):
#         cc1 = checktext(tr1)
#         for a in cc1.split('~')[1::]:
#             textout = textout + '"' + a + '"' + '\n'
#     if(len(tr3) != 0):
#         cc3 = checktext(tr3)
#         for a in cc3.split('~')[1::]:
#             textout = textout + '"' + a + '"' + '\n'
#     if(len(tr2) != 0):
#         cc2 = checktext(tr2)
#         for a in cc2.split('~')[1::]:
#             textout = textout + "'" + a + "'" + '\n'
#     if(len(tr4) != 0):
#         cc4 = checktext(tr4)
#         for a in cc4.split('~')[1::]:
#             textout = textout + "'" + a + "'" + '\n'

#     return textout.strip()


# def checktext(tr):
#     check = False
#     listc = list()
#     textout = ''
#     for a in tr:
#         if(a == "~" and len(listc) <= 1):
#             check = True
#             listc.append('OK')
#         if(a == "~" and len(listc) == 2):
#             listc.pop()
#             listc.pop()
#         if(len(listc) == 0):
#             check = False
#         if(check):
#             textout = textout + a
#     return textout
# # <---------------------------------------------------------> #


# @app.get("/ark-serversPVP", response_class=PlainTextResponse)
# def ark_serverPVP():
#     # Ragnarok! ==> GetServers ARK !!
#     res = requests.get('https://www.battlemetrics.com/servers/ark/6663725')
#     soup = BeautifulSoup(res.content, 'html.parser')
#     f = soup.find('div', {'class': "col-md-8"}).findAll('a')
#     t = soup.find('div', {'class': "col-md-8"}).findAll('time')

#     text = ''
#     for a in range(0, len(f)):
#         print(f[a].text.strip(), t[a].text.strip())
#         text = text + f[a].text.strip() + ' >> ' + t[a].text.strip() + '<br>'

#     text = 'Active players : ' + str(len(f)) + '<br><br>' + text

#     return(text)
# # <---------------------------------------------------------> #


# @app.get("/ark-serversPVEEx", response_class=PlainTextResponse)
# def ark_serverPVEEx():
#     # Extinction! ==> GetServers ARK !!
#     res = requests.get('https://www.battlemetrics.com/servers/ark/6663729')
#     soup = BeautifulSoup(res.content, 'html.parser')
#     f = soup.find('div', {'class': "col-md-8"}).findAll('a')
#     t = soup.find('div', {'class': "col-md-8"}).findAll('time')

#     text = ''
#     for a in range(0, len(f)):
#         print(f[a].text.strip(), t[a].text.strip())
#         text = text + f[a].text.strip() + ' >> ' + t[a].text.strip() + '<br>'

#     text = 'Active players : ' + str(len(f)) + '<br><br>' + text

#     return(text)
# # <---------------------------------------------------------> #


# @app.get("/ark-serversPVEPm", response_class=PlainTextResponse)
# def ark_serverPVEPm():
#     # Primal! ==> GetServers ARK !!
#     res = requests.get('https://www.battlemetrics.com/servers/ark/8002813')
#     soup = BeautifulSoup(res.content, 'html.parser')
#     f = soup.find('div', {'class': "col-md-8"}).findAll('a')
#     t = soup.find('div', {'class': "col-md-8"}).findAll('time')

#     text = ''
#     for a in range(0, len(f)):
#         print(f[a].text.strip(), t[a].text.strip())
#         text = text + f[a].text.strip() + ' >> ' + t[a].text.strip() + '<br>'

#     text = 'Active players : ' + str(len(f)) + '<br><br>' + text

#     return(text)
# # <---------------------------------------------------------> #


# @app.get("/jobsDB-test", response_class=PlainTextResponse)
# def jobs_Test():

#     res = requests.get(
#         'https://th.jobsdb.com/th/th/job/oracle-functional-consultant-300003002258965', verify=False)
#     soup = BeautifulSoup(res.content, 'html.parser')
#     f = soup.find(
#         'h1', {'class': "FYwKg C6ZIU_3 _3nVJR_3 _642YY_3 _27Shq_3 _2k6I7_3"}).text

#     return(f)
# # <---------------------------------------------------------> #


# @app.get("/math-X", response_class=PlainTextResponse)
# def math_X(text):
#     # 1,2,3 ==> 6
#     listobj = text.split(',')
#     sumout = 1
#     for a in listobj:
#         sumout *= int(a)

#     return(str(sumout))
# # <---------------------------------------------------------> #


# @app.get("/math-ascii", response_class=PlainTextResponse)
# def math_ascii(text):
#     # abc10 ==> '0x61,0x62,0x63,0x31,0x30'
#     textout = ''
#     count = 1
#     for a in text:
#         t = hex(ord(a))
#         if(count >= len(text)):
#             textout += t
#         else:
#             textout = textout + t + ','
#         count += 1

#     return(textout)
# # <---------------------------------------------------------> #


# @app.get("/readmongo")
# def readmongo():
#     client = pymongo.MongoClient()
#     db = client['test_pymongo']
#     listout = []
#     for a in db.test.find():
#         dict1 = {'id': str(a['_id']), 'name': a['name'], 'age': a['age']}
#         listout.append(dict1)

#     return listout
# # <---------------------------------------------------------> #


# @app.get("/news-covid")
# def news_covid(lim: int = 30):
#     client = pymongo.MongoClient()
#     db = client['news']
#     listlinetoday = list(db.linetoday.find())
#     print('sum >', len(listlinetoday))
#     i = 0
#     j = 0
#     #stringout = ''
#     listout = []
#     for a in listlinetoday[::-1]:
#         try:
#             if 'covid' in str(a['title']).strip() or 'covid' in str(a['description']).strip() or 'โควิด' in str(a['title']).strip() or 'โควิด' in str(a['description']).strip():
#                 #stringout += 'url > ' + str(a['url']) + '<br>' +'title > ' + str(a['title']) + '<br>' +'description > ' + str(a['description']) + '<br>' +'created_at > ' + str(a['created_at']) + '<br>' + '-'*50 + '<br>'
#                 #stringout += 'url > ' + str(a['url']) + '\n' +'title > ' + str(a['title']) + '\n' +'description > ' + str(a['description']) + '\n' +'created_at > ' + str(a['created_at']) + '\n' + '-'*50 + '\n'
#                 dict1 = {'url': str(a['url']), 'title': str(a['title']).strip(), 'description': str(
#                     a['description']).strip(), 'created_at': str(a['created_at'])}
#                 listout.append(dict1)
#                 i += 1
#             if len(listout) == int(lim):
#                 break
#         except Exception as e:
#             j += 1
#             print(e, type(e))

#     print('check-covid >', i, j)

#     return {'data': listout}
# # <---------------------------------------------------------> #


# @app.get("/news-all")
# def news_all(lim: int = 30):
#     client = pymongo.MongoClient()
#     db = client['news']
#     listlinetoday = list(db.linetoday.find())
#     print('sum >', len(listlinetoday))
#     i = 0
#     j = 0
#     listout = []
#     for a in listlinetoday[::-1]:
#         try:
#             dict1 = {'url': str(a['url']), 'title': str(a['title']).strip(), 'description': str(
#                 a['description']).strip(), 'created_at': str(a['created_at'])}
#             listout.append(dict1)
#             i += 1
#             if len(listout) == int(lim):
#                 break
#         except Exception as e:
#             j += 1
#             print(e, type(e))

#     print('check-all >', i, j)

#     return {'data': listout}
# # <---------------------------------------------------------> #


# @app.get("/covid-api", response_class=PlainTextResponse)
# def covid_api():
#     import datetime
#     res = requests.get('https://covid19.th-stat.com/api/open/today')
#     jj = res.json()

#     dd = str(jj['UpdateDate'])
#     y = int(dd.split()[0].split('/')[-1])
#     m = int(dd.split()[0].split('/')[1])
#     d = int(dd.split()[0].split('/')[0])
#     days = "-- "+str(datetime.datetime(y, m, d).strftime("%a"))+" "+dd+" --"

#     jjout = {
#         "type": "bubble",
#         "body": {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#             {
#                 "type": "image",
#                 "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnOjK39ZKttYRVkSB9nvpjKE2r5uOGSiII2w&usqp=CAU",
#                 "size": "full",
#                 "aspectMode": "cover",
#                 "aspectRatio": "3:4",
#                 "gravity": "top"
#             },
#             {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                 {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": days,
#                             "size": "lg",
#                             "color": "#ffffff"
#                         }
#                         ],
#                         "alignItems": "center"
#                     }
#                     ]
#                 },
#                 {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": "ติดเชื้อรายใหม่ :",
#                             "color": "#ffffff",
#                             "size": "md"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": str(jj['NewConfirmed']),
#                             "color": "#ffffff",
#                             "size": "md"
#                         }
#                         ]
#                     }
#                     ],
#                     "margin": "md"
#                 },
#                 {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": "ติดเชื้อสะสม :",
#                             "size": "md",
#                             "color": "#ffffff"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": str(jj['Confirmed']),
#                             "size": "md",
#                             "color": "#ffffff"
#                         }
#                         ]
#                     }
#                     ],
#                     "margin": "md"
#                 },
#                 {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": "หายแล้ว :",
#                             "size": "md",
#                             "color": "#ffffff"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": str(jj['Recovered']),
#                             "size": "md",
#                             "color": "#ffffff"
#                         }
#                         ]
#                     }
#                     ],
#                     "margin": "md"
#                 },
#                 {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": "รักษาอยู่ใน รพ. :",
#                             "size": "md",
#                             "color": "#ffffff"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "box",
#                         "layout": "vertical",
#                         "contents": [
#                         {
#                             "type": "text",
#                             "text": str(jj['Hospitalized']),
#                             "size": "md",
#                             "color": "#ffffff"
#                         }
#                         ]
#                     }
#                     ],
#                     "margin": "md"
#                 }
#                 ],
#                 "position": "absolute",
#                 "offsetBottom": "0px",
#                 "offsetStart": "0px",
#                 "offsetEnd": "0px",
#                 "backgroundColor": "#03303Acc",
#                 "paddingAll": "20px",
#                 "paddingTop": "18px"
#             }
#             ],
#             "paddingAll": "0px",
#             "action": {
#                 "type": "uri",
#                 "label": "action",
#                 "uri": "https://covid19.th-stat.com/"
#             }
#         }
#     }

#     #stringout = 'ติดเชื้อรายใหม่ > '+str(jj['NewConfirmed'])+'<br>'+'อัพเดทข้อมูลล่าสุด > '+str(jj['UpdateDate'])+'<br>'+'ติดเชื้อสะสม > '+str(
#     #    jj['Confirmed'])+'<br>'+'หายแล้ว > '+str(jj['Recovered'])+'<br>'+'รักษาอยู่ใน รพ. > '+str(jj['Hospitalized'])

#     return str(jjout)
# # <---------------------------------------------------------> #


# @app.get("/flex-news-all-v1", response_class=PlainTextResponse)
# def flex_news_all_v1(lim: int = 20):
#     import requests
#     res = requests.get('https://abdul.in.th/v24/yamato/news-all?lim=20')
#     if str(res) != '<Response [200]>':
#         return 'ERROR > https://abdul.in.th/v24/yamato/news-all?lim=20'

#     listitems = []
#     listcat = ['https://ichef.bbci.co.uk/news/640/cpsprodpb/51F3/production/_106997902_gettyimages-611696954.jpg',
#                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJq7At985pAblTrxTw2Ed4oFv7-gSKXOVUgA&usqp=CAU',
#                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwbFjmdFjV30g9BmsQLalmFEdDpbzV0T-KEg&usqp=CAU',
#                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpruLsawmEmkm8aa1UQJ4bSK68NXIIJ1qcpQ&usqp=CAU',
#                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrXHYWYcGgqfMCoFDkMgzsQBAWfEeJfWXPlw&usqp=CAU']

#     for a in res.json()['data']:
#         if str(a['imageurl']) != '':
#             listitems.append({'title': a['title'], 'url': a['url'], 'imageurl': a['imageurl']})

#     def image(listimage):
#         listimageout = []
#         i = 0
#         for a in listimage:
#             dict1 = {}
#             if i == 0:
#                 dict1 = {
#                     "type": "image",
#                     # "url": str(listcat[i]),
#                     "url": str(a['imageurl']),
#                     "align": "center",
#                     "gravity": "top",
#                     "size": "sm",
#                     "aspectRatio": "4:3",
#                     "aspectMode": "cover",
#                     "action": {
#                         "type": "uri",
#                         "uri": str(a['url'])
#                     }
#                 }
#             else:
#                 dict1 = {
#                     "type": "image",
#                     # "url": str(listcat[i]),
#                     "url": str(a['imageurl']),
#                     "margin": "md",
#                     "align": "center",
#                     "gravity": "top",
#                     "size": "sm",
#                     "aspectRatio": "4:3",
#                     "aspectMode": "cover",
#                     "action": {
#                         "type": "uri",
#                         "uri": str(a['url'])
#                     }
#                 }
#             listimageout.append(dict1)
#             i += 1
#         return listimageout

#     def title(listtitle):
#         listtitleout = []
#         i = 0
#         for a in listtitle:
#             dict1 = {
#                 "type": "text",
#                 "text": str(a['title']),
#                 "size": "xs",
#                 "flex": 2,
#                 "align": "start",
#                 "gravity": "center",
#                 "action": {
#                     "type": "uri",
#                     "uri": str(a['url'])
#                 },
#                 "contents": []
#             }

#             listtitleout.append(dict1)
#             i += 1
#             if i != len(listtitle):
#                 listtitleout.append({"type": "separator"})
#         return listtitleout

#     def carousel(listitems):
#         i = 0
#         listcarouselout = []
#         while (True):
#             listimage = image(listitems[i:i+5])
#             listtitle = title(listitems[i:i+5])
#             dict1 = {
#                 "type": "bubble",
#                 "header": {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                         {
#                             "type": "text",
#                             "text": "LINE TODAY NEWS",
#                             "weight": "bold",
#                             "size": "sm",
#                             "color": "#000000FF",
#                             "contents": []
#                         }
#                     ]
#                 },
#                 "hero": {
#                     "type": "image",
#                     "url": "https://lineforbusiness.com/files/Service"+"%20"+"Logo-04___2.png",
#                     "size": "full",
#                     "aspectRatio": "20:12",
#                     "aspectMode": "cover",
#                     "backgroundColor": "#6DEA91FF",
#                     "action": {
#                         "type": "uri",
#                         "label": "Action",
#                         "uri": "https://today.line.me/th/v2/tab"
#                     }
#                 },
#                 "body": {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "spacing": "md",
#                     "contents": [
#                         {
#                             "type": "box",
#                             "layout": "vertical",
#                             "flex": 1,
#                             "contents": listimage
#                         },
#                         {
#                             "type": "box",
#                             "layout": "vertical",
#                             "flex": 2,
#                             "contents": listtitle
#                         }
#                     ]
#                 }
#             }

#             listcarouselout.append(dict1)
#             i += 5
#             if i == 20:
#                 return listcarouselout

#     dictout = {"type": "carousel", "contents": carousel(listitems)}

#     return str(dictout)
# # <---------------------------------------------------------> #


# @app.get("/flex-news-all-v2", response_class=PlainTextResponse)
# def flex_news_all_v2():
#     import requests
#     res = requests.get('https://abdul.in.th/v24/yamato/news-all?lim=10')
#     if str(res) != '<Response [200]>': return 'ERROR > https://abdul.in.th/v24/yamato/news-all'

#     listitems = []
#     for a in res.json()['data']:
#         if str(a['imageurl']) != '':
#             listitems.append({'title': a['title'], 'url': a['url'], 'imageurl': a['imageurl']})

#     def content(items):
#         listflex = []
#         for a in items:
#             dict1 = {
#                 "type": "bubble",
#                 "body": {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [
#                         {
#                             "type": "image",
#                             "url": str(a['imageurl']),
#                             "size": "full",
#                             "aspectMode": "cover",
#                             "aspectRatio": "2:3",
#                             "gravity": "top"
#                         },
#                         {
#                             "type": "box",
#                             "layout": "vertical",
#                             "contents": [
#                                 {
#                                     "type": "box",
#                                     "layout": "vertical",
#                                     "contents": [
#                                         {
#                                             "type": "text",
#                                             "text": str(a['title']),
#                                             "size": "md",
#                                             "color": "#ffffff",
#                                             "weight": "bold"
#                                             #"wrap": True
#                                         }
#                                     ]
#                                 },
#                                 {
#                                     "type": "box",
#                                     "layout": "vertical",
#                                     "contents": [
#                                         {
#                                             "type": "filler"
#                                         },
#                                         {
#                                             "type": "box",
#                                             "layout": "baseline",
#                                             "contents": [
#                                                 {
#                                                     "type": "filler"
#                                                 },
#                                                 {
#                                                     "type": "text",
#                                                     "text": "more",
#                                                     "color": "#ffffff",
#                                                     "flex": 0,
#                                                     "offsetTop": "-2px"
#                                                 },
#                                                 {
#                                                     "type": "filler"
#                                                 }
#                                             ],
#                                             "spacing": "sm"
#                                         },
#                                         {
#                                             "type": "filler"
#                                         }
#                                     ],
#                                     "borderWidth": "1px",
#                                     "cornerRadius": "sm",
#                                     "spacing": "sm",
#                                     "borderColor": "#ffffff",
#                                     "margin": "xxl",
#                                     "height": "40px",
#                                     "action": {
#                                         "type": "uri",
#                                         "label": "action",
#                                         "uri": str(a['url'])
#                                     }
#                                 }
#                             ],
#                             "position": "absolute",
#                             "offsetBottom": "0px",
#                             "offsetStart": "0px",
#                             "offsetEnd": "0px",
#                             "backgroundColor": "#03303Acc",
#                             "paddingAll": "20px",
#                             "paddingTop": "18px",
#                         }
#                     ],
#                     "paddingAll": "0px"
#                 }
#             }

#             listflex.append(dict1)
#         return listflex

#     dictout = {"type": "carousel", "contents": content(listitems)}
#     return str(dictout)
# # <---------------------------------------------------------> #

# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8080, debug=True)
