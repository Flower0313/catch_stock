# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 10:08
# @Author : Holden
# @File : dongfang
# @Project : python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网站
url = 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
# 会跳出真正的浏览器
browser.get(url)

last_page = browser.find_element(by=By.XPATH,
                                 value='//div[@id="main-table_paginate"]/span[@class="paginate_page"]/a[last()]')

# 点击下一页
last_page.click()

print(browser.page_source)




