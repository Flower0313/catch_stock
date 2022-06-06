# _*_ coding : utf-8 _*_
# @Time : 2022/5/17 - 15:54
# @Author : Holden
# @File : hander使用
# @Project : python

import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)

# 获取handler对象
handler = urllib.request.HTTPHandler()

# 获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)
