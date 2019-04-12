#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"


# 自动登录QQ空间

# from selenium import webdriver
# from time import sleep
#
# dr = webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys(1335953243)
# sleep(5)
# dr.find_element_by_id('p').send_keys('DK970326.m')
# sleep(5)
# dr.find_element_by_id('login_button').click()
# sleep(5)
# dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[4]/div[1]/div/ul/li[1]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys(' ^-^ web ^-^ ')
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/div[4]/div[4]/a[2]/span').click()
# sleep(10)
# dr.quit()



# 登录京东，并把python的第一个图书加入购物车


# from selenium import webdriver
# from time import  sleep
# dr = webdriver.Firefox()
# dr.get('https:www.jd.com')
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[2]/li[1]/a[1]').click()
# sleep(3)
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
# sleep(3)
# dr.find_element_by_id('loginname').send_keys('15936512341')
# sleep(5)
# dr.find_element_by_id('nloginpwd').send_keys('15936512341.')
# sleep(5)
# dr.find_element_by_id('loginsubmit').click()
# sleep(10)
#
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('python')
# sleep(4)
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button/i').click()
# sleep(3)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a[2]/span').click()
# sleep(5)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(10)
#
# # print(dr.current_window_handle)
# # dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
# # sleep(2)
# # 获取所有窗口的句柄
# qq = dr.window_handles
#
# # 切换句柄  参数只能是句柄
# dr.switch_to.window(qq[-1])
#
# dr.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/div/div[2]/div[3]/a[1]').click()
# sleep(5)
# dr.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/a').click()
# sleep(3)
#
# gg = dr.window_handles
# dr.switch_to.window(gg[-1])
# sleep(4)
#
#
# sleep(13)
# dr.quit()


import unittest
from ddt import ddt,data,unpack

@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')
    @data([1,2,3])
    def test_1(self,value):
        print(value)

    @data([3,2,1],[5,3,2],[10,4,6])
    @unpack
    def test_minus(self,a,b,expected):
        actual = int(a) - int(b)
        expected = int(expected)
        self.assertEqual(actual, expected)

    @data([2,3],[4,5])
    def test_compare(self,a,b):
        self.assertEqual(a,b)

    def tearDown(self):
        print('this is tearDown')

if __name__ == '__main__':
    unittest.main(verbosity=2)