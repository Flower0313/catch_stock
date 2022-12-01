# _*_ coding : utf-8 _*_
# @Time : 2022/5/28 - 13:02
# @Author : Holden
# @File : get__a_stock_kline
# @Project : python
# 首次执行即可
import datetime
import re

import pymysql
import requests

from concurrent.futures import ThreadPoolExecutor
import json


def get_all_kline(str):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='spider_base',
        charset='utf8'
    )

    cursor = conn.cursor()
    # 必须放在线程里面
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
        'st_si': '15412442463721',
        'st_asi': 'delete',
        'HAList': 'ty-1-000001-%u4E0A%u8BC1%u6307%u6570%2Cty-1-688020-%u65B9%u90A6%u80A1%u4EFD%2Cty-1-600718-%u4E1C%u8F6F%u96C6%u56E2%2Cty-0-002690-%u7F8E%u4E9A%u5149%u7535%2Cty-0-301266-%u5B87%u90A6%u65B0%u6750%2Cty-1-688112-%u9F0E%u9633%u79D1%u6280%2Ca-sz-000651-%u683C%u529B%u7535%u5668%2Ca-sz-301266-%u5B87%u90A6%u65B0%u6750%2Cty-1-600268-%u56FD%u7535%u5357%u81EA%2Cty-1-688371-%u83F2%u6C83%u6CF0',
        'st_pvi': '99298644841036',
        'st_sp': '2022-05-13%2009%3A41%3A33',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '13',
        'st_psi': '20220817103728733-113200302671-9133659144',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    cookies = {
        'qgqp_b_id': '110276fdc7a31f5dee37aad9fb4e446a',
        'ct': 'EEIhWo9zu9jtBAmjdkl2YBRq82hgRuqso3qChECmv0WJfiFuRl8IOgcthlInlYMJdK2pkiqhGmhbVqhoDy02sHmRPgKov-Lk48OiVgIeJUzp6emLUbvnf3sHgkTWzT-rYFqHMON2RgEiToOW-O_57LMljhaOPEi0JsXGTcH44ks',
        'ut': 'FobyicMgeV6SKrOicruKo72Vo--axxKGABvmM2iTa7d3SGZEFeomi-JiqMabzBGSKGMZO-TLub02PbweePxPh04gi6Do7TremUC4fA38SLZd20Fkf-QpmUa_u5Y4Bl8J_14Il46DHC2klVCCOs86R7lHzLiP1_RUTrpafGwDKEv01WS_BfOWii0_37rE02Vlnco26NzSNOZJOmw4sbU8fmvEHu8Th0Xto71KwXxlKa4rXNnxXoGYW3V4hWGzd58AoH4BNuO8jfcyE8JZKvlEMIQ2MlJ16gkGketQ4R-6Ygk',
        'uidal': '4819115464066356Holdenxiao',
        'sid': '131578758',
        'vtpst': '%7c',
        'em_hq_fls': 'js',
        'qquestionnairebox': '1',
        'em-quote-version': 'topspeed',
        'st_si': '32426815590998',
        'st_asi': 'delete',
        'HAList': 'a-sz-300010-%u8C46%u795E%u6559%u80B2%2Ca-sh-600962-%u56FD%u6295%u4E2D%u9C81%2Cty-0-430510-%u4E30%u5149%u7CBE%u5BC6%2Cty-0-835640-%u5BCC%u58EB%u8FBE%2Cty-0-833266-%u751F%u7269%u8C37%2Ca-sh-600721-%u767E%u82B1%u6751%2Ca-sz-002213-%u5927%u4E3A%u80A1%u4EFD%2Ca-sz-003032-%u4F20%u667A%u6559%u80B2%2Ca-sz-002523-%u5929%u6865%u8D77%u91CD%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-002821-%u51EF%u83B1%u82F1',
        'st_pvi': '99298644841036',
        'st_sp': '2022-05-13%2009%3A41%3A33',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '48',
        'st_psi': '20220528130858545-113200301201-6079724835',
    }

    params = {
        'secid': str,
        'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
        'fields1': 'f1,f2,f3,f4,f5,f6',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'klt': '101',
        'fqt': '1',
        'end': '20500101',
        'lmt': '5',
        '_': '1660703848550',
    }

    base_sql_zero_kline = '''
                insert into spider_base.df_a_index_day_kline(`market`,`index`,`name`,`opening_price`,`closing_price`,`highest`,`lowest`,`deal_vol`,`deal_amount`,
            `amplitude`,`up_down_rate`,`up_down_amount`,`turnover_rate`,`date`) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
            '''

    # 日k线
    url = "http://41.push2his.eastmoney.com/api/qt/stock/kline/get"
    response = requests.get(url, params=params, cookies=cookies, headers=headers, verify=False)
    result_json = json.loads(response.text)['data']
    if len(result_json.get('klines')) <= 0:
        return

    for k in result_json.get('klines'):
        klines = k.split(',')
        e_sql = base_sql_zero_kline.format(result_json.get('market'), result_json.get('code'),
                                           result_json.get('name'),
                                           klines[1], klines[2], klines[3], klines[4],
                                           klines[5], klines[6], klines[7], klines[8], klines[9], klines[10], klines[0])
        result = re.sub(r"(?<=\")-(?=\")", '0.0', e_sql)
        cursor.execute(result)
        conn.commit()
    conn.commit()
    cursor.close()  # 记得释放资源
    conn.close()


# 开启50个线程
if __name__ == '__main__':
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='spider_base',
        charset='utf8'
    )
    indexs = ['1.000001', '0.399001', '0.399005', '0.399006', '1.000300']

    with ThreadPoolExecutor(20) as t:
        for r in indexs:
            t.submit(get_all_kline, str=str(r))
