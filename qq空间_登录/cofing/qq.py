#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"



from selenium import webdriver
from time import sleep
import unittest
from ddt import ddt, data, unpack


def login(argument, u, p):
    argument.find_element_by_id('switcher_plogin').click()
    sleep(5.0)
    argument.switch_to.default_content()
    argument.switch_to_frame('login_frame')
    argument.find_element_by_id("u").send_keys(u)
    sleep(1.0)
    argument.find_element_by_id('p').send_keys(p)
    sleep(1.0)
    argument.find_element_by_class_name('login_button').click()
    sleep(1.0)
    return argument.title


@ddt  # 固定写法
class T1(unittest.TestCase):
    #
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.get(url='https://qzone.qq.com/')
        cls.dr.implicitly_wait(10.0)
        cls.dr.switch_to_frame('login_frame')

    # def test_1(self):
    #     dr.implicitly_wait(10.0)
    #     dr.switch_to_frame('login_frame')
    #     dr.find_element_by_id('switcher_plogin').click()
    #     sleep(5.0)
    #     dr.switch_to.default_content()
    #     dr.switch_to_frame('login_frame')
    #     dr.find_element_by_id("u").send_keys('825069672')
    #     sleep(1.0)
    #     dr.find_element_by_id('p').send_keys('houec1019')
    #     sleep(1.0)
    #     dr.find_element_by_class_name('login_button').click()
    #     sleep(1.0)

    @data(['1335953243,DK970326.m'])
    def test_2(self, value):
        # print(value)
        a = value[0].split(',')
        print(a)
        b = a[0]
        c = a[1].strip()
        print(c)
        d = login(self.dr, b, c)
        print(d)
        self.assertEquals('QQ空间-分享生活，留住感动',self.title)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main()
