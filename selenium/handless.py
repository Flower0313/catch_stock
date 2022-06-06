# _*_ coding : utf-8 _*_
# @Time : 2022/5/19 - 21:19
# @Author : Holden
# @File : handless
# @Project : python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    path = r'D:\Google\chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


url = 'https://www.baidu.com'

browser = share_browser()

browser.get(url)

browser.save_screenshot('baidu.png')

# 封装handless
