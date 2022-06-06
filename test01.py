# _*_ coding : utf-8 _*_
# @Time : 2022/5/11 - 11:25
# @Author : Holden
# @File : test01
# @Project : python
import json

print("你好")

# 单行注释
'''
多行注释
print("你好")
'''

# list 列表
# tuple 元组
# dict 字典

money = 5000 # int
money2 = 1.2 # float
sex = True # bool
sex = False
# 字符串在python中使用的是单引号或是双引号
s = 'hello world'
s2 = "hello world"

name_list = ['结论','你好'] # 列表

age_tuple = (18,19,20)
print(age_tuple)
print(type(s2)) # 使用type查询变量类型

age = 18
name = 'xiaohua'
print('我的名字是%s,我的年龄是%d' % (name,age))


name_list.remove('结论')

# 元组的元素不能修改，列表可以修改
# 当一个元组中只有一个数据时，就是整型，所以定义只有一个元素的元组，需要在后面再加一个空
#  文件打开了尽量关闭，若文件存在，会先清空原来的数据然后再写
# read是一字节一字节的读取，而readline是一行一行的读
# 对象若想写入文件，必须要先序列化，第一种是dumps()，第二种是dump()
fp = open('test.txt','w')
names = json.dumps(name_list) # 将对象转换为json字符串
fp.write(names)
fp.close()

# dump()将对象转换为字符串的同时，指定一个文件的对象，然后把转换后的字符串写入到这个文件里
json.dump(name_list,fp)

# 反序列化loads()和load()
fp = open('test.txt','r')
content = fp.read()
json.loads(content) # 反序列化















