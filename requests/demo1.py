# _*_ coding : utf-8 _*_
# @Time : 2022/5/20 - 0:05
# @Author : Holden
# @File : demo1
# @Project : python

import requests

url = "https://www.baidu.com"

response = requests.get(url)

response.encoding = 'utf-8'

# 一个类型和六个属性

print(type(response))

print(response.text) # 网页源码
print(response.url) # 返回一个url地址
print(response.content) # 网页二进制内容
print(response.status_code) # 响应状态码
print(response.headers) # 响应头信息

