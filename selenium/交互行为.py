# _*_ coding : utf-8 _*_
# @Time : 2022/5/19 - 18:04
# @Author : Holden
# @File : 交互
# @Project : python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网站
# url = 'http://www.baidu.com'
# 会跳出真正的浏览器
browser.get(url)


# 获取输入框对象
input = browser.find_element(by=By.ID,value='kw')

# 在输入框中输入周杰伦
input.send_keys('高俊峰')

# 休息2秒，模拟人类手速
time.sleep(2)

# 获取“百度一下”按钮
button = browser.find_element(by=By.ID,value='su')

# 点击按钮,就搜索了“肖华”
button.click()

time.sleep(2)

# 滑倒底部
js_bottom = 'document.documentElement.scrollTop=10000'
browser.execute_script(js_bottom)

time.sleep(2)

next = browser.find_element(by=By.XPATH,value='//a[@class="n"]')
# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()

time.sleep(2)

# 回去
browser.forward()

time.sleep(2)
# 退出
browser.quit()
























