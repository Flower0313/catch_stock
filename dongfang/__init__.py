# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 10:52
# @Author : Holden
# @File : __init__.py
# @Project : python

# _*_ coding : utf-8 _*_
# @Time : 2022/5/25 - 22:40
# @Author : Holden
# @File : test
# @Project : python
import os
import schedule
import time
import threading

success = ''' 
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === |
            --by {}                 
'''

fail = '''
         /"\          
        |\ /|         
        |   |         
        | ~ |         
        |   |         
     /'\|   |/'\      
 /"\|   |   |   | \   
|   [ @ ]   |   |  \  
|   |   |   |   |   \ 
| ~ ~  ~  ~ |    )   \
|                   / 
 \                 /  
  \               /   
   \    _____    /    
    |- //''`\ - |     
    | (( =+= )) |     
    |- \\_|_//- |     
	            -- by {}
'''


def insert_finance_info():
    os.system("/root/bin/project/get_finance")


def insert_news_info():
    os.system("/root/bin/project/get_news")


def every_insert():
    os.system("/root/bin/project/executeall")


def run_thread(job_func):
    job = threading.Thread(target=job_func)
    job.start()


if __name__ == '__main__':
    schedule.every().monday.at("09:15").do(run_thread, insert_news_info)
    schedule.every().tuesday.at("09:15").do(run_thread, insert_news_info)
    schedule.every().wednesday.at("09:15").do(run_thread, insert_news_info)
    schedule.every().thursday.at("09:15").do(run_thread, insert_news_info)
    schedule.every().friday.at("09:15").do(run_thread, insert_news_info)

    schedule.every().monday.at("08:51").do(run_thread, insert_finance_info)
    schedule.every().tuesday.at("08:51").do(run_thread, insert_finance_info)
    schedule.every().wednesday.at("08:51").do(run_thread, insert_finance_info)
    schedule.every().thursday.at("08:51").do(run_thread, insert_finance_info)
    schedule.every().friday.at("08:51").do(run_thread, insert_finance_info)

    schedule.every().monday.at("15:01").do(run_thread, every_insert)
    schedule.every().tuesday.at("15:01").do(run_thread, every_insert)
    schedule.every().wednesday.at("15:01").do(run_thread, every_insert)
    schedule.every().thursday.at("15:01").do(run_thread, every_insert)
    schedule.every().friday.at("15:01").do(run_thread, every_insert)
    while True:
        schedule.run_pending()
        time.sleep(60)

