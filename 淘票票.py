# _*_ coding : utf-8 _*_
# @Time : 2022/5/18 - 21:43
# @Author : Holden
# @File : 淘票票
# @Project : python

import urllib.request

url = "https://dianying.taobao.com/cityAction.json?city=430100&_ksTS=1652881375860_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true"

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'cookie': 'cna=gMdKGk4O0EcCAXJVcIFPVk9x; tracknick=%5Cu5E0C%5Cu671B%5Cu662F%5Cu6C38%5Cu4E0D%5Cu6C89%5Cu7720%5Cu7684%5Cu68A6flower; thw=cn; t=fa2e960d94ce2b97b72125c696787d65; lgc=%5Cu5E0C%5Cu671B%5Cu662F%5Cu6C38%5Cu4E0D%5Cu6C89%5Cu7720%5Cu7684%5Cu68A6flower; sgcookie=E100%2BnzshggjUc3n%2FAczbvzTvtaWKf0Hrqv4YaqX%2Fovw1r2pjF63rE0Z3gRdNEb4bkzfk6bN1nt0d1JsGoqctgDF1128br0%2B52I4fQNkj2wq0iE9tI9jwJUZ1LSuO5d5pphk; uc3=id2=UNDVdRS3wDrEfQ%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCvCl0xVaYBuwzjlY%3D&nk2=rKkU%2FKZe%2BPGvi8GtolEAmnyqB0H4gi2D; uc4=nk4=0%40roc8GIuUiOX4Uu1UY4g8f1z2SOizN1B7MOVwxef8vwskWKc%3D&id4=0%40UgclGKIsIRmizXShm77wl8my3Otx; _cc_=U%2BGCWk%2F7og%3D%3D; cookie2=14710ff0b89e3fc6bbe3b5c347eb8fce; v=0; _tb_token_=eb7fdee53d31; xlly_s=1; tb_city=430100; tb_cityName="s6TJsw=="; isg=BMfHLjQkadoSDu3ki9SMuX9VVnuRzJuuM7Q1oZmzCdZqCOPKoJ6p_n2JqshWv3Mm; tfstk=ck71BRYnhAD6tWEq71NUu2cfS2TRZDwptl9O1JtltZhosaC1iVgyFJYFmvY2MB1..; l=eBN9IWB7LM2fsqRpBO5aRurza77TfBdfG5FzaNbMiInca66N1evCqOChwr2DRdtjgtCUQeKPSMVCeRUBW9zdNxDDBeV-1NKmnxvO.'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
