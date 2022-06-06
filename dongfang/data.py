# _*_ coding : utf-8 _*_
# @Time : 2022/6/4 - 17:57
# @Author : Holden
# @File : data
# @Project : python


import datetime as dt
import requests
import json
import jsonpath
import pymysql

begin = dt.date(2002, 1, 1)
end = dt.date(2022, 12, 31)

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='spider_base',
    charset='utf8'
)
cursor = conn.cursor()
sql = '''
        insert into df_calendar values("{}","{}","{}","{}","{}","{}","{}","{}")
    '''

for i in range((end - begin).days + 1):
    day = begin + dt.timedelta(days=i)
    date = str(day).replace("-", "")
    response = requests.get(
        url="https://www.mxnzp.com/api/holiday/single/" + date + "?ignoreHoliday=false&app_id=qlghogigifeejhlk&app_secret=bkRNWC9SUmhBeEdPQ3BSeTdwaGF1UT09")
    dateJson = json.loads(response.text)
    if dateJson['code'] == 0:
        url = "https: // wannianrili.bmcx.com / ajax /?q = 1991 - 12 & v = 20031912"
        pass
    else:
        print(dateJson['data'])
        d = dateJson['data']['date']
        weekday = dateJson['data']['weekDay']
        type = dateJson['data']['type']
        typeDes = dateJson['data']['typeDes']
        chineseZodiac = dateJson['data']['chineseZodiac']
        dayOfYear = dateJson['data']['dayOfYear']
        weekOfYear = dateJson['data']['weekOfYear']
        indexWorkDayOfMonth = dateJson['data']['indexWorkDayOfMonth']
        e_sql = sql.format(d, weekday, type, typeDes, chineseZodiac, dayOfYear, weekOfYear, indexWorkDayOfMonth)
        cursor.execute(e_sql)
        conn.commit()
cursor.close()
conn.close()
