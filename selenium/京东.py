# _*_ coding : utf-8 _*_
# @Time : 2022/5/19 - 14:13
# @Author : Holden
# @File : 京东selenium
# @Project : python

# 导入selenium
from selenium import webdriver

# 创建浏览器操作对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网站
url = 'http://www.jd.com'
# 会跳出真正的浏览器
browser.get(url)

content = browser.page_source
print(content)




