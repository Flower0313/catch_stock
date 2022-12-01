# _*_ coding : utf-8 _*_
# @Time : 2022/5/18 - 9:46
# @Author : Holden
# @File : xpath解析服务器文件
# @Project : python

import urllib.request
import urllib.parse
from lxml import etree

comment_url = "https://guba.eastmoney.com/list,603719_1.html"
df_url = "https://data.eastmoney.com/stockcomment/api/603719.json"

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

# 请求对象定制
request = urllib.request.Request(url=comment_url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 解析网络源码
tree = etree.HTML(content)
# xpath返回值是列表类型数据
title = tree.xpath('//div[contains(@class,"articleh normal_post")]/span[contains(@class,"l3 a3")]/a/@title')
timez = tree.xpath('//div[contains(@class,"articleh normal_post")]/span[contains(@class,"l5 a5")]/text()')

# 比如今日是12月2号，那我要分析的是12月1号9:30之后和12月2号9:30之前这段时间
follow_count = 0
for i in range(len(timez)):
    if str(timez[i]) < '12-01 09:20:00':
        follow_count += 1

print(follow_count)
