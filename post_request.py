# _*_ coding : utf-8 _*_
# @Time : 2022/5/16 - 0:15
# @Author : Holden
# @File : post请求
# @Project : python

import urllib.request
import urllib.parse
import json

url = "https://fanyi.baidu.com/sug"

# 请求UA
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

# 参数
data = {
    'kw':'spider'
}

# post请求，必须要进行编码
datas = urllib.parse.urlencode(data).encode('utf-8')
print(datas)

# post请求的参数，是不会拼接在url后面的，而是需要放在请求对象定制的参数中，这是与get请求不同的地方
request = urllib.request.Request(url=url,data=datas,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)
print(obj)
