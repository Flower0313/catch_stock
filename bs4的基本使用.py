# _*_ coding : utf-8 _*_
# @Time : 2022/5/18 - 23:42
# @Author : Holden
# @File : bs4的基本使用
# @Project : python

from bs4 import BeautifulSoup
import urllib.request

# 默认打开的编码格式是gbk
soup = BeautifulSoup(open('xpath.html',encoding='utf-8'),'lxml')

# select方法返回的是列表，会返回多个数据

# 服务器响应的文件生成对象
