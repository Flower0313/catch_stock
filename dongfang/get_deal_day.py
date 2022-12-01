# _*_ coding : utf-8 _*_
# @Time : 2022/7/25 - 11:13
# @Author : Holden
# @File : get_a_stock_hour
# @Project : python
import json
import re

import requests
import pymysql
import datetime
from concurrent.futures import ThreadPoolExecutor


def get_deal_detail(str):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        charset='utf8'
    )
    cursor = conn.cursor()

    params = {
        'secid': str,
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fields1': 'f1,f2,f3,f4',
        'fields2': 'f51,f52,f53,f54,f55',
        'fltt': '2',
        'pos': '-0',
        'wbp2u': '4819115464066356|0|0|0|web',
    }

    cookies = {
        'qgqp_b_id': '110276fdc7a31f5dee37aad9fb4e446a',
        'ct': 'EEIhWo9zu9jtBAmjdkl2YBRq82hgRuqso3qChECmv0WJfiFuRl8IOgcthlInlYMJdK2pkiqhGmhbVqhoDy02sHmRPgKov-Lk48OiVgIeJUzp6emLUbvnf3sHgkTWzT-rYFqHMON2RgEiToOW-O_57LMljhaOPEi0JsXGTcH44ks',
        'ut': 'FobyicMgeV6SKrOicruKo72Vo--axxKGABvmM2iTa7d3SGZEFeomi-JiqMabzBGSKGMZO-TLub02PbweePxPh04gi6Do7TremUC4fA38SLZd20Fkf-QpmUa_u5Y4Bl8J_14Il46DHC2klVCCOs86R7lHzLiP1_RUTrpafGwDKEv01WS_BfOWii0_37rE02Vlnco26NzSNOZJOmw4sbU8fmvEHu8Th0Xto71KwXxlKa4rXNnxXoGYW3V4hWGzd58AoH4BNuO8jfcyE8JZKvlEMIQ2MlJ16gkGketQ4R-6Ygk',
        'uidal': '4819115464066356Holdenxiao',
        'sid': '131578758',
        'vtpst': '%7c',
        'em_hq_fls': 'js',
        'em-quote-version': 'topspeed',
        'emshistory': '%5B%22C%E9%BE%99%E8%8A%AF%22%2C%22%E4%BA%94%E6%B4%B2%E5%8C%BB%E7%96%97%22%2C%22%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A%22%2C%22%E4%B8%AD%E5%9B%BD%E8%BF%9E%E9%80%9A%22%5D',
        'xsb_history': '400071%7C%u4E2D%u5F181',
        'HAList': 'a-sz-000002-%u4E07%20%20%u79D1%uFF21%2Cty-1-688234-%u5929%u5CB3%u5148%u8FDB%2Cty-1-688020-%u65B9%u90A6%u80A1%u4EFD%2Cty-116-01808-%u4F01%u5C55%u63A7%u80A1%2Cty-116-01211-%u6BD4%u4E9A%u8FEA%u80A1%u4EFD%2Ca-sz-002821-%u51EF%u83B1%u82F1%2Ca-sz-002594-%u6BD4%u4E9A%u8FEA%2Cty-1-688607-%u5EB7%u4F17%u533B%u7597%2Ca-sh-600651-%u98DE%u4E50%u97F3%u54CD%2Cty-1-688071-%u534E%u4F9D%u79D1%u6280',
        'st_si': '68436037332696',
        'st_pvi': '99298644841036',
        'st_sp': '2022-05-13%2009%3A41%3A33',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '15',
        'st_psi': '20220725110210279-113200301202-9475732140',
        'st_asi': 'delete',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'http://quote.eastmoney.com/sz000002.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    base_sql_one_kline = '''
                    insert into spider_base.df_a_stock_deal(`market`,`code`,`prePrice`,`current_time`,`deal`,`draw`) values("{}","{}","{}","{}","{}","{}")
                '''

    url = "http://push2.eastmoney.com/api/qt/stock/details/get"
    response = requests.get(url, params=params, cookies=cookies, headers=headers, verify=False)
    result_json = json.loads(response.text)['data']

    for i in result_json['details']:
        trend_result = i.split(',')
        e_sql = base_sql_one_kline.format(result_json['market'], result_json['code'],
                                          result_json['prePrice'], trend_result[0],
                                          trend_result[1], trend_result[2])
        result = re.sub(r"(?<=\")-(?=\")", '0.0', e_sql)
        cursor.execute(result)
        conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='spider_base',
        charset='utf8'
    )

    timez = str(datetime.datetime.now().date())
    sqlcmd = "select market,code from df_a_stock_detail where ds='" + timez + "'"
    cursor = conn.cursor()
    cursor.execute(sqlcmd)
    # 获取数据
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    with ThreadPoolExecutor(20) as t:
        for r in result:
            t.submit(get_deal_detail, str=str(r[0]) + "." + str(r[1]))
