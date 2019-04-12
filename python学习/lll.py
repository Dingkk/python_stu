#!/user/bin/python
# -*- coding:utf-8 -*-
# import day1
# a=day1.哈哈()
# a.一起()
# def asd():
#     a=[]
#     for i in range(5):
#         b=input('请输入学生名:')
#         a.append(b)
#     import random
#     x=random.randint(0,4)
#     print(a[x])
# asd()

#
# def cc(s,a1,a2=0):
#     b=[]
#     m=''
#     for i in s:
#         b.append(i)
    # print(b)
    # if len(s)-(a1+a2)>0 and a1<len(s):
    #     for j in range(a2):
    #         b.pop(a1)
    #     for k in b:
    #         m += k
    #     print(m)
    # elif len(s)-(a1+a2)<0 and a1<len(s):
    #     for l in range(len(s)-a1):
    #         b.pop(a1)
    #     for k1 in b:
    #         m+=k1
    #     print(m)
    # elif a1>len(s):
    #     for k2 in b:
    #         m += k2
    #     print(m)
    # print(b)
    # else:
    #     print('>>>')
#     print(b[a1:a1+a2])
# cc('dwdwdwfef',3,10)



# a=['d', 'w', 'd', 'a', 's', 'd', 'w', 'd']
# b=''
# for i in a:
#     b+=i
# print(b)


# import requests
# import re
# class Aa(object):
#     def qq(self,page):
#         url='https://www.qiushibaike.com/textnew/page/{}/?s=5167698'.format(page)
#         head={
#             'User-Agent':'Mozilla/5.0(Windows NT 10.0)Gecko/20100101 Firefox/65.0'
#         }
#         xy=requests.get(url,headers=head)
#         jg=xy.text()
#         return jg
#     def gz(self,abc):
#         shuju=[]
#         patt=re.compile(r'<span>(.*?)</div>',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             i.replace()
#
# qsbk=Aa()
# html=qsbk.qq(page=1)
# shuju=qsbk.gz(abc=html)

# 可以将多个列表中的数据按照下标位置放在一起
# 例：c=zip(a，b)
# 需要重新定义数据类型
# print(list(c))



#爬取豆瓣
# import requests
# import re
# import xlrd
# from xlutils.copy import copy
# import xlwt
# class db(object):
#     def qq(self,page):
#         url='https://movie.douban.com/top250?start={}&filter='.format(page)
#         head={
#             'User-Agent': 'Mozilla/5.0(Windows NT 10.0)Gecko/20100101 Firefox/65.0'
#         }
#         xy = requests.get(url, headers=head)
#         html=xy.content.decode('utf-8')
#         return html
#     def gl(self,abc):
#         shuju1=[]
#         shuju2=[]
#         shuju3=[]
#         shuju4=[]
#         dianying=re.compile(r'<span class="title">(.*?)</span>',re.S)
#         daoyan=re.compile(r'<p class="">(.*?)&nbsp;&nbsp;&nbsp;',re.S)
#         pingjia=re.compile(r'<span>(.*?)</span>',re.S)
#         jianshu=re.compile(r'<span class="inq">(.*?)</span>',re.S)
#         items1=dianying.findall(abc)
#         items2 =daoyan.findall(abc)
#         items3 =pingjia.findall(abc)
#         items4 =jianshu.findall(abc)
#         for j in items1:
#             j=j.replace('</span>','').replace('<br/>','').strip()
#             if '&' in j:
#                 continue
#             shuju1.append(j)
#         for k in items2:
#             k=k.replace('\n','').strip()
#             shuju2.append(k)
#         for l in items3:
#             if '人评价' in l:
#                 l=l.replace('<span>','').replace('</span>','').replace('\n','').strip()
#                 shuju3.append(l)
#         for m in items4:
#             shuju4.append(m)
#         cc=list(zip(shuju1,shuju2,shuju3,shuju4))
#         return cc
#     def sa(self,nn,qq):
#         f=xlrd.open_workbook('导入电影.xls')
#         new_f=copy(f)
#         sheet=new_f.get_sheet(0)
#         for m in range(len(nn)):
#             for n in range(4):
#                 sheet.write(m+int(qq),n,'{}'.format(nn[m][n]))
#         new_f.save('导入电影.xls')
# a=db()
# for i in range(0,51,25):
#     b=a.qq(page=i)
#     c=a.gl(b)
#     a.sa(c,qq=i)



