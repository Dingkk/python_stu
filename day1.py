#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Dingkk"
import HTMLTestRunnertest
import requests
import unittest

class lianxi(unittest.TestCase):
    def setUp(self):
        print("pass hello")

    def test_4(self):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/queryApplication"
        head = {'Content-Type':'application/json','x-dealer-code':'2100150','x-position-code':'D_PO_1028','x-resource-code':'QUERY_APPLICATION','x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394','x-user-code':'djy0mx','x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
        body ='{"pageNum":"1","pageSize":"10","orderByField":"","orderByrule":"","status":"","applicationType":"","applicationMode":"","applicationNo":"","partCode":"","applicationStartDate":"","applicationEndDate":""}'
        res = requests.post(url, headers=head, data=body)
        mes = res.json()
        self.assertNotEqual(mes['totalSize'], '0')


    def test_1(self):
        self.assertEqual(123,123)

    def test_2(self):
        self.assertEqual(432,432)

    def test_3(self):
        self.assertNotEqual(123,567)

    def tearDown(self):
        print("pass word")

if __name__ == '__main__':
    suit = unittest.TestSuite()

    for i in range(1,5):
        suit.addTest(lianxi('test_{}'.format(i)))
    s=open('LX001.html','wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(stream=s,title='查询索赔单列表测试报告',tester='Ding kk',description='报告结果如下')
    runner.run(suit)
    s.close()
 