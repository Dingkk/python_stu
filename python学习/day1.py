#!/user/bin/python
#-*- coding:utf-8 -*-
# print()
# print(1111)
# print('河南')
# print("呵呵")
# print("nan")
# print(222)
# bc=2
# abc=int(bc)
# print (type(abc))
# print (type(24.4))
# print (type(None))
# print (type(True))
# print (type(False))
# b=4>3
# print (b)
# c="21wdw"
# print (type(c))
# m=1+42
# print (m)


# kk="1234567"
# print (kk[3:6:2])
# ll="fefsfe"
# print (ll.upper())
# print (kk.upper())
# ac="fuwhuhiw"
# f=ac.count("w")
# print(f)
# f=ac.index("w")
# print(f)
# f=ac.replace('h','333',3)
# print(f)
# f=ac.startswith('f')
# print(f)
# f=ac.endswith('w')
# print(f)

# ab="1+{li}={c}"
# f=ab.format(li=2,c=22)
# print(f)
# ab='1+%s=%s'
# f=ab%('fkwf','www45')
# print(f)
# ak='sdwwd'
# f=len(ak)
# print(f)
# a='WWwWedRFEWSdwd'
# b=a.count('W')
# print(b)

# abc=['wggg','2e33','dwdwd','$','+++']
# print(abc[-2])
# a=list("123")
# print(a[-1])
# abc.append("dwdwjkjn")
# print(abc)
# abc.remove(12)
# print(abc)
# abc.sort()
# print(abc)

# abc.reverse()
# print(abc)

# f=abc.count('+++')
# print(f)

# c=['ddww','wwdww',222]
# abc.extend(c)
# print(abc)

# dd=abc.copy()
# print(dd)

# ee=dd.copy()
# print(ee）
# import copy
# abc=[1,2,3,55,'www45','duhiue',[122,'2e2e','dwdwjkjn']]
# bc=copy.deepcopy(abc)
# abc[-1].append(198484)
# print(abc)
# print(bc)
# a=(12,'www45')

# abc={'name':['小明'],
#       'age':18,
#       'sex':'男'
#      }
# # print(abc)
# # print(abc['sex'])
# # print(type(abc))

# abc['wget']=123
# abc['age']=22
# abc['name'].append('小李')
# print(abc)
# f=abc.pop('sex')
# print(f)

# abc.popitem()
# print(abc)
# print(abc.keys())
# print(abc.values())
# print(abc.items())
# abc={'name':['小明'],
#       'age':18,
#       'sex':'男'
#      }

# bc={'hhh':12,'dwdwjkjn':344}
# abc.update(bc)
# print(abc)
# print(bc)

# abc={'abc','WWwWedRFEWSdwd',44,33}
# print(type(abc))
# print(abc)
# abc.pop()
# print(abc)
# abc.remove(44)
# print(abc)
# abc.add(32322)
# abc.add('345655q')
# print(abc)

# a=3
# a
# print(a)

# a=1
# if a>2:
# 	print(1)
# else:
# 	print('hahaha')

# a=input(`请输入成绩`)
# print(type(a))
# if  a>90 and a<=100:
# 	print("优秀")
# elif a>80 and a<=100:
# 	print("良好")
# elif a>70 and a<=80:
# 	print("一般")
# elif a>60 and a<=70:
# 	print("及格")
# else:
# 	print("渣渣")


# a = ['电脑','手机','计算机','mp4']
# for i,j in enumerate(a):
#     print(i+1,j)

# m = input('请输入您的总资产:')
# m = int(m)
# a = ['电脑','鼠标','游艇','美女','手机','计算器','mp4']
# b = [1999,10,20,998,1500,30,50]
# for i,j in enumerate(a):
#     print(i+1,j)
# c=[]
# while True:
#     d = input('请输入购买的商品号:')
#     try:
#         d = int(d)
#         print(a[d-1],b[d-1])
# 		c.append(b[d-1])
#     except:
# 		if d == '确认':
# 		break
# 		elif d == '删除':
# e = input('请输入要删除的商品号：')
# e = int(e)
# c.pop(b[e-1])
# else:
#     print('输入有误,请重新输入')
#     continue
# f=0
# for g in range(len(c)):
# f = f + int(c[g])
# print(f)
# while TRUE
# 	if m >= f
#     	h=m-f
# 		print('购买成功')
# 		break
# 	else:
# 		print('资产不足,差:', f-m)
# 		k = input('请继续充值:')
# 	try:
# 		k=int(k)
#    		l=k-(f-m)
#    	if l >= 0:
#    		print('成功')
#    	else：
#    		print(‘失败‘)
# 	except：
#    		k=‘退出’
#    		break





# m=input('请输入您的总资产:')
# m=int(m)
# a=['电脑','鼠标','游艇','美女','手机','计算器','mp4']
# b=['1999','10','20','998','1500','30','50']
# for i,j in enumerate(a):
#     print(i+1,j)
# c=[]
# while True:
#     d=input('请输入购买的商品号:')
#     try:
#         d=int(d)
#         print(a[d-1],b[d-1])
# 	except
# 		print(i)
		# if d == '确认':
     	# 	break
		# elif	d == '删除':
		# 	e = input('请输入要删除的商品号：')
		# 	e = int(e)
		# 	c.pop(b[e-1])
		# else:
    		# print('输入有误,请重新输入')
    		# continue
