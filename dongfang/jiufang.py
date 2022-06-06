# _*_ coding : utf-8 _*_
# @Time : 2022/5/26 - 17:58
# @Author : Holden
# @File : jiufang
# @Project : python
import requests
import jsonpath
import json
from dongfang.Stock import Stock
import pymysql
import re
import datetime
import time

# 这里有点麻烦，这个网站使用了ajax请求，使用marketCenter.js来发送请求，还对signature进行了加密处理
url = 'http://api-hq.chongnengjihua.com/finance/api/2/stock/a/rank/list?pageNum=1&pageSize=100&listedSector=0&sortField=pxChangeRate&sortType=0'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'api-hq.chongnengjihua.com',
    'Origin': 'https://www.9fzt.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.9fzt.com/',
    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'signature': 'daff9da6e41ed01705a7e5696ecc9cd4',
    'timestamp': '1653558718469',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
response = requests.get(url=url,headers=headers)

print(response.text)