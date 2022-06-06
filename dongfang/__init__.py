# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 10:52
# @Author : Holden
# @File : __init__.py
# @Project : python

import requests
import json
import jsonpath
import re
import datetime
import time

# url = "https://edu.shbytech.com/writeoff/detail/student_lesson_query_page?writeOffStartTime=2022-04-02&writeOffEndTime=2022-04-02&writeOffType=1&pageNum=1&pageSize=928"
#
# headers = {
#     "authorization": "Bearer OTNjMDAwMzctMzQwZS00Y2QyLThjMmEtYWY0ZWFkY2M3ZjFm"
# }
#
# response = requests.get(url=url, headers=headers, verify=False)
#
# content = response.text
# real_json = jsonpath.jsonpath(json.loads(content), '$.data.list[*]')
#
# sum = 0
# i = 0
# hour = 0
# ccc = ""
# for j in real_json:#
#     hour += j.get('lessonHour')
#     i += 1
#     sum += j.get('amount')
#     ccc += str(j.get('studentId')) + ','
# print(i, hour, sum)
# print(ccc)