# f=0
# for g in range(len(c)):
# 	f = f + int(c[g])
# print(f)
# while TRUE:
# 	if m >= f:
#     	h=m-f
# 		print('购买成功')
# 		break
# 	else:
# 		print('资产不足,差:', f-m)
# 		k = input('请继续充值:')
# 	try:
# 		k=int(k)
#    		l=k-(f-m)
#    	if l >= 0:
#    		print('成功')
#    	else：
#    		print("失败")
# 	except:
#    		k="退出"
#    		break


# e=0
# c=[]
# d=int(input('请输入你的充值资金：'))
# a = [['电脑',3000],['cpu',1200],['显卡',500],['硬盘',800]]
# for i,j in enumerate(a):
#     print(i+1,j)
# while True:
#     b = int(input('请输入购买的商品号:'))
#     if b == 0:
#         for f in range(len(c)):
#             e = c[f] + e
#         print('总共:',e)
#         if e > d :
#             print('您的余额不足，请充值后再来购买')
#             o =input('请充值:')
#             o =int(o)
#             d =d+o
#             continue
#         else:
#             e=d-e
#             print('找您:',e,'欢迎下次光临')
#         break
#     elif  b >= len(a)+1:
#         print('输入有误，请重新输入')
#     else:
#         b = int(b)
#         print(a[b-1])
#         c.append(a[b-1][1])

# 质数之和
# sum=0
# for i in range(2,100):
# 	for j in range(2,i+1):
# 		if i%j == 0:
# 			break
# 	if i == j:
# 		sum=sum+i
# print(sum)


# 去重
# a=['dwuwh','dhwuih','222','duwh','222','duwh']
# b=[]
# for i in a:
# 	if i not in b:
# 		b.append(i)
# 	else:
# 		continue
# print(b) 
#

# 阶乘：
# o=0
# m=input('请输入数:')
# m=int(m)
# m=4
# i=1
# for j in range(1,m+1):
# 	s=i*j
# 	o=o+s 
# print(o)


# 打印列表中第一大和第二大的元素：
# a=[112,33,33,4,522,444,444,522,444,444]
# a.sort()
# c=[]
# for i in range(len(a)//2):
# 	if int(a[i]) < int(a[-i-1]):
# 		c.append(a[-i-1])
# 	elif int(a[i]) == int(a[-i-1]):
# 		c.append(a[i])
# 		c.append(a[-i-1])
# print(c)



# a=[12,33,44,55,64,55]
# b=a.copy()
# b=list(set(b))
# b.sort()
# c = a.count(b[-1])
# d = a.count(b[-2])
# print('{},'.format(b[-1])*c)
# print('{},'.format(b[-2])*d)


# 用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
# a=2
# b=1
# c=0.5
# m=100
# for i in range(101):
# 	for j in range(101):
# 		if 

# 九九乘法表
# def cfb():
# 	for i in range(1,10):
# 		for j in range(1,i+1):
# 			print('{}*{}={}'.format(j,i,i*j),end='\t')
# 		print('')
# cfb()

# 质数之和
# def zszh():
# 	s=0
# 	for i in range(2,100):
# 		for j in range(2,i+1):
# 			if i%j ==0:
# 				break
# 		if i == j:
# 			s += i
# 	print(s)
# zszh()	

# 阶乘之和：
# a=0
# m=input('请输入数值:')
# m=int(m)
# i=1
# for j in range(1,4):
# 	s=i*j
# 	a +=j
# print(a)

# 判断三角形:
# abc=[]
# for i in range


# 不用int将字符串变整数：
# def bzs(x):
# 	x=x[::-1]
# 	print(x)
# 	s=0
# 	for i in range(len(x)):
# 	 	for j in range(10):
# 	 		if str(j) == x[i]:
# 	 			s=s+j*10**i
# 	print(s)

# bzs('345')


# for i in range(1,1000):
# 	s=0
# 	for j in range(1,i):
# 		if i % j==0:
# 			s=s+j
# 	if s==i:
# 		print(s)


# a=[12,33,44,55,64,55]
# b=a.copy()
# b=list(set(b))
# b.sort()
# c = a.count(b[-1])
# d = a.count(b[-2])
# print('{},'.format(b[-1])*c)
# print('{},'.format(b[-2])*d)


# m=['11','dww','dwda','fwd']
# a='22'
# print(a.join(m))

# 十进制转十六进制：
# def szsl()
# 	for i in 

# def wj(x):
# 	f = open('a.txt','r',encoding='utf-8')
# 	a=readlins()
# 	b=a[::-1]
# 	for i in b:
# 		if x in a[i]:
# 			print(a[i])
# 	f.close()
# wj(#)

# def s(x,y):
# 	sum=0
# 	for i in range(x,y):
# 		for j in range(2,i+1):
# 			if i % j == 0:
# 				break
# 		if i == j:
# 			sum += i
# 	print(sum)
# 	return sum

# s(30,40)
a=1
print(a)