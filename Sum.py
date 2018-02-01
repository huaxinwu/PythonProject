#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
'''  通过用户输入两个数字，并计算连个数字之和  '''
# 用户输入的数字
num1 = input("请输入第一个数字:")
num2 = input("请输入第二个数字:")
# 求和
sum = float(num1) + float(num2)
# 打印 测试
print("数字 {0} 和 {1} 相加结果为:{2}".format(num1,num2,sum))
