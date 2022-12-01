# _*_ coding : utf-8 _*_
# @Time : 2022/7/14 - 14:41
# @Author : Holden
# @File : test
# @Project : python
import numpy as np
from clickhouse_driver import Client
from datetime import datetime

from knn.海伦约会 import file2matrix

client = Client(host='43.142.117.50', database='spider_base', user='default', password='root',
                port=61616)


# res = client.execute("select code,name,closing_price from spider_base.stock_detail where code='301266'")

def datingClassTest():
    fr = open("stock.csv")
    # 读取文件所有内容
    arrayOLines = fr.readlines()
    # 得到文件行数
    numberOfLines = len(arrayOLines)
    # 返回的分类标签向量
    simaple = []
    result = []
    # 行的索引值
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split(',')
        simaple.append(listFromLine[3:38])
        if float(listFromLine[-1]) > 0:
            result.append("up")
        else:
            result.append("down")
    return simaple, result


def autoNorm(datingDataMat):
   for i in range(len(datingDataMat))



if __name__ == '__main__':
    # 获取数据源
    datingDataMat, datingLabels = datingClassTest()
    # 矩阵数据归一化
    autoNorm(datingDataMat)
