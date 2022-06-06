# _*_ coding : utf-8 _*_
# @Time : 2022/5/17 - 16:20
# @Author : Holden
# @File : 代理
# @Project : python

import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)

# 代理ip
proxies = {
    'http':'117.186.112.42:9999'
}

# 获取handler对象
handler = urllib.request.ProxyHandler(proxies=proxies)

# 获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)

