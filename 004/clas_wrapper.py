#!/usr/bin/env python
# -*- coding:utf-8 -*-

def wrapper(func):
    def inner(*args,**kwargs):
        print('找alex问行情')
        rv= func(*args,**kwargs)
        print('关外挂')
        return rv
    return inner

@wrapper
def yue():
    print('吃饭')
@wrapper
def lol():
    print('撸啊撸ing')

#yue()
lol()
