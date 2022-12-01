import datetime
import json
import re

import pymysql as pymysql
import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://search-api-web.eastmoney.com/search/jsonp"

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
    'emshistory': '%5B%22000638%22%2C%22%E4%B8%9C%E6%96%B9%E9%9B%A8%E8%99%B9%22%2C%22301266%22%2C%22%E7%91%9E%E6%B3%B0%E6%96%B0%E6%9D%90%22%2C%22688349%22%2C%22C%E9%BE%99%E8%8A%AF%22%2C%22%E4%BA%94%E6%B4%B2%E5%8C%BB%E7%96%97%22%2C%22%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A%22%2C%22%E4%B8%AD%E5%9B%BD%E8%BF%9E%E9%80%9A%22%5D',
    'st_si': '45042106836084',
    'Hm_lvt_f5b8577eb864c9edb45975f456f5dc27': '1667873192',
    'HAList': 'ty-0-430047-%u8BFA%u601D%u5170%u5FB7%2Cty-0-839725-%u60E0%u4E30%u94BB%u77F3%2Cty-1-688348-%u6631%u80FD%u79D1%u6280%2Cty-0-300763-%u9526%u6D6A%u79D1%u6280%2Cty-1-688390-%u56FA%u5FB7%u5A01%2Cty-1-603136-%u5929%u76EE%u6E56%2Cty-0-002993-%u5965%u6D77%u79D1%u6280%2Cty-0-002866-%u4F20%u827A%u79D1%u6280%2Cty-0-003004-%u58F0%u8FC5%u80A1%u4EFD%2Cty-1-688123-%u805A%u8FB0%u80A1%u4EFD',
    'st_asi': 'delete',
    'st_pvi': '99298644841036',
    'st_sp': '2022-05-13%2009%3A41%3A33',
    'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
    'st_sn': '46',
    'st_psi': '20221108111928803-113301310291-4593303011',
    'Hm_lpvt_f5b8577eb864c9edb45975f456f5dc27': '1667877575',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://emweb.securities.eastmoney.com/PC_HSF10/CompanyBigNews/Index?type=web&code=sh688348',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def getStocks():
    conn = pymysql.connect(
        host='8.130.49.69',
        port=3306,
        user='root',
        passwd='w654646',
        charset='utf8'
    )

    cursor = conn.cursor()
    cursor.execute("select `code` from spider_base.df_a_stock_detail where ds='2022-11-24'")
    content = cursor.fetchall()
    cursor.close()
    conn.close()
    return list(content)


def insertSQL(code, index, size):
    conn_result = pymysql.connect(
        host='8.130.49.69',
        port=3306,
        user='root',
        passwd='w654646',
        charset='utf8'
    )

    base_sql = '''
        insert into spider_base.df_a_stock_news(code,mediaName,title,content,notice_date) values("{}","{}","{}","{}","{}")
    '''

    params = {
        'cb': 'jQuery35103701525263440091_1669278461933',
        'param': '{"uid":"4819115464066356","keyword":"(' + str(
            code) + ')","type":["cmsArticleWebOld"],"client":"web","clientType":"web","clientVersion":"curr","param":{"cmsArticleWebOld":{"searchScope":"default","sort":"default","pageIndex":' + str(
            index) + ',"pageSize":' + str(size) + '}}}',
        '_': '1669270208096',
    }
    response = requests.get(url, params=params, cookies=cookies, headers=headers, verify=False)
    content = re.findall(r"(?<=\().*(?=\))", response.text)
    content = json.loads(content[0])['result']['cmsArticleWebOld']
    cursor = conn_result.cursor()
    for i in content:
        e_sql = base_sql.format(code, i['mediaName'], re.sub(r"\<(.{2,3})\>", '', i['title']),
                                '', i['date'])  # re.sub(r"\<(.{2,3})\>", '', i['content'])
        cursor.execute(e_sql)
        conn_result.commit()
    cursor.close()
    conn_result.close()


# 002408后面出问题
if __name__ == '__main__':
    with ThreadPoolExecutor(15) as t:
        for stock in getStocks():
            t.submit(insertSQL, stock[0], 1, 10)
