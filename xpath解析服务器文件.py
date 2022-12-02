# _*_ coding : utf-8 _*_
# @Time : 2022/5/18 - 9:46
# @Author : Holden
# @File : xpath解析服务器文件
# @Project : python
import json

import requests
from lxml import etree

comment_url = "https://guba.eastmoney.com/list,603719_1.html"
df_url = "https://data.eastmoney.com/stockcomment/api/603719.json"

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

response = requests.get(url=comment_url, verify=False)
tree = etree.HTML(response.text)
timez = tree.xpath('//div[contains(@class,"articleh normal_post")]/span[contains(@class,"l5 a5")]/text()')
follow_count = [x for x in timez if x < '12-02 09:20:00']
print(len(follow_count))



# response = requests.get(url=df_url, verify=False)
# content = json.loads(response.text)['ApiResults']['scrd']['focus'][1]
# x = content['XData']
# y = content['Ydata']['StockFocus']
# # 每日15:00后会刷新当天的数据
# print(x[0], y[1])


# 比如今日是12月2号，那我要分析的是12月1号9:30之后和12月2号9:30之前这段时间
