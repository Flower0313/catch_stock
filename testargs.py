# _*_ coding : utf-8 _*_
# @Time : 2022/7/2 - 22:08
# @Author : Holden
# @File : testargs
# @Project : python

import requests
import time
import json
import datetime

url_str = "http://datacenter-web.eastmoney.com/api/data/v1/get?pageSize=1&columns=SECURITY_CODE%2CSECUCODE%2CSECURITY_NAME_ABBR%2CEVENT_TYPE%2CEVENT_CONTENT%2CTRADE_DATE&filter=(TRADE_DATE='" + str(
    datetime.datetime.now().date()) + "')&reportName=RPT_SPECIAL_ALL"
response = requests.get(url=url_str)
result_json = json.loads(response.text)
if result_json['success']:
    print("好的")
else:
    print("不好的")


