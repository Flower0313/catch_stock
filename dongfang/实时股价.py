import json
import time

import pymysql
import requests
from kafka import KafkaProducer


def getAllCode():
    a_url = 'http://4.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=2000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=4819115464066356|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f2,f19,f12,f3&_=' + str(
        int(time.mktime(time.localtime(time.time()))) * 1000)
    response = requests.get(url=a_url)
    content = response.text
    target_json = json.loads(content)
    return target_json['data']['diff']


def sendKafka(str):
    producer = KafkaProducer(bootstrap_servers=['43.142.117.50:9092', '43.142.75.17:9092','121.4.71.97:9092'])
    producer.send(
        topic='stocks',
        value=json.dumps(str).encode('utf-8'))  # python3 fix to bytes('{}'.format(result_str), 'utf-8'))
    producer.flush()
    producer.close()


if __name__ == '__main__':
    while True:
        timer = time.strftime('%H:%M:%S', time.localtime(time.time()))  # '11:00:00'
        if timer == '09:15:00':
            conn_result = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='w654646',
                charset='utf8'
            )
            cursor = conn_result.cursor()
            cursor.execute("truncate table spider_base.stock_real_time")
            conn_result.commit()
            cursor.close()
            conn_result.close()

        if '09:30:00' <= timer <= '11:30:00' or '13:00:00' <= timer <= '15:00:00':
            sendKafka(getAllCode())
        time.sleep(1)
