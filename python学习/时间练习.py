#!/usr/bin/python
# -*- coding:utf-8 -*-
#输入一个日期，打印是否是闰年，星期几，一年中的第几天
# import time
# try:
#     a=input('请输入日期:')
#     a1=a[0:4]
#     if int(a1) % 4 ==0:
#         print('闰年')
#     elif int(a1) %100==0 and int(a1) % 400 ==0:
#         print('闰年')
#     else:
#         print('平年')
#     b=time.strptime(a,'%Y-%m-%d')
#     print('这一天是星期'+str(b[-3]))
#     print('这一天是一年中的第{}天'.format(b[-2]))
# except:
#     print('输入有误')


#输入日期的前一天
import time
a=input('请输入日期:')
aa=time.strptime(a,'%Y-%m-%d')
print(aa)
b=time.mktime(aa)-86400
bb=time.localtime(b)
print(time.strftime('%Y-%m-%d',bb))


