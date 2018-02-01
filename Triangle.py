#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
# 通过用户输入三角形三边长度，并计算三角形的面积
# （ 海伦公式）（p=(a+b+c)/2） S=sqrt[p(p-a)(p-b)(p-c)]
a = float(input('输入三角形的第一边长:'))
b = float(input('输入三角形的第二边长:'))
c = float(input('输入三角形的第三边长:'))

# 计算半周长
s = (a+b+c)/2
# 计算三角形面积 --海伦公式
area = (s*(s-a)*(s-b)*(s-c))**0.5

print('三角形面积为:%0.2f' %area)