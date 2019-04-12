# -*- coding: utf-8 -*- 

# @Time : 2019/4/8 下午12:46 

# @Author : 废柴 

# @Project: jianshu

# @FileName : tools.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

import yaml

def element(var):
    """
    读取定位元素文件方法---加载ElementPage目录下的各个马甲包文件定位文件名
    :param var: 保存定位元素文件的路径
    :return: 定位元素文件的全部数据
    """
    with open(var, 'r', encoding='utf-8') as fb:
        return yaml.load(fb)
