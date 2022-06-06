# _*_ coding : utf-8 _*_
# @Time : 2022/5/15 - 21:21
# @Author : Holden
# @File : urllib_xh
# @Project : python - get请求

import urllib.request
import urllib.parse

# 将汉字变为unicode编码:urllib.parse.quote('肖华')
# urlencode应用场景：多个参数的时候


# 找到自己的UA,这是UA反扒
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
# 参数

datas = {
    'wd':'肖华',
    'sex':'女'
}
url = "https://www.baidu.com/s?" + str(urllib.parse.urlencode(datas))

# 定制请求对象
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
