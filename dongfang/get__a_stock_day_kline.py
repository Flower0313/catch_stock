# _*_ coding : utf-8 _*_
# @Time : 2022/5/28 - 13:02
# @Author : Holden
# @File : get__a_stock_kline
# @Project : python
# 首次执行即可
import pymysql
import requests
import logging

from concurrent.futures import ThreadPoolExecutor
import json
import datetime

start = datetime.datetime.now()  # 开始时间

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='spider_base',
    charset='utf8'
)

sqlcmd = "select market,code from df_a_stock_detail where ds='2022-07-01' and current_price<>0"
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

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    }

    base_sql_one_kline = '''
            insert into df_a_one_stock_day_kline(market,code,name,dk_total,up_down_rate,up_down_amount,turnover_rate,amplitude,highest,lowest,
        opening_price,closing_price,deal_amount,deal_vol,year,month_day) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
        '''

    base_sql_zero_kline = '''
                insert into df_a_zero_stock_day_kline(market,code,name,dk_total,up_down_rate,up_down_amount,turnover_rate,amplitude,highest,lowest,
            opening_price,closing_price,deal_amount,deal_vol,year,month_day) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
            '''

    # 日k线
    url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"
    response = requests.get(url, params=params, cookies=cookies, headers=headers, verify=False)
    result_json = json.loads(response.text)['data']
    index = 0
    e_sql = ""
    if len(result_json.get('klines')) <= 0:
        return

    for k in result_json.get('klines'):
        index += 1
        klines = k.split(',')
        if 1 == result_json.get('market'):
            e_sql = base_sql_one_kline.format(result_json.get('market'), result_json.get('code'),
                                                    result_json.get('name'),
                                                    result_json.get('dktotal'),
                                                    klines[8], klines[9], klines[10], klines[7],
                                                    klines[3], klines[4], klines[1], klines[2], klines[5], klines[6],
                                                    klines[0][:4], klines[0][5:])
        elif 0 == result_json.get('market'):
            e_sql = base_sql_zero_kline.format(result_json.get('market'), result_json.get('code'),
                                                     result_json.get('name'),
                                                     result_json.get('dktotal'),
                                                     klines[8], klines[9], klines[10], klines[7],
                                                     klines[3], klines[4], klines[1], klines[2], klines[5], klines[6],
                                                     klines[0][:4], klines[0][5:])
        cursor.execute(e_sql)
        # 打印日志
        logging.warning(e_sql)
        conn.commit()
    conn.commit()
    cursor.close()  # 记得释放资源
    conn.close()


# 开启50个线程
if __name__ == '__main__':
    with ThreadPoolExecutor(20) as t:
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
    # print('--运行时间: %s秒--' % (end - start))
