#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Dingkk"
import HTMLTestRunnertest
from 接口_框架.report import HTMLTestRunnertest
import unittest
from 接口_框架.suo_test.test_suopei import suopei_case

def baogao_(aa):
    suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(suopei_case))
    for o in aa:
        dis = unittest.defaultTestLoader.discover('E:\python_学习\接口_框架\suo_test',pattern='test_{}.py'.format(o.strip()))
    #两个参数，第一个路径  ，第二个，匹配条件
    #到这个路径下，匹配所有的一test开头的文件
    #test 开头文件中找到函数以test开头的函数
        for i in dis:
            suit.addTest(i)
    f = open(r'E:\python_学习\接口_框架\d.html','wb')
    runner= HTMLTestRunnertest.HTMLTestRunner(stream=f,title='查询索赔单列表测试报告',tester='Ding kk',description='报告结果如下')
    runner.run(suit)
    f.close()

def run(aa):
    baogao_(aa)
# if __name__ == '__main__':
#     baogao_()