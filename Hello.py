#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
print("hello python, 你好，趴生");
# 整型变量
counter = 100;

# 浮点型变量
miles = 1000.0;
# 字符串
name = "runoob";

print(counter);
print(miles);
print(name);
# 加减乘除
5 + 4  # 加法

4.3 - 2 # 减法

3 * 7  # 乘法

2 / 4  # 除法，得到一个浮点数

2 // 4 # 除法，得到一个整数

17 % 3 # 取余

2 ** 5 # 乘方
### 字符串 ##
str = "Runnob";
print(str);
#第一元素到倒数第二个元素，左闭合右开
print(str[0:-1]);
print(str[0]);
print(str[2:5]);
print(str[2:]);
#输出两个相同的
print(str*2);
print(str+"test");

###### 元祖 #####
tuple = ('abc',123,2.23,"agdc");
print(tuple);

#########字典########
dict = {};
dict['one']='1 - 菜鸟教程';
dict[2]='2 - 菜鸟工具';
print(dict['one']);
print(dict[2]);

##########成员运算符 in /not in################
a = 10;
b = 20;
list = {1,2,3,4,5,6};
if(a in list):
    print('a在list序列中');
else:
    print("a不在list序列中");

##############身份运算符 is /not is ######################
c = 30;
d = 30;
if(a is b):
    print("a和b是相同标识");
else:
    print("a和b不是相同标识");

##############if elif else语句##############################
age = int(input("请输入你的年龄:"));
if(age < 0):
    print("你在逗我吧");
elif(age == 1):
    print("相当于14岁的人");
elif(age == 2):
    print("相当于22岁的人");
else:
    print("相当于中年人");
### 退出
input("按下enter退出");

##############for else语句#####################
for i in range(5):
    print(i);