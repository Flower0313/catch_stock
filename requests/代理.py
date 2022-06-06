# _*_ coding : utf-8 _*_
# @Time : 2022/5/20 - 14:12
# @Author : Holden
# @File : 代理
# @Project : python
import requests

url = 'http://www.baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

data = {
    'wd': 'ip'
}

prox = {
    'http':''
}

response = requests.get(url=url, params=data, headers=headers,proxies=prox)

content = response.text

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)

