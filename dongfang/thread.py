# _*_ coding : utf-8 _*_
# @Time : 2022/5/27 - 22:08
# @Author : Holden
# @File : thread
# @Project : python

from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor  # 导入线程池和进程池


def func(name):
    print(name)


# t = Thread(target=func())
# t.start()  # 只是将多线程状态变成可执行状态,具体开始时间由cpu决定

if __name__ == '__main__':
    # 创建50个线程池
    with ThreadPoolExecutor(2) as t:
        for i in range(100):  # 100个任务
            t.submit(func, name=f"线程{i}")  # 相当于这100个任务由50个线程来瓜分
    # 会等待线程池中任务全部完成再继续执行，也就是with后的数据
    print("xx")
