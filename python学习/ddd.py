# def sum(x,y):
#     s=x+y
#     print(s)
# if __name__ == '__mian__':
#     print('哈哈')
# def jian(x,y):
#     s=x-y
#     print(s)

# with open('b.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
#     b=[]
#     print(a)
    # for i in a:
    #     if
    #         b.append(i)
    # print(b)
#
# a=[i for i in range(10)]+[chr(j) for j in range(97,103)]
# print(a)




# 删除东西
# import os
# try:
#     a=0
#     while True:
#         os.remove('{}.jpg'.format(a))
#         a+=1
# except:
#     pass
# a=os.listdir(r'E:\python学习')
# print(a)


# import requests
# import re
# class tupian(object):
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
#         #任何图片都是二进制
#         #请求图片的网址，得到图片的源码
#         for i in range(len(qwe)):
#             res = requests.get('https:'+qwe[i])
#             ht = res.content      #得到的是二进制
#             with open('{}.jpg'.format(i),'wb') as f:
#                 f.write(ht)
# a=tupian()
# cd=[]
# for i in range(1,3):
#     cd.extend(a.guolv(a.qingqiu(p=i)))
# a.save(cd)

# for i in range(0,100,25):
#     print(i)

# import requests
# import re
# import json
# class gaode(object):
#     def qingqiu(self):
#         url='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=11&city=310000&geoobj=121.295119|31.07524|121.871923|31.396985&keywords=火车站'
#         head = {
#                 'User-Agent':'Mozilla/5.0(Windows NT 10.0)Gecko/20100101 Firefox/65.0'
#                 }
#         res = requests.get(url=url, headers=head)
#         html = res.content.decode('utf-8')
#         ht=json.loads(html)
#         return ht
#     def guolv(self,ht):
#         a=ht.items()
#         print(a)
#         shuju={}
#         for i in a:
#             if i == 'date':
#                 print(i)
#
#     def save(self):
#         with open('a.txt','w',encoding='utf-8')as f:
#
# a=gaode()
# b=a.qingqiu()
# a.guolv(b)


# https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20
# &pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000
# &div=PC1000&addr_poi_merge=true&is_classify=true&zoom=11&city=310000
# &geoobj=121.295119|31.07524|121.871923|31.396985&keywords=火车站


# 从txt文件导入到表格文件
# import xlwt
# with open('b.txt','r',encoding='utf-8')as f:
#     a=f.readlines()
# f=xlwt.Workbook(encoding='utf-8')
# shett=f.add_sheet('exclelalla')
# for i,j in enumerate(a):
#     j=j.replace('\n','').split(',')
#     for k in range(len(j)):
#         shett.write(i,k,j[k])
# f.save('daoyan.xls')



# 从表格文件导入到txt文件
# import xlrd
# f=xlrd.open_workbook('导入电影.xls')
# a=f.sheets()[0]
# with open('e.txt','w',encoding='utf-8')as b:
#     for i in range(a.nrows):
#         c=a.row_values(i)
#         for j in c:
#             if j == c[-1]:
#                 b.write(j+'\n')
#             else:
#                 b.write(j+',')

# #从表格文件到数据库文件
# import pymysql
# import xlrd
# conn=pymysql.connect(host='192.168.0.101',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# abc=conn.cursor()
# abc.execute('create database biaoo0;')
# abc.execute('use biaoo0;')
# f=xlrd.open_workbook('导入数据.xls')
# sheet=f.sheets()[0]
# for i in range(sheet.nrows):
#     a=sheet.row_values(i)
#     print(a[0],a[1],a[2],a[3])
#     if i==0:
#         abc.execute('create table biao6({} char(255),{} char(255),{} char(255),{} char(255));'.format(a[0],a[1],a[2],a[3]))
#     else:
#         abc.execute('insert into biao6 values("{}","{}","{}","{}");'.format(a[0],a[1],a[2],a[3]))
#         conn.commit()
# abc.execute('select * from biao6;')
# print(abc.fetchall())
# conn.close()





# 从数据库到表格文件
# import pymysql
# import xlwt
# conn=pymysql.connect(host='192.168.0.101',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# abc=conn.cursor()
# abc.execute('use daoru;')
# abc.execute('select * from douban;')
# a=abc.fetchall()
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('shujuku')
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sheet.write(i,j,a[i][j])
# f.save('shujuku.xls')

# 从数据库到txt文件
# import pymysql
# conn=pymysql.connect(host='192.168.0.101',
#                      user='root',
#                      port=3306,
#                      password='123456',
#                      charset='utf8')
# abc=conn.cursor()
# abc.execute('use daoru;')
# abc.execute('select * from douban;')
# a=abc.fetchall()
# with open('e.txt','w',encoding='utf-8')as f:
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if a[i][j] ==a[i][-1]:
#                 f.write(a[i][j]+'\n')
#             else:
#                 f.write(a[i][j]+',')
