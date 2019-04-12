#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Dingkk"

import HTMLTestRunnertest   #产生测试报告
import requests
import unittest
import time
class wo(unittest.TestCase):
    def setUp(self):
    #是每次执行用例之前
    #初始化测试环境，让测试环境变成最开始的状态
        print('hello')
    def test_1(self):
        self.assertEqual(123,123)
    def test_2(self):
        self.assertEqual(432,432)
    def test_3(self):
        self.assertNotEqual(123,567)
    def tearDown(self):
    #是每次用例结束之后执行
    #清理测试环境
        print('world')
if __name__=='__main__':
    #创建一个测试套件
    suit=unittest.TestSuite()
    #添加测试用例
    for i in range(1,4):
        suit.addTest(wo('test_{}'.format(i)))
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    f=open('at.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title='索赔测试报告',tester='JIdongyang',description='结果如下')
    # 定义测试报告内容
    runner.run(suit)
    f.close()
