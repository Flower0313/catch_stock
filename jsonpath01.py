# _*_ coding : utf-8 _*_
# @Time : 2022/5/18 - 16:53
# @Author : Holden
# @File : jsonpath01
# @Project : python
# example:https://blog.csdn.net/I_r_o_n_M_a_n/article/details/123187332

import jsonpath
import json

obj = json.load(open('books.json','r',encoding='utf-8'))


# 书店所有书的作者
book_author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')

# 获取所有的作者
author_list = jsonpath.jsonpath(obj,'$..author')

# store下面所有的元素
tag_list = jsonpath.jsonpath(obj,'$.store.*')

# 条件过滤需要在()前面添加一个?
jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')


print(tag_list)






