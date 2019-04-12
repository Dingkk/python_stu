#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"

# #web自动化
# # 环境搭建
# # 1.需要安装python
# # 2.安装selenium模块
# # 3.下载浏览器驱动器
# from selenium import webdriver
# from time import sleep
# # 定义使用什么浏览器
# dr = webdriver.Chrome()
# #打开网址
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.get('https://www.jd.com')
# sleep(2)
#
# # 回退
# dr.back()
# sleep(2)
# # 前进
# dr.forward()
# sleep(2)
#
#
# # 设置浏览器的大小
# dr.set_window_size(200,200)
# sleep(2)
#
# # 设置浏览器的位置
# dr.set_window_position(600,200)
# sleep(2)
# # 设置浏览器最大化（全屏)、
# dr.maximize_window()
# sleep(2)
#
# # 最小化
# dr.minimize_window()
# sleep(2)
#
# # 定位  是核心
# #1.  ID 定位    标签的id属性   通过id来定位
# dr.find_element_by_id('kw').send_keys('12306抢票')
# sleep(2)
# # click  点击
# dr.find_element_by_id('su').click()
# # 2. class_name 定位  标签的class的属性
# dr.find_element_by_class_name('s_ipt').send_keys('12306抢票神奇')
# sleep(2)
# dr.find_element_by_class_name('btn self-btn bg s_btn btnhover').click()
# # 3.name定位   标签上的name属性
# dr.find_element_by_name('wd').send_keys('12306抢票神奇')
# dr.find_element_by_id('su').click()
# # 4.link_test定位   标签的文本定位
# dr.find_element_by_link_text('地图').click()
# # 5.partial_link_text 定位  标签页的模糊文本定位
# dr.find_element_by_partial_link_text('hao').click()
# # 6.tag_name  最不唯一的一个定位，通常用来定位一组数据
# dr.find_elements_by_tag_name('input')
# # 通过css_selector    css来定位
# dr.find_element_by_css_selector('#kw').send_keys('122')
# # 8. xpath定位  路径定位
# #xpath 路径标记语言
# #xml  可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('12306')
# #  唯一性   id > css > xpath > name > class_name ……
# # 获取网址的标题
# print(dr.title)
# # 获取打开网页的网址
# print(dr.current_url)
# # quit 关闭浏览器，断开浏览器，cloce 关闭浏览器不断开连接
# dr.quit()
#
# # 定义一组数据   同时对多个数据操作的时
# wd = dr.find_elements_by_class_name('mnav')
#
# # 模拟动作   每次只能有一次动作
# #send_keys()   输入
# #click（）    点击
# #text     获取定位到的元素的文本
# #clear   清空定位到的元素上的数据
#
#
# # 层级定位   遇到复杂的元素的时候
# # 进入携程官网，自动连续选择酒店级别
# dr = webdriver.Chrome()
# dr.get('https://www.ctrip.com/?sid=155947&allianceid=4897&ouid=cuoP&gclid=CMa9muqMtuECFcObvAodNlMARA&gclsrc=ds')
# sleep(2)
# wd = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in wd:
#     i.click()
#     sleep(4)

# from selenium import webdriver
# from selenium.webdriver.common.keys import keys
# from time import sleep
# dr = webdriver.Firefox
# dr.maximize_window()
#
# dr.get('https://qzone.qq.com/')
# sleep(2)
#
# # 处理框架     iframe
# dr.switch_to.frame("login_frame")
# # dr.switch_to.frame () 框架的id或name或者，先定位到框架
# # 切换到某一个框架
# # dr.switch_to.frame()
#
# # 回到到最开始的页面上
# dr.switch_to.default_content()
#
# # 回到父框架页面上
# dr.switch_to.parent_frame()
#
#
#
#
# from selenium import webdriver
#
# from time import sleep
#
# dr= webdriver.Firefox()
# dr.get('https://www.douban.com/')
# sleep(2)
#
# #处理浏览器窗口
# # 获取当前窗口的字符串（句柄）
# print(dr.current_window_handle)
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
# sleep(2)
# # 获取所有窗口的句柄
# qq = dr.window_handles
#
# # 切换句柄  参数只能是句柄
# dr.switch_to.window(qq[-1])
#
#
#
#
# # 鼠标的操作。
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# from time import  sleep
# dr = webdriver.Firefox()
# dr.get('https:www.jd.com')
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul[2]/li[1]/a[1]').click()
# sleep(3)
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
# sleep(3)
# dr.find_element_by_id('loginname').send_keys('15936512341')
# sleep(5)
# dr.find_element_by_id('nloginpwd').send_keys('15936512341.')
# sleep(5)
# dr.find_element_by_id('loginsubmit').click()
# sleep(3)
# start = dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
#
# # drag_and_drop(起始位置，结束位置)
#
# # drag_and_drop_by_offset(1起始位置，x轴坐标，y轴坐标)
#
# ActionChains(dr).drag_and_drop_by_offset(start,68,0,).perform()
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
#
# 处理滚动条  JavaScript 代码
# for i  in range(1,10000,2000):
#     js="var q=document.documentElement.scrollTop={}".format(i)
#     # 执行 JavaScript 语句
#     dr.execute_script(js)
#     sleep(2)
#
#
#
# 智能等待
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# from time import  sleep
# import selenium.webdriver.support.ui as ui
# dr = webdriver.Firefox()
# dr.maximize_window()
# dr.get('http://www.jd.com')
#
# # 强制等待
# # sleep(2)
#
# # 智能等待    设置一个最大等待时间，检测到某个元素出现，就不会继续等待
# # 设置最大等待时间
# unit = ui.WebDriverWait(dr,10)
# # 直到定位的元素出现，就不等待
# unit.until(lambda dr:dr.find_element_by_xpaath('/html/body/div[1]/div[3]/div/div[5]/ul[1]/li[1]/a').is_displayed())
# print('hello word')
#



from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import  sleep
import selenium.webdriver.support.ui as ui
dr = webdriver.Firefox()
dr.maximize_window()
dr.get('http://www.jd.com')

sleep(2)
w = dr.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[5]/ul[1]/li[1]/a')

# 获取定位到的元素某个属性的值。
a=w.get_attribute('herf')






# 刷新当前页面
dr.refresh()