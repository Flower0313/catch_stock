# _*_ coding : utf-8 _*_
# @Time : 2022/5/15 - 17:43
# @Author : Holden
# @File : urllib_test2
# @Project : python

import urllib.request

# 下载网页
url_page = "https://www.baidu.com"
url_pic = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fblog%2F202106%2F14%2F20210614102145_720d0.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1655203253&t=376b20b35adffddd096ea1696795528c"
# 在python中可以写变量的名字，也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')


# 下载图片
urllib.request.urlretrieve(url_pic,'lisa.jpg')

# 下载视频


