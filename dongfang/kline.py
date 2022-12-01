import matplotlib.pyplot as plt
import matplotlib
import pymysql
import re

import requests

print("open")
response = requests.get(
    "http://push2.eastmoney.com/api/qt/stock/details/get?fields1=f1,f2,f3,f4&fields2=f51,f52,f53,f54,f55&fltt=2&pos=-0&secid=1.688371&wbp2u=4819115464066356|0|0|0|web&ut=bd1d9ddb04089700cf9c27f6f7426281")

print(response.text)
