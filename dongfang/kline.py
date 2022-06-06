# _*_ coding : utf-8 _*_
# @Time : 2022/5/27 - 20:54
# @Author : Holden
# @File : kline
# @Project : python

import requests
import jsonpath
import json
from dongfang.Stock import Stock
import pymysql
import re
import datetime

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
    'st_si': '94378284527844',
    'HAList': 'a-sz-003032-%u4F20%u667A%u6559%u80B2%2Ca-sz-300010-%u8C46%u795E%u6559%u80B2%2Ca-sz-002523-%u5929%u6865%u8D77%u91CD%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-002821-%u51EF%u83B1%u82F1%2Ca-sz-002777-%u4E45%u8FDC%u94F6%u6D77%2Ca-sz-301215-%u4E2D%u6C7D%u80A1%u4EFD%2Ca-sz-300688-%u521B%u4E1A%u9ED1%u9A6C%2Cty-116-01153-%u4F73%u6E90%u670D%u52A1%2Ca-sz-300364-%u4E2D%u6587%u5728%u7EBF%2Ca-sz-300220-%u91D1%u8FD0%u6FC0%u5149',
    'st_asi': 'delete',
    'st_pvi': '99298644841036',
    'st_sp': '2022-05-13%2009%3A41%3A33',
    'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
    'st_sn': '130',
    'st_psi': '20220527205516479-113200301201-6358179493',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'qgqp_b_id=110276fdc7a31f5dee37aad9fb4e446a; ct=EEIhWo9zu9jtBAmjdkl2YBRq82hgRuqso3qChECmv0WJfiFuRl8IOgcthlInlYMJdK2pkiqhGmhbVqhoDy02sHmRPgKov-Lk48OiVgIeJUzp6emLUbvnf3sHgkTWzT-rYFqHMON2RgEiToOW-O_57LMljhaOPEi0JsXGTcH44ks; ut=FobyicMgeV6SKrOicruKo72Vo--axxKGABvmM2iTa7d3SGZEFeomi-JiqMabzBGSKGMZO-TLub02PbweePxPh04gi6Do7TremUC4fA38SLZd20Fkf-QpmUa_u5Y4Bl8J_14Il46DHC2klVCCOs86R7lHzLiP1_RUTrpafGwDKEv01WS_BfOWii0_37rE02Vlnco26NzSNOZJOmw4sbU8fmvEHu8Th0Xto71KwXxlKa4rXNnxXoGYW3V4hWGzd58AoH4BNuO8jfcyE8JZKvlEMIQ2MlJ16gkGketQ4R-6Ygk; uidal=4819115464066356Holdenxiao; sid=131578758; vtpst=%7c; em_hq_fls=js; qquestionnairebox=1; em-quote-version=topspeed; st_si=94378284527844; HAList=a-sz-003032-%u4F20%u667A%u6559%u80B2%2Ca-sz-300010-%u8C46%u795E%u6559%u80B2%2Ca-sz-002523-%u5929%u6865%u8D77%u91CD%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-002821-%u51EF%u83B1%u82F1%2Ca-sz-002777-%u4E45%u8FDC%u94F6%u6D77%2Ca-sz-301215-%u4E2D%u6C7D%u80A1%u4EFD%2Ca-sz-300688-%u521B%u4E1A%u9ED1%u9A6C%2Cty-116-01153-%u4F73%u6E90%u670D%u52A1%2Ca-sz-300364-%u4E2D%u6587%u5728%u7EBF%2Ca-sz-300220-%u91D1%u8FD0%u6FC0%u5149; st_asi=delete; st_pvi=99298644841036; st_sp=2022-05-13%2009%3A41%3A33; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=130; st_psi=20220527205516479-113200301201-6358179493',
    'Pragma': 'no-cache',
    'Referer': 'http://quote.eastmoney.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}

params = {
    'secid': '0.003032',
    'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
    'fields1': 'f1,f2,f3,f4,f5,f6',
    'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
    'klt': '101',
    'fqt': '0',
    'end': '20500101',
    'lmt': '10',
    '_': '1653656115193',
}

response = requests.get('http://66.push2his.eastmoney.com/api/qt/stock/kline/get', params=params, cookies=cookies,
                        headers=headers, verify=False)

content = response.text
kline_json = jsonpath.jsonpath(json.loads(content), '$.data.klines[*]')

for k in kline_json:
    print(k)
