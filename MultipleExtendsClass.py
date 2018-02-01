#!/usr/bin/env python3.5.2
# -*- coding:utf-8 -*-
######################多继承##############################
# 定义类
class people:
    name = ''
    age = 0
    # 定义私有属性,类外部无法直接访问
    __weight = 0
    # 定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    #  普通方法
    def speek(self):
            print("%s 说: 我 %d 岁。"%(self.name,self.age))

#  单继承示例
class student(people):
    grade = ''
    # 定义构方法
    def __init__(self,n,a,w,g):
        # 调用父类构造方法
        people.__init__(self,n,a,w)
        self.grade = g
    # 重写父类方法
    def speek(self):
        print("%s 说: 我 %d 岁。我在读%d年级"%(self.name,self.age,self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim", 25, 80, 4, "Python")
# 方法名同，默认调用的是在括号中排前地父类的方法
test.speak()



