# _*_ coding : utf-8 _*_
# @Time : 2022/5/17 - 14:34
# @Author : Holden
# @File : 微博cookie
# @Project : python

import urllib.request
import urllib.parse

url = "https://weibo.com/ajax/profile/info?uid=6033930102"

# cookie中携带着你的登陆信息
headers = {
    'referer': 'https://weibo.com/u/6033930102',
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'cookie': 'UOR=www.baidu.com,weibo.com,www.baidu.com; SINAGLOBAL=6964553201904.971.1641486698421; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFnV0VFhTwM3puuNT0OsNqZ5JpX5KMhUgL.Foq7e0e4e05pehz2dJLoI7v0eGiEwHxa9P9LMrLldJ-t; ULV=1644739376707:4:3:1:7764694117248.98.1644739376573:1644665543469; PC_TOKEN=d12edca84e; ALF=1684305338; SSOLoginState=1652769337; SCF=Am_9aMRmAN5SigySto2OiwshWCTunTS3wLNSOJm8r_HY_3BbT0iw85lSWnSqfcqVasUVX0AHn6oWvjZFbsjq0Lo.; SUB=_2A25PhzJnDeRhGeBO6FEY8y7Nyz6IHXVs9SSvrDV8PUNbmtB-LUnmkW9NSgVY5wg5hy_h9Wvsd-8G7H98aPognDeD; XSRF-TOKEN=5Gin3NFMUs2s7hyeU-g-wEHw; WBPSESS=oH0dz8c-Ry284eRmyR4HnD29XkQBxYQcp6aUYatJAWsQeQf5XQzyn2GHK3tf1Bw75lmvHLf82n5ep5RgDOxhe89H8XZW7_fVDbx7T5dzUocSIDskjNbZqRV75fmyItF2-q9_MOfsVw-XFya6-bEk_Q=='
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级...')
