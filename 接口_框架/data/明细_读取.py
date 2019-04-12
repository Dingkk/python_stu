#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"

import xlrd
class mingxi01(object):
    def mingxi_duqu(self):
        shuju04=[]
        f = xlrd.open_workbook(r'E:\python_学习\接口_框架\data\suopei.xls')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i==0:
                continue
            else:
                shuju04.append(sheet.rom_values(i))
        return shuju04
if __name__=='__main__':
    print(mingxi01().mingxi_duqu())

