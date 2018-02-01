#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
# 定义函数
def printme(str):
    print(str);
    return ;
# 调用函数
printme("你好，Python");

###############变量作用域####################
# 内建作用域
x = int(2.9);

# 全局作用域
g_count = 0;

def outer():
    # 闭包函数外的函数中
    o_count = 1;

    def inner():
        # 局部作用域
        i_count = 2;

##############列表当做栈堆或者队列使用####################
list = [3,4,5];
stack = list;
stack.append(6);
stack.append(7);
print(stack);
stack.pop();
print(stack);

##############队列：因为所有其他的元素都得一个一个地移动，从第一个开始#################
from collections import  deque;
queue = deque(["Lucy","Tone","Johe"]);
queue.append("Tome");
queue.append("Gome");
print(queue);
print(queue.popleft());

####################列表推导式##############################
vec = [2,4,6];
print([3*x for x in vec]);
print([[x,x*2] for x in vec]);

#########################嵌套列表解析##################################
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
];
# 3x4---4x3矩阵
print([[row[i] for row in matrix] for i in range(4)]);

##############引用模块##########################
import Support;
Support.print_func("Python");
import  sys;
print(sys.path);
print(dir(sys));