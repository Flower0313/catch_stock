# _*_ coding : utf-8 _*_
# @Time : 2022/5/19 - 17:27
# @Author : Holden
# @File : 元素信息交互
# @Project : python

from selenium import webdriver
from selenium.webdriver.common.by import By

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网站
url = 'http://www.baidu.com'
# 会跳出真正的浏览器
browser.get(url)

input = browser.find_element(by=By.ID,value='su')
# 找到标签的属性名
print(input.get_attribute('class')) # 元素属性
print(input.tag_name) # 元素签名
print(input.text)# 元素文本





