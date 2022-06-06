# _*_ coding : utf-8 _*_
# @Time : 2022/5/19 - 16:18
# @Author : Holden
# @File : selenium元素定位
# @Project : python

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器操作对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网站
url = 'http://www.baidu.com'
# 会跳出真正的浏览器
browser.get(url)

# 获取百度一下的按钮,根据标签属性的属性值来获取对象的
button = browser.find_element(by=By.ID,value="su") # 根据id来获取
button2 = browser.find_element(by=By.XPATH,value='//input[@id="su"]') # 根据xpath来获取
button3 = browser.find_element(by=By.TAG_NAME,value='input') # 根据标签来获取
button4 = browser.find_element(by=By.CSS_SELECTOR,value='#su') # 根据css选择器来获取
button5 = browser.find_element(by=By.LINK_TEXT,value='网盘')
print(button5)
















