# _*_ coding : utf-8 _*_
# @Time : 2022/5/17 - 21:20
# @Author : Holden
# @File : xpath的基本使用
# @Project : python

from lxml import etree

# 解析本地的html文件,注意其中没有标签都要成对出现
tree = etree.parse('xpath.html')

'''
xpath基本语法
//是查询所有子孙节点，不考虑层级关系
/是直接子节点


'''
# 查找ul标签下的li
li_list = tree.xpath('//body/ul/li')
li_list2 = tree.xpath('//ul/li[@id]/text()') # 查找有id属性的li标签，text()是获取标签内容
print(li_list2)

# 找到id为l1的li标签
li_list3 = tree.xpath('//ul/li[@id="l1"]/text()')
print(li_list3)

# 查找到id为l1的li标签的class的属性值
li = tree.xpath('//ul/li[@id="l1"]/@class')
print(len(li))

# 查询id中包含l的标签，模糊查询
li_mo = tree.xpath('//ul/li[contains(@id,"l")]')
print(len(li_mo))





