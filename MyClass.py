#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
############面向对象#############
class MyClass:
    ''' 一个简单的类型实例  '''
    i = 12345;
    def f(self):
        return "hello,python"
# 实例化类
x = MyClass()
print("MyClass 类属性i为：",x.i)
print("MyClass 类的方法为：",x.f())
