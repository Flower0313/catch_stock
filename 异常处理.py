# _*_ coding : utf-8 _*_
# @Time : 2022/5/17 - 14:15
# @Author : Holden
# @File : 异常处理
# @Project : python

import urllib.request
import urllib.error

url = "https://blog.csdn.net/qq_41684621/article/details/113851644"

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级...')

