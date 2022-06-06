# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 11:45
# @Author : Holden
# @File : Stock
# @Project : python

import json
import requests
import time


class Stock:
    def __init__(self):
        pass

    @classmethod
    def get_a_stock_num(cls):
        a_url = 'http://4.push2.eastmoney.com/api/qt/clist/get?pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=4819115464066356|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1&_=' + str(
            int(time.mktime(time.localtime(time.time()))) * 1000)
        response = requests.get(url=a_url)
        content = response.text
        target_json = json.loads(content)

        return target_json.get('data').get('total')

    @classmethod
    def get_hk_stock_num(cls):
        hk_url = 'http://14.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=2&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=4819115464066356|0|0|0|web&fid=f3&fs=m:116+t:3,m:116+t:4,m:116+t:1,m:116+t:2&fields=f1&_=' + str(
            int(time.mktime(time.localtime(time.time()))) * 1000)
        response = requests.get(url=hk_url)
        content = response.text
        target_json = json.loads(content)

        return target_json.get('data').get('total')

    base_sql = '''
        insert into df_a_stock_detail(type,market,code,name,current_price,up_down_rate,up_down_amount,turnover_rate,PE_ratio_d,amplitude,volume_ratio,
    highest,lowest,opening_price,t_1_price,total_market_v,circulation_market_v,price_to_b_ratio,increase_this_year,
    time_to_market,outer_disk,inner_disk,aoe,total_share_capital,tradable_shares,total_revenue,total_revenue_r,
    gross_profit_margin,total_assets,debt_ratio,flow_main_forces_today,f97,f98,f99,industry,regional_plate,
    remark,profit,PE_ratio_s,ttm,net_assets,ds) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
    "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
    "{}","{}","{}","{}","{}")
    '''

    @classmethod
    def verify_code(cls, code):
        if "60" == code[:2]:
            return 1  # 沪市A股
        elif "90" == code[:2]:
            return 2  # 沪市B股
        elif "000" == code[:3]:
            return 3  # 深市A股
        elif "200" == code[:3]:
            return 4  # 深市B股
        elif "002" == code[:3]:
            return 5  # 中小板股
        elif "400" == code[:3] or "830" == code[:3]:
            return 6  # 三板市场
        elif "30" == code[:2]:
            return 7  # 创业板
        elif "688" == code[:3]:
            return 8  # 科创板
        else:
            return 9  # 未知

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

    base_sql_one_kline_month = '''
            insert into df_a_one_stock_month_kline(market,code,name,dk_total,up_down_rate,up_down_amount,turnover_rate,amplitude,highest,lowest,
        opening_price,closing_price,deal_amount,deal_vol,year,month_day) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
        '''

    base_sql_zero_kline_month = '''
                insert into df_a_zero_stock_month_kline(market,code,name,dk_total,up_down_rate,up_down_amount,turnover_rate,amplitude,highest,lowest,
            opening_price,closing_price,deal_amount,deal_vol,year,month_day) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
            '''

    base_sql_one_kline_week = '''
                insert into df_a_one_stock_week_kline(market,code,name,dk_total,up_down_rate,up_down_amount,turnover_rate,amplitude,highest,lowest,
            opening_price,closing_price,deal_amount,deal_vol,year,month_day) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
            '''

    base_sql_zero_kline_week = '''
                    insert into df_a_zero_stock_week_kline(market,code,name,dk_total,up_down_rate,up_down_amount,turnover_rate,amplitude,highest,lowest,
                opening_price,closing_price,deal_amount,deal_vol,year,month_day) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
                '''



    lmt = 10000
