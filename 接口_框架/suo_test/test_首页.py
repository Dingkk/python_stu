#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"

import unittest
import requests
from 接口_框架.cofing import 查询订单
from 接口_框架.data import 首页_读取

class shouye_case(unittest.TestCase):
    shuju= 首页_读取.shouye01()
    shuju123=shuju.shouye_duqu()
    def test_SY01(self):
        shou =查询订单.chaxun
        qwe=shou.chaxundingdan(int(self.shuju123[1][0]),int(self.shuju123[1][1]))
        self.assertEqual(qwe['totalSize'],9)

    def test_SY02(self):
        shuo=查询订单.chaxun
        qwe=shuo.chaxundingdan(int(self.shuju123[2][0]),int(self.shuju123[2][2]))
        self.assertEquals(qwe['errMsg'],'处理成功')
if __name__=='__main__':
    unittest.main()