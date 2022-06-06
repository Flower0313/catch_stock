# _*_ coding : utf-8 _*_
# @Time : 2022/5/16 - 17:42
# @Author : Holden
# @File : postDemo2
# @Project : python
import urllib.request
import urllib.parse

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'X-Requested-With': ' XMLHttpRequest',
    'Cookie': ' BIDUPSID=8757BE6D730D29809F8CA026248EDE27; PSTM=1640167970; __yjs_duid=1_8ceb78da1c3ac6eeaf7ab54221a932071640265454870; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; BAIDUID=FEBAC5C5B48EFED28B0C78519E83EEFA:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=B5U0FlR1VwNUplRERuSTdCZ1pzQVh2cVVxNE5wdlZHV28zLWxHdUJXQkVlWmRpRVFBQUFBJCQAAAAAAAAAAAEAAADZkAlZsK7QprXEztLKx7uotvkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETsb2JE7G9iRH; BDUSS_BFESS=B5U0FlR1VwNUplRERuSTdCZ1pzQVh2cVVxNE5wdlZHV28zLWxHdUJXQkVlWmRpRVFBQUFBJCQAAAAAAAAAAAEAAADZkAlZsK7QprXEztLKx7uotvkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETsb2JE7G9iRH; BAIDUID_BFESS=FEBAC5C5B48EFED28B0C78519E83EEFA:FG=1; RT="z=1&dm=baidu.com&si=asah389o3ww&ss=l3728cy1&sl=2&tt=1un&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=47j&ul=9ns&hd=9o9"; H_WISE_SIDS=110085_114550_127969_179347_184716_189755_190620_194085_194519_194529_196082_196427_197241_197711_197957_199023_199572_201193_203309_203519_203525_203880_203882_203885_204710_204713_204715_204717_204720_204817_204864_204915_205217_205420_205424_205751_205838_206929_207003_207236_207264_207830_207996_208721_209063_209345_209395_209512_209568_210088_210092_210300_210359_210669_210733_210736_210756_210788_210790_210890_210892_210895_210906_210914_211013_211023_211029_211173_211180_211301_211441_211456_211580_211732_211761_211925_212227_212293_212295_212416_212618_212775_212967_212970_212977_213003_213040_213060_213094_213140_213220_213327_213350; SE_LAUNCH=5%3A27543658; BA_HECTOR=ala10k0lal24a40guf1h820450r; BAIDU_WISE_UID=wapp_1652635073588_643; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=36426_36367_34812_35912_36167_34584_35978_36055_36235_26350_36349_36311; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1650550281,1652631403,1652693501; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1652694120; ab_sr=1.0.1_NTU0ODNkYWRhNzI1YjNhNDc2MTAwNzM2MzViZmU4MTQ3NDIzOWZlNTc3ZDdjYzRmOTY1Mzc3YTRhODY4ZTAwMzg3NDNjOTQ5YWE4MTE0NWFhMGVlNGZmZmJkZTNmZjBmNmNjYTI2MGY5ZTlkNmM5ZjQzNmVjNTczYzUwYzc4ODU2YTBlZGEzMjNiMTI3NDJiOGMxYzg5ZjE0NjNiNDdmZGMzNmE0YmM3ODFkZWFmNTE3OWU4YjdmNWIyMzEwM2M1'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'c5f10f0bfcde439d392283be90991295',
    'domain': 'common'
}

datas = urllib.parse.urlencode(data).encode('utf-8')

# 请求定制
request = urllib.request.Request(url=url, data=datas, headers=headers)

# 模拟发送请求
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
