import json
import re
import time
import requests
from kafka import KafkaProducer
from concurrent.futures import ThreadPoolExecutor


def requestForNew(url, max_try_num=10, sleep_time=5):
    headers = {
        'Referer': 'http://finance.sina.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    response = requests.get(url, headers=headers)
    for i in range(max_try_num):
        if response.status_code == 200:
            return response.text
        else:
            print("fail", response)
            time.sleep(sleep_time)


def getAllCode():
    a_url = 'http://4.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=6000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=4819115464066356|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f2,f13,f12&_=' + str(
        int(time.mktime(time.localtime(time.time()))) * 1000)
    response = requests.get(url=a_url)
    content = response.text
    target_json = json.loads(content)

    stocks = []
    for i in target_json['data']['diff']:
        if i['f2'] != 0 and str(i['f2']) != '-':
            prex = "sz"
            if i['f12'][0] == str(6):
                prex = "sh"
            elif i['f12'][0] == str(8):
                prex = "bj"
            stocks.append(prex + i['f12'])
    return stocks


def sendKafka(stocks):
    url = "https://hq.sinajs.cn/list=" + ",".join(stocks)

    content = requestForNew(url).split(";")[:-1]
    producer = KafkaProducer(bootstrap_servers=['43.142.117.50:9092', '43.142.75.17:9092'])

    for i in content:
        code = re.findall(r'(?<=\_).{8}(?=\=)', i)[0]
        detail = re.findall(r'(?<=\").*(?=\")', i)[0].split(",")
        name = detail[0]
        if len(detail) > 1:
            open_price = detail[1]
            before_closing = detail[2]
            current_price = detail[3]
            highest = detail[4]
            lowest = detail[5]

            result_str = {"code": code,
                          "name": name,
                          "opening_price": open_price,
                          "before_closing": before_closing,
                          "current_price": current_price,
                          "highest": highest,
                          "lowest": lowest,
                          "buy1": detail[11],
                          "buy1hand": detail[10],
                          "buy2": detail[13],
                          "buy2hand": detail[12],
                          "buy3": detail[15],
                          "buy3hand": detail[14],
                          "buy4": detail[17],
                          "buy4hand": detail[16],
                          "buy5": detail[19],
                          "buy5hand": detail[18],
                          "sale1": detail[21],
                          "sale1hand": detail[20],
                          "sale2": detail[23],
                          "sale2hand": detail[22],
                          "sale3": detail[25],
                          "sale3hand": detail[24],
                          "sale4": detail[27],
                          "sale4hand": detail[26],
                          "sale5": detail[29],
                          "sale5hand": detail[28],
                          "date": detail[30],
                          "time": detail[31]}
            producer.send(
                topic='first',
                value=json.dumps(result_str).encode('utf-8'))  # python3改为bytes('{}'.format(result_str), 'utf-8'))
            print(result_str)
            producer.flush()
    producer.close()


stocks = getAllCode()

with ThreadPoolExecutor(10) as t:
    nums = len(stocks)
    y = nums % 700
    stock_num = (y if nums <= 0 else 1) + (nums // 700)
    while True:
        timez = '11:00:00' #time.strftime('%H:%M:%S', time.localtime(time.time()))
        if timez == '09:00:00':
            stocks = getAllCode()
        if '09:00:00' < timez <= '11:30:00' or '13:00:00' < timez <= '15:00:00':
            for i in range(stock_num):
                t.submit(sendKafka, stocks[i * 700:(i + 1) * 700])
        time.sleep(2)
