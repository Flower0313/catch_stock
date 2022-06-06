# _*_ coding : utf-8 _*_
# @Time : 2022/5/27 - 10:09
# @Author : Holden
# @File : get_hk_stock_list
# @Project : python

import requests
import jsonpath
import json
from dongfang.Stock import Stock
import pymysql
import re
import datetime
import time


url = 'http://14.push2.eastmoney.com/api/qt/clist/get'
hk_stock_nums = Stock.get_hk_stock_num()


cookies = {
    'qgqp_b_id': '110276fdc7a31f5dee37aad9fb4e446a',
    'ct': 'EEIhWo9zu9jtBAmjdkl2YBRq82hgRuqso3qChECmv0WJfiFuRl8IOgcthlInlYMJdK2pkiqhGmhbVqhoDy02sHmRPgKov-Lk48OiVgIeJUzp6emLUbvnf3sHgkTWzT-rYFqHMON2RgEiToOW-O_57LMljhaOPEi0JsXGTcH44ks',
    'ut': 'FobyicMgeV6SKrOicruKo72Vo--axxKGABvmM2iTa7d3SGZEFeomi-JiqMabzBGSKGMZO-TLub02PbweePxPh04gi6Do7TremUC4fA38SLZd20Fkf-QpmUa_u5Y4Bl8J_14Il46DHC2klVCCOs86R7lHzLiP1_RUTrpafGwDKEv01WS_BfOWii0_37rE02Vlnco26NzSNOZJOmw4sbU8fmvEHu8Th0Xto71KwXxlKa4rXNnxXoGYW3V4hWGzd58AoH4BNuO8jfcyE8JZKvlEMIQ2MlJ16gkGketQ4R-6Ygk',
    'uidal': '4819115464066356Holdenxiao',
    'sid': '131578758',
    'vtpst': '%7c',
    'em_hq_fls': 'js',
    'qquestionnairebox': '1',
    'HAList': 'a-sz-300364-%u4E2D%u6587%u5728%u7EBF%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC%2Ca-sz-300220-%u91D1%u8FD0%u6FC0%u5149%2Ca-sz-301185-%u9E25%u739B%u8F6F%u4EF6%2Cty-1-000001-%u4E0A%u8BC1%u6307%u6570',
    'em-quote-version': 'topspeed',
    'st_si': '94378284527844',
    'st_asi': 'delete',
    'st_pvi': '99298644841036',
    'st_sp': '2022-05-13%2009%3A41%3A33',
    'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
    'st_sn': '3',
    'st_psi': '20220527100000734-113200301321-7400588657',
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

data = {
    'pn': 1,
    'pz': hk_stock_nums,
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
    '_': int(time.mktime(time.localtime(time.time()))) * 1000

}













