#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"
from appium import webdriver
from time import sleep
import unittest

def bixu(u,p):
    desired_caps =  {'platformName': 'Android',
                            'deviceName': '8BN0217912000957',
                            'appPackage': 'com.baidu.input',
                            'appActivity': '.ImeAppMainActivity',
                            'noReset': 'True'}
    dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(10)

    dr.find_element_by_id('com.baidu.input:id/banner_settings').click()
    sleep(3)
    dr.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView[2]').click()
    sleep(8)
    dr.find_element_by_id('login-otherLogin').click()
    sleep(3)
    dr.find_element_by_id('login-username').send_keys("{}".format(u))
    sleep(3)
    dr.find_element_by_id('login-password').send_keys("{}".format(p))
    sleep(3)
    dr.find_element_by_id('login-submit').click()
    sleep(5)
    print('登录成功')
    return dr
    # return dr.title
# if __name__ == '__main__':
#     unittest.main()