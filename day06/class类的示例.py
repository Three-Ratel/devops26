#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
class Car(object):
    def fly(self):
        print('会飞')
    def run(self):
        print('会跑')
    def gotohell(self):
        print('上西天')



class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def run(self):
        print('人会跑')
    def chi(self):
        print('人会吃')
p=Person('jay',28,'boy')
p.run()
p.chi()
print(os.getcwd())
print(__file__)