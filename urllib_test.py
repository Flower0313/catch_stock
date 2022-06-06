# _*_ coding : utf-8 _*_
# @Time : 2022/5/15 - 16:02
# @Author : Holden
# @File : urllib_test
# @Project : python

import urllib.request

url = "https://www.baidu.com"
# 找到自己的UA,这是UA反扒
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')  # read返回的是字节形式的二进制数据
# 将二进制数据转换为字符串
print(content)
# response是HTTPResponse的类型
# print(response.getcode()) # 返回状态码
# print(response.getheaders()) # 返回状态信息
# print(response.geturl()) # 返回url地址
