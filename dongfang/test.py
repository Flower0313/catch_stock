# _*_ coding : utf-8 _*_
# @Time : 2022/6/22 - 16:25
# @Author : Holden
# @File : test
# @Project : python
import datetime
import json
import re
import time
from concurrent.futures.thread import ThreadPoolExecutor

import pymysql
import requests
from json import JSONDecodeError
import selenium

conn = pymysql.connect(
    host='8.130.49.69',
    port=3306,
    user='root',
    passwd='w654646',
    charset='utf8'
)
stocks = []
for i in range(5187):
    stocks.append(i + 1)

nums = len(stocks)
step = 520
y = nums % step
stock_num = (y if nums <= 0 else 1) + (nums // step)

for i in range(stock_num):
    print(stocks[i * step:(i + 1) * step])
