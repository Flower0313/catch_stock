# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 22:40
# @Author : Holden
# @File : test
# @Project : python
import os
import threading
import time
import smtplib
import requests
import json

df_url = "https://data.eastmoney.com/stockcomment/api/603719.json"

response = requests.get(url=df_url, verify=False)
content = json.loads(response.text)['ApiResults']['scrd']['focus'][1]
x = content['XData']
y = content['Ydata']['StockFocus']
# 每日15:00后会刷新当天的数据
print(x[0], y[1])
