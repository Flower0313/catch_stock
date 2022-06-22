# _*_ coding : utf-8 _*_
# @Time : 2022/5/28 - 13:02
# @Author : Holden
# @File : get__a_stock_kline
# @Project : python
# 首次执行即可
import pymysql
import requests
import logging

from dongfang.Stock import Stock
from concurrent.futures import ThreadPoolExecutor
import jsonpath
import json
import datetime
import time

start = datetime.datetime.now()  # 开始时间

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='spider_base',
    charset='utf8'
)

sqlcmd = "select market,code from df_a_stock_detail where ds='2022-06-22' and current_price<>0"
cursor = conn.cursor()
cursor.execute(sqlcmd)
# 获取数据
result = cursor.fetchall()


def get_all_kline(str, conn):
    # 线程中的对象不能共用，必须每个线程特有才行
    cursor = conn.cursor()
    # 必须放在线程里面
    params = {
        'secid': str,
        'ut': '7eea3edcaed734bea9cbfc24409ed989',
        'fields1': 'f1,f2,f3,f4,f5,f6',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'klt': '101',  # 日k线
        'fqt': '1', # 1才是真实的k线
        'beg': '0',
        'end': '20500101',
        '_': '1655883377857',
    }

    # 日k线
    url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"
    response = requests.get(url, params=params, cookies=Stock.cookies, headers=Stock.headers, verify=False)
    result_json = jsonpath.jsonpath(json.loads(response.text), '$.data')[0]
    index = 0
    e_sql = ""
    if len(result_json.get('klines')) <= 0:
        return

    for k in result_json.get('klines'):
        index += 1
        klines = k.split(',')
        if 1 == result_json.get('market'):
            e_sql = Stock.base_sql_one_kline.format(result_json.get('market'), result_json.get('code'),
                                                    result_json.get('name'),
                                                    result_json.get('dktotal'),
                                                    klines[8], klines[9], klines[10], klines[7],
                                                    klines[3], klines[4], klines[1], klines[2], klines[5], klines[6],
                                                    klines[0][:4], klines[0][5:])
        elif 0 == result_json.get('market'):
            e_sql = Stock.base_sql_zero_kline.format(result_json.get('market'), result_json.get('code'),
                                                     result_json.get('name'),
                                                     result_json.get('dktotal'),
                                                     klines[8], klines[9], klines[10], klines[7],
                                                     klines[3], klines[4], klines[1], klines[2], klines[5], klines[6],
                                                     klines[0][:4], klines[0][5:])
        cursor.execute(e_sql)
        # 打印日志
        logging.warning(e_sql)
        # 批次大小500一批次
        if index % 500 == 0:
            conn.commit()
    conn.commit()
    cursor.close()  # 记得释放资源
    conn.close()


# 开启50个线程
with ThreadPoolExecutor(50) as t:
    for r in result:
        t.submit(get_all_kline, str=str(r[0]) + "." + str(r[1]), conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='spider_base',
            charset='utf8'
        ))

cursor.close()
conn.close()
end = datetime.datetime.now()  # 结束时间
print('--运行时间: %s秒--' % (end - start))
