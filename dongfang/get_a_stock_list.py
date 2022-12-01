# _*_ coding : utf-8 _*_
# @Time : 2022/5/20 - 0:36
# @Author : Holden
# @File : get
# @Project : python
import logging

import requests
import json
import pymysql
import re
import datetime
import time

# reload(sys)
# sys.setdefaultencoding('utf8')
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    charset='utf8'
)


def get_a_stock_num():
    a_url = 'http://4.push2.eastmoney.com/api/qt/clist/get?pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=4819115464066356|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1&_=' + str(
        int(time.mktime(time.localtime(time.time()))) * 1000)
    response = requests.get(url=a_url)
    content = response.text
    target_json = json.loads(content)

    return target_json.get('data').get('total')


def if_catch():
    # 获取股票日历中的有无数据
    url_str = "http://datacenter-web.eastmoney.com/api/data/v1/get?pageSize=1&columns=SECURITY_CODE%2CSECUCODE%2CSECURITY_NAME_ABBR%2CEVENT_TYPE%2CEVENT_CONTENT%2CTRADE_DATE&filter=(TRADE_DATE='" + str(
        datetime.datetime.now().date()) + "')&reportName=RPT_SPECIAL_ALL"
    response = requests.get(url=url_str)
    result_json = json.loads(response.text)
    # 若休市就不会爬取股票了
    if result_json['success']:
        return True
    else:
        return False


def stock_calendar_a():
    url_str = "http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1799_jyrl&txtFsrq=" + str(
        datetime.datetime.now().date())
    response = requests.get(url=url_str)
    result_json = json.loads(response.text)
    return result_json[0]['data'] != []


def catch_stock(timex):
    url = 'http://2.push2.eastmoney.com/api/qt/clist/get'
    a_stock_nums = get_a_stock_num()

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
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': 2,
        'invt': 2,
        'wbp2u': '4819115464066356|0|0|0|web',
        'fid': 'f3',
        'fs': 'm:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048',
        'fields': 'f13,f12,f14,f2,f3,f109,f160,f4,f8,f9,f7,f10,f15,f16,f17,f18,f19,f20,f21,f23,f25,f26,f34,f35,f37,f38,f39,f40,f41,f49,f50,f57,f100,f102,f112,f114,f115,f135,f6,f5,f292,f33,f129,f44,f113,f45,f46,f48,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87',
        '_': timex

    }

    base_sql = '''
            insert into spider_base.df_a_stock_detail(market,`code`,`name`,current_price,up_down_rate,up_down_rate5,up_down_rate10,up_down_amount,turnover_rate,
            PE_ratio_d,amplitude,volume_ratio,highest,lowest,opening_price,t_1_price,total_market_v,circulation_market_v,price_to_b_ratio,increase_this_year,
            time_to_market,outer_disk,inner_disk,roe,total_share_capital,tradable_shares,total_revenue,total_revenue_r,gross_profit_margin,total_assets,debt_ratio,
            industry,regional_plate,profit,PE_ratio_s,ttm,net_assets,deal_amount,deal_vol,dealTradeStae,commission,net_margin,total_profit,net_assets_per_share,
            net_profit,net_profit_r,unearnings_per_share,main_inflow,main_inflow_ratio,Slarge_inflow,Slarge_inflow_ratio,large_inflow,large_inflow_ratio,mid_inflow,
            mid_inflow_ratio,small_inflow,small_inflow_ratio,board,ds) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
        "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
        "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
        "{}","{}","{}","{}","{}","{}")
        '''

    response = requests.get(url=url, params=data, headers=headers, cookies=cookies, verify=False)

    real_json = json.loads(response.text)['data']['diff']

    cursor = conn.cursor()
    for j in real_json:
        e_sql = base_sql.format(j.get('f13'), j.get('f12'), j.get('f14'),
                                j.get('f2'), j.get('f3'), j.get('f109'), j.get('f160'), j.get('f4'),
                                j.get('f8'), j.get('f9'), j.get('f7'), j.get('f10'), j.get('f15'),
                                j.get('f16'), j.get('f17'), j.get('f18'), j.get('f20'), j.get('f21'),
                                j.get('f23'), j.get('f25'), j.get('f26'), j.get('f34'), j.get('f35'),
                                j.get('f37'), j.get('f38'), j.get('f39'), j.get('f40'), j.get('f41'),
                                j.get('f49'), j.get('f50'), j.get('f57'), j.get('f100'), j.get('f102'),
                                j.get('f112'), j.get('f114'), j.get('f115'), j.get('f135'),
                                j.get('f6'), j.get('f5'), j.get('f292'), j.get('f33'), j.get('f129'),
                                j.get('f44'), j.get('f113'), j.get('f45'), j.get('f46'), j.get('f48'),
                                j.get('f62'), j.get('f184'), j.get('f66'), j.get('f69'), j.get('f72'),
                                j.get('f75'), j.get('f78'), j.get('f81'), j.get('f84'), j.get('f87'), j.get('f19'),
                                str(datetime.datetime.utcfromtimestamp(timex / 1000).strftime("%Y-%m-%d"))
                                )

        result = re.sub(r"(?<=\")-(?=\")", '0.0', e_sql)
        print(e_sql)
    # cursor.execute(result)
    # conn.commit()

    # conn.commit()
    # cursor.close()
    # conn.close()


if __name__ == '__main__':
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Astatus FROM spider_base.df_calendar where date='" + str(datetime.datetime.now().date()) + "'")
    result = cursor.fetchone()
    if result[0] == str(1):
        catch_stock((int(time.mktime(time.localtime(time.time())))) * 1000)
    print("catch done....")
