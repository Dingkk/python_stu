#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"
from 接口_框架.report.baogao import baogao_


def run(aa):
    baogao_(aa)

with open('回归.txt','r') as f:
    a = f.readlines()
    if len(a) == 1:
        run('*')
    else:
        run(a)


