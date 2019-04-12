#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Dingkk"

import requests
import unittest
# unittest 单元测试框架
 # 主要的作用：对用例进行管理和执行
# 面向对象
# 所有的用例函数，必须以test开头
class suopei(unittest.TestCase):
    def test_1(self):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
        head = {
            'Content-Type':'application/json',
            'x-dealer-code':'2100150',
            'x-position-code':'D_PO_1028',
            'x-resource-code':'BASIC_DATA',
            'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code':'djy0mx',
            'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'
            }
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res = requests.post(url,headers=head,data=body)
        mes = res.json()
        self.assertEqual(mes['data']['applicationType'][0]['name'],'多装')
    def test_2(self):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
        head = {
            'Content-Type': 'application/json',
            'x-dealer-code': '2100150',
            'x-position-code': 'D_PO_1028',
            'x-resource-code': 'BASIC_DATA',
            'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code': 'djy0mx',
            'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb'
        }
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res = requests.post(url, headers=head, data=body)
        mes = res.json()
        self.assertNotEqual(mes['data']['applicationType'][0]['name'],'多装')
    def setUp(self):  #初始化测试环境
#         是在每次执行用例之前执行
        print('pass1')

    def tearDown(self):  #清理测试环境     （setup，teardown任何测试用例都要在相同的环境下执行。）
#         是每次用例执行结束之后执行
        print('pass2')
    def test_3(self):
        print('hello')

    def test_4(self):
        print('word')

# main相当于一个控制器，检测类中所有以test开头的函数
#  执行顺序;  比较test后面的字符，谁在前就先执行谁。
if __name__=='__main__':
    unittest.main()