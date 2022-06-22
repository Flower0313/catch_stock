# _*_ coding : utf-8 _*_
# @Time : 2022/6/22 - 16:25
# @Author : Holden
# @File : test
# @Project : python
from concurrent.futures.thread import ThreadPoolExecutor

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='spider_base',
    charset='utf8'
)
cursor = conn.cursor()

index = 1


def show(r):
    cursor.execute("insert into python values(" + r + ")")
    conn.commit()


with ThreadPoolExecutor(5) as t:
    for r in range(10):
        t.submit(show, r)

cursor.close()
conn.close()
