#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
'''  通过用户输入一个数字，并计算这个数字的平方根 '''
num = float(input("请输入一个数字:"))
num_sqrt = num ** 0.5
print('%0.3f的平方根为%0.3f'%(num,num_sqrt))