# import pymysql
# conn = pymysql.connect(host='192.168.0.159',
#                        port=3306,
#                        user='root',
#                        password='123',
#                        charset='utf8')
# abc =conn.cursor()
# while True:
#     a=input('请输入sql语句:')
#     print(a)
#     if a != 'exit':
#         abc.execute(a)
#         print(abc.fetchall())
#     else:
#         break
# conn.close()

# import xlrd
# f=xlrd.open_workbook('导入电影.xls')
# abc=f.sheets()[0]
# with open('b.txt','w',encoding='utf-8')as f:
#     for i in range(abc.nrows):
#         j=abc.row_values(i)
#         for k in j:
#             if k == j[-1]:
#                 f.write(k+'\n')
#             else:
#                 f.write(k+',')


#从excel 表格导入数据库
# import xlrd
# import pymysql
# conn = pymysql.connect(host='192.168.0.199',
#                        port=3306,
#                        user='root',
#                        password='123456',
#                        charset='utf8')
# efg =conn.cursor()
# efg.execute('create database dm;')
# efg.execute('use dm;')
# f=xlrd.open_workbook('导入电影.xls')
# abc=f.sheets()[0]
# for i in range(abc.nrows):
#     j=abc.row_values(i)
#     if i==0:
#         efg.execute('create table douban2(dianying char(255),daoyan char(255),pingjia char(255),jianshu char(255))')
#         # for k in j:
#     else:
#         efg.execute('insert into douban2 values("{}","{}","{}","{}");'.format(j[0],j[1],j[2],j[3]))saa22
# efg.execute('select * from douban2;')
# print(efg.fetchall())



#爬取壁纸
import requests
import re
import os
class bizhi(object):
    def qingqiu(self,page):
        ur='http://desk.zol.com.cn/bizhi/{}.html'.format(page)
        head={
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0)Gecko/20100101 Firefox/65.0'
            }
        res=requests.get(url=ur,headers=head)
        html=res.content.decode('gb2312')
        return html
    def qingqiu2(self,i):
        url = 'http://desk.zol.com.cn/bizhi/{}_2.html'.format(i)
        head = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0)Gecko/20100101 Firefox/65.0'
        }
        ress = requests.get(url=url, headers=head)
        html1 = ress.content.decode('gb2312')
        return html1
    def wz(self,abc):
        wangzhi=[]
        jk = re.compile('<a href="/bizhi/(.*?)_2.html">')
        item1 = jk.findall(abc)
        for o in item1:
            wangzhi.append(o)
            print(wangzhi)
        for i in range(2):
            wangzhi.pop(0)
            wangzhi.pop(-1)
        return wangzhi
    def guolv(self,abc):
        shuju=[]
        shuju1=[]
        wangzhi=[]
        ab=re.compile('<img src="(.*?)" width="144" height="90" >')
        cd=re.compile('<img srcs="(.*?)" width="144" height="90" >')
        gh=re.compile('<h3>(.*?)<span>',re.S)
        item=ab.findall(abc)
        items=cd.findall(abc)
        itemss=gh.findall(abc)
        for l in itemss:
            ef = re.compile('<a id=''".*href=.*html">(.*?)</a>')
            itemsss = ef.findall(l)
            itemsss=','.join(itemsss)
            shuju.append('{}'.format(itemsss))
        print(shuju)
        for i in item:
            shuju.append(i)
        for j in items:
            shuju1.append(j)
        shuju.extend(shuju1)
        return shuju
    def guolv2(self,mo):
        sj=[]
        a1=re.compile('<li class="photo-list-padding">(.*?)</li>')
        ii=a1.findall(mo)
        for v in ii:
            a2=re.compile('href="/bizhi/(.*?)_2.html"')
            ig=a2.findall(v)
            ig=','.join(ig)
            sj.append(ig)
        return(sj)
    def sa(self,m):
        os.chdir(r'E:\壁纸')
        os.mkdir('{}'.format(m[0]))
        os.chdir(r'E:\壁纸\{}'.format(m[0]))
        m.pop(0)
        for i,j in enumerate(m):
            j=j.replace('144x90','1024x768')
            r=requests.get(j)
            ht=r.content
            with open('{}.jpg'.format(i),'wb')as f:
                f.write(ht)
a=bizhi()
b=a.qingqiu(page=1)
e=a.guolv2(b)
for i in e:
    f=a.qingqiu2(1)
    g=a.guolv(f)
    # a.sa(g)

# for k in d:
#     m=a.qingqiu2(k)
#     n=a.guolv(d)
#     a.sa(n)


