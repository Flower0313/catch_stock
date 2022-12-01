import json
import re

import pymysql as pymysql
import requests
from concurrent.futures import ThreadPoolExecutor

import os
import requests

conn = pymysql.connect(
    host='8.130.49.69',
    port=3306,
    user='root',
    passwd='w654646',
    charset='utf8'
)


def getStocks():
    cursor = conn.cursor()
    cursor.execute("select `code` from spider_base.df_a_stock_detail where ds='2022-11-24' and code='603130'")
    content = cursor.fetchall()
    cursor.close()
    conn.close()
    return list(content)


def getChance(code):
    conn_result = pymysql.connect(
        host='8.130.49.69',
        port=3306,
        user='root',
        passwd='w654646',
        charset='utf8'
    )

    base_sql = '''
               insert into spider_base.df_a_stock_chance(`code`,TOTAL_SCORE,RISE_1_PROBABILITY,AVERAGE_1_INCREASE,RISE_5_PROBABILITY,AVERAGE_5_INCREASE,STOCK_RANK_RATIO,WORDS_EXPLAIN,notice_date) 
               VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}")
    '''

    cookies = {
        'qgqp_b_id': '110276fdc7a31f5dee37aad9fb4e446a',
        'ct': 'EEIhWo9zu9jtBAmjdkl2YBRq82hgRuqso3qChECmv0WJfiFuRl8IOgcthlInlYMJdK2pkiqhGmhbVqhoDy02sHmRPgKov-Lk48OiVgIeJUzp6emLUbvnf3sHgkTWzT-rYFqHMON2RgEiToOW-O_57LMljhaOPEi0JsXGTcH44ks',
        'ut': 'FobyicMgeV6SKrOicruKo72Vo--axxKGABvmM2iTa7d3SGZEFeomi-JiqMabzBGSKGMZO-TLub02PbweePxPh04gi6Do7TremUC4fA38SLZd20Fkf-QpmUa_u5Y4Bl8J_14Il46DHC2klVCCOs86R7lHzLiP1_RUTrpafGwDKEv01WS_BfOWii0_37rE02Vlnco26NzSNOZJOmw4sbU8fmvEHu8Th0Xto71KwXxlKa4rXNnxXoGYW3V4hWGzd58AoH4BNuO8jfcyE8JZKvlEMIQ2MlJ16gkGketQ4R-6Ygk',
        'uidal': '4819115464066356Holdenxiao',
        'sid': '131578758',
        'vtpst': '%7c',
        'em_hq_fls': 'js',
        'em-quote-version': 'topspeed',
        'xsb_history': '400071%7C%u4E2D%u5F181',
        'mtp': '1',
        'EMFUND1': 'null',
        'EMFUND2': 'null',
        'EMFUND3': 'null',
        'EMFUND4': 'null',
        'EMFUND5': 'null',
        'EMFUND6': 'null',
        'EMFUND7': 'null',
        'EMFUND8': 'null',
        'emshistory': '%5B%22%E8%8A%82%E8%83%BD%E9%A3%8E%E7%94%B5%22%2C%22000638%22%2C%22%E4%B8%9C%E6%96%B9%E9%9B%A8%E8%99%B9%22%2C%22301266%22%2C%22%E7%91%9E%E6%B3%B0%E6%96%B0%E6%9D%90%22%2C%22688349%22%2C%22C%E9%BE%99%E8%8A%AF%22%2C%22%E4%BA%94%E6%B4%B2%E5%8C%BB%E7%96%97%22%2C%22%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A%22%2C%22%E4%B8%AD%E5%9B%BD%E8%BF%9E%E9%80%9A%22%5D',
        'st_si': '57927427544532',
        'HAList': 'ty-1-600222-%u592A%u9F99%u836F%u4E1A%2Cty-1-605136-%u4E3D%u4EBA%u4E3D%u5986%2Cty-0-002181-%u7CA4%20%u4F20%20%u5A92%2Cty-0-002467-%u4E8C%u516D%u4E09%2Cty-0-300454-%u6DF1%u4FE1%u670D%2Cty-1-603176-%u6C47%u901A%u96C6%u56E2%2Cty-1-600301-%u5357%u5316%u80A1%u4EFD%2Cty-0-301377-N%u9F0E%u6CF0%2Cty-0-300772-%u8FD0%u8FBE%u80A1%u4EFD%2Cty-1-601016-%u8282%u80FD%u98CE%u7535',
        'st_asi': 'delete',
        'guba_blackUserList': '',
        'st_pvi': '99298644841036',
        'st_sp': '2022-05-13%2009%3A41%3A33',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '23',
        'st_psi': '20221124140927885-113300302193-0761584642',
        'JSESSIONID': '56376599E91B145EFB8B967D89358F81',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://data.eastmoney.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params1 = {
        'filter': '(SECURITY_CODE="' + str(code) + '")',
        'columns': 'ALL',
        'source': 'WEB',
        'client': 'WEB',
        'reportName': 'RPT_CUSTOM_STOCK_PK',  # type
        '_': '1669270208096',
    }

    params2 = {
        'filter': '(SECURITY_CODE="' + str(code) + '")',
        'columns': 'ALL',
        'source': 'WEB',
        'client': 'WEB',
        'reportName': 'RPT_STOCK_CHANGERATE',  # type
        '_': '1669270208096',
    }

    url = 'http://datacenter-web.eastmoney.com/api/data/v1/get'
    response1 = requests.get(url, params=params1, cookies=cookies, headers=headers, verify=False)
    response2 = requests.get(url, params=params2, cookies=cookies, headers=headers, verify=False)
    if not json.loads(response1.text)['success']:
        content1 = None
    else:
        content1 = json.loads(response1.text)['result']['data'][0]

    if not json.loads(response2.text)['success']:
        content2 = json.loads(
            '{"RISE_1_PROBABILITY":-1,"AVERAGE_1_INCREASE":-1,"RISE_5_PROBABILITY":-1,"AVERAGE_5_INCREASE":-1}')
    else:
        content2 = json.loads(response2.text)['result']['data'][0]

    cursor = conn_result.cursor()
    if content1 is not None or content2 is not None:
        e_sql = base_sql.format(code, content1.get('TOTAL_SCORE'), content2.get('RISE_1_PROBABILITY'),
                                content2.get('AVERAGE_1_INCREASE'),
                                content2.get('RISE_5_PROBABILITY'), content2.get('AVERAGE_5_INCREASE'),
                                content1.get('STOCK_RANK_RATIO'),
                                content1.get('WORDS_EXPLAIN'), str(content1.get('DIAGNOSE_TIME')).split(" ")[0])
        cursor.execute(e_sql)
        conn_result.commit()
    cursor.close()
    conn_result.close()


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for stock in getStocks():
            t.submit(getChance, stock[0])
