# !/user/bin/python
# -*- coding:utf-8 -*-
import xlrd
import xlwt
with open('a.txt','r',encoding='utf-8') as f:
	s=f.readlines()
with open('b.txt', 'r', encoding='utf-8') as h:
	m=h.readlines()
with open('d.txt','r',encoding='utf-8') as q:
	p=q.readlines()
	b = xlwt.Workbook(encoding='utf-8')
	sheet = b.add_sheet('test.xls')
for i, j in enumerate(s+m+p):
	j = j.replace('\n', '').split(',')
	for k in range(len(j)):
		sheet.write(i, k, j[k])
b.save('test.xls')
