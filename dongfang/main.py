# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 22:40
# @Author : Holden
# @File : test
# @Project : python
import pymysql
import requests
import jsonpath
import json
from datetime import datetime

from dongfang.get_a_stock_list import catch_stock
import time

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='spider_base',
    charset='utf8'
)

cursor = conn.cursor()
cursor.execute("SELECT typeDes FROM `df_calendar` where date='" + str(datetime.now().date()) + "'")
result = cursor.fetchone()

if result[0] == '工作日':
    catch_stock((int(time.mktime(time.localtime(time.time())))) * 1000)

conn.commit()
cursor.close()  # 记得释放资源
conn.close()
