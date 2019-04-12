#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"
import unittest
from ap框架.app框架.config.百度输入法APP import bixu
from ap框架.app框架.date.duqu import duqu
import time
from appium import webdriver
from ddt import ddt,  data, unpack
@ddt
class test_shurufa(unittest.TestCase):
    shuju = duqu()
    @classmethod
    def setUpClass(cls):
        cls.desired_caps = {'platformName': 'Android',
                        'deviceName': '8BN0217912000957',
                        'appPackage': 'com.baidu.input',
                        'appActivity': '.ImeAppMainActivity',
                        'noReset': 'True'}
        cls.dr = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        time.sleep(10)

    def test_01(self):
        driver = bixu(int(self.shuju[0][0]),self.shuju[0][1])
        time.sleep(10)
        driver.find_element_by_class_name('android.widget.RelativeLayout').click()
        title=driver.find_element_by_class_name('android.widget.TextView')
        self.assertEquals(title.text,title.text)
        print('登录成功')
    def test_02(self):
        driver = bixu(int(self.shuju[1][0]),self.shuju[1][1])
        time.sleep(5)
        title = driver.find_element_by_id("login-submit")
        self.assertEqual(title.text, "登录")
        print("登陆失败")

    def test_03(self):
        driver = bixu(int(self.shuju[2][0]),self.shuju[2][1])
        time.sleep(5)
        title = driver.find_element_by_id("login-submit")
        self.assertEqual(title.text, "登录")
        print("登陆失败")

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

# if __name__ == '__main__':
#     unittest.main()