# _*_ coding : utf-8 _*_
# @Time : 2022/5/20 - 14:03
# @Author : Holden
# @File : post
# @Project : python

import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

data = {
    'kw': 'eye'
}

response = requests.post(url=url,data=data,headers=headers)

content = response.text

# 转为编码格式
obj = json.loads(content,encoding='utf-8')
print(obj)
