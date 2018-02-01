#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        # 数据末尾添加一个空字符串不换行
        print('{}x{}\t'.format(i,j,i*j),end='')
    # 换行
    print()
