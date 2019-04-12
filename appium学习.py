#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"
import unittest
from appium import webdriver
import time
from ddt import ddt,  data, unpack

# desired_caps={'platformName':'Android',
#               'deviceName':'127.0.0.1:62026',
#               'appPackage':'com.netease.cloudmusic',
#               'appActivity':'.activity.LoadingActivity'
#                }
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# print('hello word')
# time.sleep(12)
#
# driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()  #点击手机号登录
# time.sleep(2)
# driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('15936512341') #输入账号
# time.sleep(2)
# driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('15936512341.') #输入密码
# time.sleep(2)
# driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()#点击登录
# time.sleep(2)
#
#
#
# time.sleep(10)
# # 断言
#
#
# driver.find_element_by_id('com.netease.cloudmusic:id/qn').click() #点击抽屉菜单
# time.sleep(3)
#
# aa=driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
# if aa == 'Ding__kk':
#     print('pass')
# else:
#     print('fail')
# driver.quit()

def login(driver,u,p):
    driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()  # 点击手机号登录
    time.sleep(2)
    driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys(u)  # 输入账号
    time.sleep(4)
    driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys(p)  # 输入密码
    time.sleep(4)
    driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()  # 点击登录
    time.sleep(10)
    driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()  # 点击抽屉菜单
    time.sleep(3)
    return driver.title

@ddt
class Wangyi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.desired_caps = {'platformName': 'Android',
                        'deviceName': '127.0.0.1:62026',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': '.activity.LoadingActivity'
                        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        print('hello word')
        time.sleep(12)

    @data(['15537831769,gao19930903'],['15936512341,15936512341.'],[' , '],['15936512341,123456'],['123345613231,15936512341.'],['123413131323,2313113424'])
    def test_01(seif,value):
        a = value[0].split(',')
        print(a)
        b = a[0]
        c = a[1].strip()
        print(c)
        d = login(seif.driver,a,b)
        print(d)
        aa = seif.driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
        # seif.assertEquals(aa,'Ding__kk')
        if aa == 'Ding__kk':
            print('pass')
        else:
            print('fail')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()