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

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    charset='utf8'
)


def get_a_stock_num():
    a_url = 'http://55.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=1&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=4819115464066356|0|0|0|web&fid=f3&fs=m:116+t:3,m:116+t:4,m:116+t:1,m:116+t:2&fields=f1&_=' + str(
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


def catch_stock(timex):
    url = 'http://55.push2.eastmoney.com/api/qt/clist/get'
    a_stock_nums = get_a_stock_num()
    print(a_stock_nums)

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
        'st_si': '51002801573679',
        'HAList': 'a-sz-000002-%u4E07%20%20%u79D1%uFF21%2Cty-116-01211-%u6BD4%u4E9A%u8FEA%u80A1%u4EFD%2Ca-sz-002821-%u51EF%u83B1%u82F1%2Ca-sz-002594-%u6BD4%u4E9A%u8FEA%2Cty-1-688607-%u5EB7%u4F17%u533B%u7597%2Ca-sh-600651-%u98DE%u4E50%u97F3%u54CD%2Cty-1-688071-%u534E%u4F9D%u79D1%u6280%2Ca-sz-300990-%u540C%u98DE%u80A1%u4EFD%2Ca-sz-000957-%u4E2D%u901A%u5BA2%u8F66%2Cty-1-688400-%u51CC%u4E91%u5149',
        'st_asi': 'delete',
        'st_pvi': '99298644841036',
        'st_sp': '2022-05-13%2009%3A41%3A33',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '20',
        'st_psi': '20220720181732602-113200301321-1662038893',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'qgqp_b_id=110276fdc7a31f5dee37aad9fb4e446a; ct=EEIhWo9zu9jtBAmjdkl2YBRq82hgRuqso3qChECmv0WJfiFuRl8IOgcthlInlYMJdK2pkiqhGmhbVqhoDy02sHmRPgKov-Lk48OiVgIeJUzp6emLUbvnf3sHgkTWzT-rYFqHMON2RgEiToOW-O_57LMljhaOPEi0JsXGTcH44ks; ut=FobyicMgeV6SKrOicruKo72Vo--axxKGABvmM2iTa7d3SGZEFeomi-JiqMabzBGSKGMZO-TLub02PbweePxPh04gi6Do7TremUC4fA38SLZd20Fkf-QpmUa_u5Y4Bl8J_14Il46DHC2klVCCOs86R7lHzLiP1_RUTrpafGwDKEv01WS_BfOWii0_37rE02Vlnco26NzSNOZJOmw4sbU8fmvEHu8Th0Xto71KwXxlKa4rXNnxXoGYW3V4hWGzd58AoH4BNuO8jfcyE8JZKvlEMIQ2MlJ16gkGketQ4R-6Ygk; uidal=4819115464066356Holdenxiao; sid=131578758; vtpst=%7c; em_hq_fls=js; em-quote-version=topspeed; emshistory=%5B%22C%E9%BE%99%E8%8A%AF%22%2C%22%E4%BA%94%E6%B4%B2%E5%8C%BB%E7%96%97%22%2C%22%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A%22%2C%22%E4%B8%AD%E5%9B%BD%E8%BF%9E%E9%80%9A%22%5D; xsb_history=400071%7C%u4E2D%u5F181; st_si=51002801573679; HAList=a-sz-000002-%u4E07%20%20%u79D1%uFF21%2Cty-116-01211-%u6BD4%u4E9A%u8FEA%u80A1%u4EFD%2Ca-sz-002821-%u51EF%u83B1%u82F1%2Ca-sz-002594-%u6BD4%u4E9A%u8FEA%2Cty-1-688607-%u5EB7%u4F17%u533B%u7597%2Ca-sh-600651-%u98DE%u4E50%u97F3%u54CD%2Cty-1-688071-%u534E%u4F9D%u79D1%u6280%2Ca-sz-300990-%u540C%u98DE%u80A1%u4EFD%2Ca-sz-000957-%u4E2D%u901A%u5BA2%u8F66%2Cty-1-688400-%u51CC%u4E91%u5149; st_asi=delete; st_pvi=99298644841036; st_sp=2022-05-13%2009%3A41%3A33; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=20; st_psi=20220720181732602-113200301321-1662038893',
        'Pragma': 'no-cache',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
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
        'fs': 'm:116+t:3,m:116+t:4,m:116+t:1,m:116+t:2',  # 控制港股还是A股
        'fields': 'f1,f5,f6,f12,f13,f14,f2,f3,f4,f8,f9,f7,f10,f15,f16,f17,f18,f20,f21,f23,f25,f26,f35,f34,f37,f38,f39,f40,f46,f49,f50,f57,f62,f100,f102,f112,f114,f115,f135,f292',
        '_': timex

    }

    base_sql = '''
                insert into spider_base.df_hk_stock_detail(market,code,name,current_price,up_down_rate,up_down_amount,turnover_rate,PE_ratio_d,amplitude,volume_ratio,
            highest,lowest,opening_price,t_1_price,total_market_v,circulation_market_v,price_to_b_ratio,increase_this_year,
            time_to_market,outer_disk,inner_disk,aoe,total_share_capital,tradable_shares,total_revenue,total_revenue_r,
            gross_profit_margin,total_assets,debt_ratio,flow_main_forces_today,industry,regional_plate,
            remark,profit,PE_ratio_s,ttm,net_assets,deal_amount,deal_vol,dealTradeStae,ds) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
            "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
            "{}","{}","{}","{}","{}","{}","{}","{}")
            '''

    response = requests.get(url=url, params=data, headers=headers, cookies=cookies, verify=False)
    real_json = json.loads(response.text)['data']['diff']

    cursor = conn.cursor()
    for j in real_json:
        e_sql = base_sql.format(j.get('f13'), j.get('f12'), j.get('f14'),
                                j.get('f2'),
                                j.get('f4'), j.get('f8'), j.get('f3'),
                                j.get('f9'), j.get('f7'), j.get('f10'), j.get('f15'), j.get('f16'), j.get('f17'),
                                j.get('f18'), j.get('f20'), j.get('f21'), j.get('f23'), j.get('f25'),
                                j.get('f26'),
                                j.get('f34'), j.get('f35'), j.get('f37'), j.get('f38'), j.get('f39'),
                                j.get('f40'),
                                j.get('f46'), j.get('f49'), j.get('f50'), j.get('f57'), j.get('f62'),
                                j.get('f100'), j.get('f102'), j.get('f103'),
                                j.get('f112'),
                                j.get('f114'), j.get('f115'), j.get('f135'), j.get('f5'), j.get('f6'),
                                j.get('f292'),
                                str(datetime.datetime.utcfromtimestamp(timex / 1000).strftime("%Y-%m-%d"))
                                )

        result = re.sub(r"(?<=\")-(?=\")", '0.0', e_sql)
        cursor.execute(result)
        conn.commit()

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    cursor = conn.cursor()
    cursor.execute(
        "SELECT HKstatus FROM spider_base.df_calendar where date='" + str(datetime.datetime.now().date()) + "'")
    result = cursor.fetchone()

    if result[0] == 1:
        catch_stock((int(time.mktime(time.localtime(time.time())))) * 1000)
    print("catch done....")
