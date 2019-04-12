#!/user/bin/python
# -*- coding:utf-8 -*-
# import requests
# import re
# class 糗事_Spider(object):
#     def 发送请求(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         ##伪装成浏览器
#         head={
#               'User-Agent':'Mozilla/5.0(Windows NT 10.0)Gecko/20100101 Firefox/65.0'
#             }
#         #发送请求
#         响应=requests.get(url=url,headers=head)
#         #读取响应 1.text 以字符串的方式读取  2.content 以字节的方式读取
#         html=响应.content.decode('utf-8')
#         #返回结果并赋值
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         #将正则表达式编译
#         patt = re.compile(r'<div class="cont发ent">(.*?)</span>',re.S)
#         #将编译后的条件到字符串中去查找
#         items = patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','').replace('<br/>','').strip()
#             # print(i)
#             shuju.append(i)
#         # print(shuju)
#         return shuju
#     def save(self,qwe):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i+'\n')
# qiu=糗事_Spider()
# for i in range(1,6):
#     html=qiu.发送请求(page=i)
#     shuju=qiu.guolv(abc=html)
#     qiu.save(shuju)


#爬取图片
# import requests
# import re
# class tupian(object):
#     a=0
#     def qingqiu(self,p):
#         ur = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(p)
#         head={
#                 'User-Agent':'Mozilla/5.0(Windows NT 10.0)Gecko/20100101 Firefox/65.0'
#                 }
#         res = requests.get(url=ur,headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         #过滤的是图片的网址
#         ab=re.compile('<div class="thumb">(.*?)</div>',re.S)
#         item=ab.findall(abc)
#         for j in item:
#             patt=re.compile('src="(.*?)"',re.S)
#             hhh=patt.findall(j)
#         # for i in items:
#         #     i='https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#             shuju.append(hhh[0])
#         return shuju
#     def save(self,qwe):
# #         #任何图片都是二进制
# #         #请求图片的网址，得到图片的源码
#         for i in range(len(qwe)):
#             res = requests.get('https:'+qwe[i])
#             ht = res.content      #得到的是二进制
#             print(ht)
#             with open('{}.jpg'.format(self.a),'wb') as f:
#                 f.write(ht)
#             self.a+=1
#         for i,j in enumerate(qwe):
#             res = requests.get(j)
#             ht = res.content      #得到的是二进制
#             with open('{}.jpg'.format(i),'wb') as f:
#                 f.write(ht)
# a=tupian()
# for i in range(1,3):
#     b=a.qingqiu(p=i)
#     c=a.guolv(b)
#     a.save(c)





# https://pic.qiushibaike.com/system/pictures/12153/121533870/medium/I10PNOB4OX9LFILS.jpg



# import pymysql
# 连接数据库
# conn = pymysql.connect(host='192.168.0.159',
#                        port=3306,
#                        user='root',
#                        password='123',
#                        charset='utf8')
# 创建游标（控制器）
# abc =conn.cursor()
# 执行sql语句：
# abc.execute('show databases;')
# abc.execute('create database python_test;')
# abc.execute('show databases;')
# abc.execute('use python_test;')
# 断开数据库
# conn.close()
# abc.execute('create table biao1(name char(20),age int,sex char(10));')
# abc.execute('insert into biao1 values("xiaoming",20,"nv"),("xiaoming",13,"nan");')
# 提交 对数据库数据进行更改的时候
# 是由连接数据库的变量名来提交
# conn.commit()
# abc.execute('show tables;')
# abc.execute('select * from biao1;')
# abc.execute('show databases;')
#
# 任何结果都需要有容器来接收
# print(abc.fetchall())  #只接收上一个sql语句的结果，接收全部内容
# print(abc.fetchmany(3))  #也只接收上一个sql语句的结果，但默认只接收第一行，在括号里写入数字几就就接收多少行
# print(abc.fetchone())    #也只接收上一个sql语句的结果,每次只接收一行，但具有迭代功能(写几个显几行）
# print(abc.fetchone())
#
# import json
# a={'infe':113}
# dw=json.dumps(a)
# print(type(dw))
# from time import sleep
# import threading
# def asd():
#     for i in range(3):
#         print('打篮球')
#         sleep(2)
# def sdf():
#     for j in range(3):
#         print('制作饮料')
#         sleep(3)
# threading.Thread(target=asd).start()  #开启线程
# threading.Thread(target=sdf).start()
#
# import time
# # # bb=time.time()
# # # abc=time.localtime(bb-1578748)
# # # print(time.strftime('%Y-%m-%d %H:%M:%S %w',abc))
# # print(time.strptime('1970-10-23','%Y-%m-%d'))
#
# 采用ssh协议。连接linux，并管理
# import paramiko
# #创建一个远程客户端
# ssh123=paramiko.SSHClient()
# #第一次连接主机，knows_hosts 存放的主机地址，跳过查找
# 允许连接不在know_hosts文件中的主机
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #连接主机
# ssh123.connect(hostname='192.168.0.101',
#                port=22,
#                username='root',
#                password='123456')
# #exec_command 执行命令  直接具有结果的命令
# a,b,c=ssh123.exec_command('route -n')
# #第一个变量：表示输入的命令
# #第二个命令：表示命令执行的结果
# #第三个结果：表示命令的报错
# print(b.read().decode())
# #断开连接
# ssh123.close()
#
#
#
# #传输文件：
# import paramiko
# #建立一个传输通道
# ssh123=paramiko.Transport('192.168.0.101',22)
# #连接linux
# ssh123.connect(username='root',password='123456')
# #创建一个传输文件的对象
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# #从linux到windows传文件
# #第一个参数：表示要传输的文件
# #第二个文件：表示存放的本机位置
# sftp.get('install.log',r'.\abc.log')
#
# #从windows上到linux上
# sftp.put('a.txt',r'/home/b.txt')



#socket  自带的
#socket ：套接字  是实现最底层的一种通信方式  接收  发送
#采用c/s架构
#实现通过tcp协议进行通信  socket
#server端 （服务器端）
# import socket
# #创建一个套接字，规定使用tcp协议，ip版本
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip地址和端口号  接收的是个元组
# s.bind(('127.0.0.1',8888))
# #监听服务是否开启，数字指的是最大等待数
# s.listen(3)
# while True:
#     #接收请求 (会有两个值，第一个：表示连接信息  第二个：客户端的ip和端口号）
#     conn,addr=s.accept()
#     reg = conn.recv(1024)
#     print(type(conn))
#     #接收数据  1024表示一次性最大能接收1024字节的数据（最大1024）
#     print(reg.decode('utf-8'))
#     #发送数据
#     msg=input('请输入回应:')
#     conn.send(msg.encode('utf-8'))



#udp  server端
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定主机
s.bind(('127.0.0.1',8888))
while True:
    #第一个：客户端发送的请求数据，第二个：客户端的ip和端口号
    conn,addr=s.recvfrom(1024)
    #打印接收到的数据
    print(conn.decode('utf-8'))
    #发送响应
    s.sendto('响应的数据'.encode('utf-8'),addr)

