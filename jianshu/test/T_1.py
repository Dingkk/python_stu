# -*- coding: utf-8 -*- 

# @Time : 2019/4/8 下午12:02 

# @Author : 废柴 

# @Project: jianshu

# @FileName : T_1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

import unittest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from jianshu.config.C_1 import login
from ddt import ddt, file_data, data, unpack
import HTMLTestRunnertest
import time


@ddt
class JianShu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Firefox()
        cls.dr.get("https://qzone.qq.com/")
        cls.dr.implicitly_wait(5.0)  # 隐性等待
        # 强制等待
        sleep(1.0)
        # 显性等待
        wait_element =(By.ID, "login_frame")
        try:
            WebDriverWait(cls.dr, 10, 0.5).until(EC.presence_of_element_located(wait_element))
        except:
            print("frame元素未找到！")

    # 没有测试数据文件导入的写法
    # def test_1(self):
    #     a = login(self.dr, username='825069672', password='houec1029')
    #     sleep(1.0)
    #     self.assertEqual(a, '唯美一生')

    # 有测试文件导入的写法

    @file_data(r'E:\python_学习\jianshu\data\login.json')
    def test_2(self, var):
        # print(var)
        for i in var:
            print(i)
            print(i['username'])
            print(i['password'])
            a = login(self.dr, username=i['username'], password=i['password'])
            try:
                self.assertEqual(a, 'YOYO、')
            except:
                self.assertEqual(a, "QQ空间-分享生活，留住感动")
                self.dr.refresh()


    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)



