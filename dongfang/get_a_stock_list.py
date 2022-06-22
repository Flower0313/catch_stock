# _*_ coding : utf-8 _*_
# @Time : 2022/5/20 - 0:36
# @Author : Holden
# @File : get
# @Project : python

import requests
import jsonpath
import json
from dongfang.Stock import Stock
import pymysql
import re
import datetime
import logging


def catch_stock(timex):
    url = 'http://2.push2.eastmoney.com/api/qt/clist/get'
    # 获取股票的总数
    a_stock_nums = Stock.get_a_stock_num()

    cookies = {
        'qgqp_b_id': '110276fdc7a31f5dee37aad9fb4e446a',
        'ct': 'EEIhWo9zu9jtBAmjdkl2YBRq82hgRuqso3qChECmv0WJfiFuRl8IOgcthlInlYMJdK2pkiqhGmhbVqhoDy02sHmRPgKov-Lk48OiVgIeJUzp6emLUbvnf3sHgkTWzT-rYFqHMON2RgEiToOW-O_57LMljhaOPEi0JsXGTcH44ks',
        'ut': 'FobyicMgeV6SKrOicruKo72Vo--axxKGABvmM2iTa7d3SGZEFeomi-JiqMabzBGSKGMZO-TLub02PbweePxPh04gi6Do7TremUC4fA38SLZd20Fkf-QpmUa_u5Y4Bl8J_14Il46DHC2klVCCOs86R7lHzLiP1_RUTrpafGwDKEv01WS_BfOWii0_37rE02Vlnco26NzSNOZJOmw4sbU8fmvEHu8Th0Xto71KwXxlKa4rXNnxXoGYW3V4hWGzd58AoH4BNuO8jfcyE8JZKvlEMIQ2MlJ16gkGketQ4R-6Ygk',
        'uidal': '4819115464066356Holdenxiao',
        'sid': '131578758',
        'vtpst': '%7c',
        'HAList': 'a-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Cty-1-000001-%u4E0A%u8BC1%u6307%u6570',
        'em_hq_fls': 'js',
        'st_si': '28391038832023',
        'st_asi': 'delete',
        'st_pvi': '99298644841036',
        'st_sp': '2022-05-13%2009%3A41%3A33',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '8',
        'st_psi': '20220525102716256-113200301321-2733745278',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': '69.push2.eastmoney.com',
        'Pragma': 'no-cache',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    data = {
        'pn': 1,
        'pz': a_stock_nums,
        'np': 1,
        'po': 1,
        'np': 1,
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': 2,
        'invt': 2,
        'wbp2u': '4819115464066356|0|0|0|web',
        'fid': 'f3',
        'fs': 'm:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048',
        'fields': 'f1,f12,f13,f14,f2,f3,f4,f8,f9,f7,f10,f15,f16,f17,f18,f20,f21,f23,f25,f26,f35,f34,f37,f38,f39,f40,f46,f49,f50,f57,f62,f97,f98,f99,f100,f102,f112,f114,f115,f135',
        '_': timex

    }

    response = requests.get(url=url, params=data, headers=headers, cookies=cookies, verify=False)

    content = response.text
    real_json = jsonpath.jsonpath(json.loads(content), '$.data.diff[*]')

    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='spider_base',
        charset='utf8'
    )

    cursor = conn.cursor()
    index = 0
    for j in real_json:
        index += 1
        e_sql = Stock.base_sql.format(Stock.verify_code(j.get('f12')), j.get('f13'), j.get('f12'), j.get('f14'),
                                      j.get('f2'),
                                      j.get('f4'), j.get('f8'), j.get('f3'),
                                      j.get('f9'), j.get('f7'), j.get('f10'), j.get('f15'), j.get('f16'), j.get('f17'),
                                      j.get('f18'), j.get('f20'), j.get('f21'), j.get('f23'), j.get('f25'),
                                      j.get('f26'),
                                      j.get('f34'), j.get('f35'), j.get('f37'), j.get('f38'), j.get('f39'),
                                      j.get('f40'),
                                      j.get('f46'), j.get('f49'), j.get('f50'), j.get('f57'), j.get('f62'),
                                      j.get('f97'),
                                      j.get('f98'), j.get('f99'), j.get('f100'), j.get('f102'), j.get('f103'),
                                      j.get('f112'),
                                      j.get('f114'), j.get('f115'), j.get('f135'),
                                      str(datetime.datetime.utcfromtimestamp(timex / 1000).strftime("%Y-%m-%d"))
                                      )

        result = re.sub(r"(?<=\")-(?=\")", '0.0', e_sql)
        cursor.execute(result)

        # 分批次提交，加快写入速度
        if index % 500 == 0:
            conn.commit()
    # 爬取完关闭连接
    conn.commit()  # 将剩余的提交
    cursor.close()
    conn.close()
    logging.warning("执行完毕")