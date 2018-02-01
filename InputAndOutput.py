#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
##################输入和输出 表达式语句、print函数、wirte函数#####################
s = "hell,input";
print(str(s));
print(repr(s));
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'));

######################错误和异常##################################
#while True  期望一个冒号
#    print("hello,python")
# ZeroDivisionError: division by zeroZeroDivisionError: division by zero 异常
print(10*(1/0))