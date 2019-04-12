#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"

import xlrd
class shouye01(object):
    def shouye_duqu(self):
        shuju=[]
        f = xlrd.open_workbook(r'E:\python_学习\接口_框架\data\suopei.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju
if __name__=='__main__':
    print(shouye01().shouye_duqu())
