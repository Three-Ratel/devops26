#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

n = 100000000
struct_time = time.localtime(n)
print(struct_time)  # python时间格式

s = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(s)  # 转为字符串
# s = input('请输入一个时间%Y-%m-%d %H:%M:%S')
struc_tim = time.strptime(s, "%Y-%m-%d %H:%M:%S")  # 字符串转时间格式
print(struc_tim)
n = time.mktime(struc_tim)  # py时间格式转时间戳
print(n)
print('===>')
s1 = "1989-01-01 12:00:00"
s2 = "1989-01-02 14:35:00"
start = time.strptime(s1, "%Y-%m-%d %H:%M:%S")#转时间格式
end = time.strptime(s2, "%Y-%m-%d %H:%M:%S")
print('s1和s2是%s ,  %s' % (s1, s2))
s3 = time.mktime(start)#转时间戳
s4 = time.mktime(end)
print('s3和s4是%s ,  %s' % (s3, s4))
sf = s4 - s3#相减
print(sf)
sf = time.gmtime(sf)#此处使用localtime 时区减去8
finaltime = time.strftime('%H:%M:%S', sf)
print(finaltime)
