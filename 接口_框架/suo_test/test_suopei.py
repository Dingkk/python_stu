#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
import requests
from 接口_框架.cofing import suopei
from 接口_框架.data import suopei_duqu

class suopei_case(unittest.TestCase):
    shuju =suopei_duqu.suopei_shuju()
    shuju123 =shuju.duqu_jichushuju()
    def test_1(self):
        suo=suopei.Suopei()
        asd=suo.jichushuju(int(self.shuju123[0][0]),int(self.shuju123[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'],'多装')

    def test_2(self):
        suo = suopei.Suopei()
        asd = suo.jichushuju(int(self.shuju123[1][0]),int(self.shuju123[1][1]))
        self.assertEqual(asd['message'],'get error')



if __name__=='__main__':
    unittest.main()