#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-

###############测试python语法等等################
import sys;


# 斐波那契数列
def fibonacci(n):
    a,b,counter = 0,1,0;
    while True:
        if(counter > n):
            return;
        yield a;
        a,b = b,a + b;
        counter+=1;
f = fibonacci(10);
while True:
    try:
        print(next(f),end=" ");
    except StopIteration:
        sys.exit();



