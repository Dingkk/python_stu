#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"
from  selenium import webdriver
import unittest
from time import sleep
from ddt import ddt,data,unpack
#
# # dr = webdriver.Firefox()
# # dr.get('https://qzone.qq.com/')
# # dr.implicitly_wait(10.0)
# # dr.switch_to.frame('login_frame')
# # sleep(2)
# # dr.find_element_by_id('switcher_plogin').click()
# # sleep(2)
# # dr.find_element_by_id('u').send_keys(1335953243)
# # sleep(5)
# # dr.find_element_by_id('p').send_keys('DK970326.m')
# # sleep(5)
# # dr.find_element_by_id('login_button').click()
# # sleep(5)
#
# def kjdl(dr,u,p):
#     dr.find_element_by_id('switcher_plogin').click()
#     sleep(5.0)
#     dr.switch_to.default_content()
#     dr.switch_to.frame('login_frame')
#     sleep(2)
#     dr.find_element_by_id('switcher_plogin').click()
#     sleep(2)
#     dr.find_element_by_id('u').send_keys(u)
#     sleep(5)
#     dr.find_element_by_id('p').send_keys(p)
#     sleep(5)
#     dr.find_element_by_id('login_button').click()
#     sleep(5)
#     return dr.title
# @ddt
# class qq(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.dr =webdriver.Firefox()
#         cls.dr.get(url='https://qzone.qq.com')
#         cls.dr.implicitly_wait(10.0)
#         cls.dr.switch_to_frame('kjdl.frame')
#
#     @data(['1335953243,Dk970326.m','12345,123456'])
#     def test_01(self,value):
#         a = value[0].split(',')
#         print(a)
#         b = a[0]
#         c = a[1].strip()
#         print(c)
#         d = kjdl(self.dr, b, c)
#         print(d)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()






from selenium import webdriver
option = webdriver.ChromeOptions()
# 伪装iphone登录
# # option.add_argument('--user-agent=iphone')
# # 伪装android
option.add_argument('--user-agent=android')
dr= webdriver.Chrome(chrome_options=option)
dr.get('http://www.taobao.com/')
dr.implicitly_wait(10.0)
dr.switch_to.frame('callapp_iframe_1554724913767')
dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/span[4]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div[1]').send_keys(15936512341)
sleep(2)
dr.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div[1]').send_keys('15936512341.')
sleep(2)
dr.find_element_by_xpath('//*[@id="btn-submit"]').click()
sleep(5)
dr.quit()