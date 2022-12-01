# _*_ coding : utf-8 _*_
# @Time : 2022/7/22 - 11:29
# @Author : Holden
# @File : ee
# @Project : python
import json
import operator
from datetime import datetime
import jieba
import pymysql

conn = pymysql.connect(
    host='8.130.49.69',
    port=3306,
    user='root',
    passwd='w654646',
    charset='utf8'
)

cursor = conn.cursor()
cursor.execute("SELECT title FROM spider_base.`df_a_stock_news`")
content = cursor.fetchall()
cursor.close()
conn.close()

dict = {}

for i in content:
    seg_list = jieba.cut(i[0], cut_all=True)

    for key in list(seg_list):
        if key != '.' and key != ',' and key != '%' and key != '' and key != '：' and key != ' ':
            dict[key] = dict.get(key, 0) + 1

x = sorted(dict.items(), key=operator.itemgetter(1))
print(x)

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)# 全模式
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)# 精确模式
