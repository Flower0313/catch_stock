# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 22:40
# @Author : Holden
# @File : test
# @Project : python

import requests
import jsonpath
import json
from datetime import datetime

from dongfang.get_a_stock_list import catch_stock
import time

if str(datetime.now().weekday() + 1) not in ("7", "6"):
    catch_stock((int(time.mktime(time.localtime(time.time())))) * 1000)
