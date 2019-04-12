#!/user/bin/python
# -*- coding:utf-8 -*-
import smtplib   #连接邮件服务器
import email.mime.multipart     #处理邮件组成
import email.mime.text          #处理邮件正文
server = 'smtp.163.com'        #邮件服务器
from_user='15237891832@163.com' #发件人
res='dongyang000@foxmail.com'   #收件人
passwd='jidongyang960604'      #授权码  允许登陆客户端的密码
#创建一个空邮件
message = email.mime.multipart.MIMEMultipart()
message['From']=from_user  #邮件的发件人
message['To']=res          #邮件的接收者
message['Subject']='我等你放假而纷纷'   #邮件主题
text="""
hello,china,my name is dingkun,i'm from jopen!
i think world is beautiful
but ……
"""
#对正文进行编码
tet=email.mime.text.MIMEText(text,'plain','utf-8')
#将正文添加到邮件中
message.attach(tet)

#带附件的
#对附件进行读取和编码
att2=email.mime.text.MIMEText(open('b.txt','rb').read(),'base64','utf-8')
#给附件添加头部信息
att2["Content-Type"]='application/octet-stream'
att2["Content-Disposition"]='attachment;filename="b.txt"'
#将附件添加到邮件里
message.attach(att2)

#连接服务器
smtp123=smtplib.SMTP_SSL(server,465)
#登陆服务器
smtp123.login(from_user,passwd)
#发送邮件
smtp123.sendmail(from_user,res,message.as_string())
#断开连接
smtp123.close()

