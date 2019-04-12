# -*- coding: utf-8 -*- 

# @Time : 2019/4/8 下午12:03 

# @Author : 废柴 

# @Project: jianshu

# @FileName : C_1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
from jianshu.config.tools import element
from selenium import  webdriver
from time import sleep


a = element(r'E:\python_学习\jianshu\element\login.yaml')
# 返回一个字典
print(a)

#
# dr = webdriver.Chrome()
# dr.get("https://qzone.qq.com/")
# dr.implicitly_wait(5.0)
# dr.switch_to.frame(a['frame_id'])
# dr.find_element_by_id(a['login']['l_id']).click()
# dr.find_element_by_id(a['login']['u_id']).send_keys('825069672')
# sleep(1.0)
# dr.find_element_by_id(a['login']['p_id']).send_keys('houec1019')
# sleep(1.0)
# dr.find_element_by_id(a['login']['s_id']).click()
# dr.quit()


# 定义登录函数
def login(arg, username, password):
    arg.switch_to.frame(a['frame_id'])
    arg.find_element_by_id(a['login']['l_id']).click()
    arg.find_element_by_id(a['login']['u_id']).send_keys(username)
    sleep(1.0)
    arg.find_element_by_id(a['login']['p_id']).send_keys(password)
    sleep(1.0)
    arg.find_element_by_id(a['login']['s_id']).click()
    return arg.title

