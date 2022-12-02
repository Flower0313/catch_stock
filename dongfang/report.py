import datetime
import json
import re
import pymysql as pymysql
import requests
from concurrent.futures import ThreadPoolExecutor

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
    'emshistory': '%5B%22603259%22%2C%22%E8%8A%82%E8%83%BD%E9%A3%8E%E7%94%B5%22%2C%22000638%22%2C%22%E4%B8%9C%E6%96%B9%E9%9B%A8%E8%99%B9%22%2C%22301266%22%2C%22%E7%91%9E%E6%B3%B0%E6%96%B0%E6%9D%90%22%2C%22688349%22%2C%22C%E9%BE%99%E8%8A%AF%22%2C%22%E4%BA%94%E6%B4%B2%E5%8C%BB%E7%96%97%22%2C%22%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A%22%5D',
    'st_si': '03174680155856',
    'Hm_lvt_f5b8577eb864c9edb45975f456f5dc27': '1669775540,1669859724,1669860368,1669948143',
    'HAList': 'ty-1-603288-%u6D77%u5929%u5473%u4E1A%2Cty-0-002507-%u6DAA%u9675%u69A8%u83DC%2Cty-1-603365-%u6C34%u661F%u5BB6%u7EBA%2Cty-0-002594-%u6BD4%u4E9A%u8FEA%2Cty-0-300768-%u8FEA%u666E%u79D1%u6280%2Cty-0-000055-%u65B9%u5927%u96C6%u56E2%2Cty-0-002852-%u9053%u9053%u5168%2Cty-0-300718-%u957F%u76DB%u8F74%u627F%2Cty-1-688317-%u4E4B%u6C5F%u751F%u7269%2Cty-0-002424-%u8D35%u5DDE%u767E%u7075',
    'st_asi': 'delete',
    'Hm_lpvt_f5b8577eb864c9edb45975f456f5dc27': '1669967226',
    'st_pvi': '99298644841036',
    'st_sp': '2022-05-13%2009%3A41%3A33',
    'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
    'st_sn': '40',
    'st_psi': '20221202154706116-113301310291-5150232434',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/Index?type=web&code=sz002507',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

conn = pymysql.connect(
    host='8.130.49.69',
    port=3306,
    user='root',
    passwd='w654646',
    charset='utf8'
)


# 03-31|06-30|09-30|12-31

def getStocks():
    cursor = conn.cursor()
    cursor.execute(
        "select distinct if(substr(`code`,1,1)='6','sh','sz') per,`code` from spider_base.df_a_stock_detail where board in (2,6) and ds='2022-12-02' and current_price>0")
    content = cursor.fetchall()
    cursor.close()
    conn.close()
    return content


def company_asset(params):
    url = "http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/zcfzbAjaxNew"
    response = requests.get(url, params=params, cookies=cookies, headers=headers, verify=False)
    result = json.loads(response.text)
    if len(result) > 2:
        asset = result['data'][0]
        return str(asset['REPORT_DATE']).split(" ")[0], asset['MONETARYFUNDS'], asset['MONETARYFUNDS_YOY'], asset[
            'TOTAL_CURRENT_ASSETS'], asset[
                   'TOTAL_CURRENT_ASSETS_YOY'], asset['TOTAL_NONCURRENT_ASSETS'], asset['TOTAL_NONCURRENT_ASSETS_YOY'], \
               asset[
                   'TOTAL_CURRENT_LIAB'], asset['TOTAL_CURRENT_LIAB_YOY'], asset['TOTAL_NONCURRENT_LIAB'], asset[
                   'TOTAL_NONCURRENT_LIAB_YOY'], asset['TOTAL_EQUITY'], asset['TOTAL_EQUITY_YOY']
    else:
        return -1


def company_profit(params):
    url = "http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/lrbAjaxNew"
    response = requests.get(url, params=params, cookies=cookies, headers=headers, verify=False)
    # [0] represent the close report date
    result = json.loads(response.text)
    if len(result) > 2:
        profit = result['data'][0]
        return profit['TOTAL_OPERATE_INCOME'], profit['TOTAL_OPERATE_INCOME_YOY'], profit['TOTAL_OPERATE_COST'], profit[
            'TOTAL_OPERATE_COST_YOY'], profit['OPERATE_PROFIT'], profit['OPERATE_PROFIT_YOY'], profit['TOTAL_PROFIT'], \
               profit['TOTAL_PROFIT_YOY'], profit['NETPROFIT'], profit['NETPROFIT_YOY'], profit['TOTAL_COMPRE_INCOME'], \
               profit['TOTAL_COMPRE_INCOME_YOY']

    else:
        return -1


def cash_flow(params):
    url = "http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/xjllbAjaxNew"
    response = requests.get(url, params=params, cookies=cookies, headers=headers, verify=False)
    result = json.loads(response.text)
    if len(result) > 2:
        cash = result['data'][0]
        return cash['NETCASH_OPERATE'], cash['NETCASH_OPERATE_YOY'], cash['NETCASH_INVEST'], cash['NETCASH_INVEST_YOY'], \
               cash['NETCASH_FINANCE'], cash['NETCASH_FINANCE_YOY'], cash['END_CCE'], cash['END_CCE_YOY']
    else:
        return -1


def all_report(pre, code, date):
    conn_min = pymysql.connect(
        host='8.130.49.69',
        port=3306,
        user='root',
        passwd='w654646',
        charset='utf8'
    )

    params = {
        'companyType': '4',
        'reportDateType': '0',
        'reportType': '1',
        'dates': date,
        'code': str(pre) + str(code),
    }
    base_sql = '''
        insert into spider_base.df_a_stock_report(`code`,`report_date` ,`monetary_funds`,`monetary_funds_yoy`,`total_current_assets`,`total_current_assets_yoy`,`total_noncurrent_assets`,`total_noncurrent_assets_yoy`,`total_current_liab`,`total_current_liab_yoy`,`total_noncurrent_liab` ,`total_noncurrent_liab_yoy`,`total_equity`,`total_equity_yoy`,`total_operate_income`,`total_operate_income_yoy`,`total_operate_cost`,`total_operate_cost_yoy`,`operate_profit`,`operate_profit_yoy`,`total_profit`,`total_profit_yoy`,`netprofit`,`netprofit_yoy`,`total_compre_income`,`total_compre_income_yoy`,`netcash_operate`,`netcash_operate_yoy`,`netcash_invest`,`netcash_invest_yoy`,`netcash_finance`,`netcash_finance_yoy`,`end_cce`,`end_cce_yoy`) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
    '''

    asset = company_asset(params)
    profit = company_profit(params)
    cash = cash_flow(params)
    if asset != -1 and cash != -1 and profit != -1:
        result_sql = base_sql.format(code, asset[0], asset[1], asset[2], asset[3], asset[4], asset[5], asset[6],
                                     asset[7], asset[8],
                                     asset[9], asset[10], asset[11], asset[12], profit[0], profit[1], profit[2],
                                     profit[3],
                                     profit[4], profit[5], profit[6], profit[7], profit[8], profit[9], profit[10],
                                     profit[11],
                                     cash[0], cash[1], cash[2], cash[3], cash[4], cash[5], cash[6], cash[7])
        cursor = conn_min.cursor()
        cursor.execute(result_sql)
        conn_min.commit()
        cursor.close()
        conn_min.close()


if __name__ == '__main__':
    with ThreadPoolExecutor(20) as t:
        for i in getStocks():
            t.submit(all_report, i[0], i[1], '2022-09-30')
