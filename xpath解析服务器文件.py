# _*_ coding : utf-8 _*_
# @Time : 2022/5/18 - 9:46
# @Author : Holden
# @File : xpath解析服务器文件
# @Project : python

import urllib.request
import urllib.parse
from lxml import etree


url = "http://www.baidu.com/"

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

# 获取网页源码

content = response.read().decode('utf-8')

# 解析网络源码
tree = etree.HTML(content)

# xpath返回值是列表类型数据
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)







