#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
、有变量name = "aleX leNb" 完成如下操作：
1)  移除 name 变量对应的值两边的空格,并输出处理结果
2)  移除name变量左边的"al"并输出处理结果
3)  移除name变量右面的"Nb",并输出处理结果
4)  移除name变量开头的a"与最后的"b",并输出处理结果
5)  判断 name 变量是否以 "al" 开头,并输出结果
6)  判断name变量是否以"Nb"结尾,并输出结果'''
# 1.1
name = "aleX leNb"
print(name.strip())
print(name.lstrip('al'))
print(name.rstrip('Nb'))
print(name.rstrip('b').lstrip('a'))
print(name.startswith('al'))
print(name.endswith(('Nb')))
'''
7)  将 name 变量对应的值中的所有的"l" 替换为 "p",并输出结果 print()
8)  将name变量对应的值中的第一个"l"替换成"p",并输出结果
9)  将 name 变量对应的值根据所有的"l" 分割,并输出结果。
10) 将name变量对应的值根据第一个"l"分割,并输出结果。'''
print(name.replace('l', 'p'))
print(name.split('l'))
print(name.split('l')[0])
'''
11) 将 name 变量对应的值变大写,并输出结果
12) 将 name 变量对应的值变小写,并输出结果
13) 将name变量对应的值首字母"a"大写,并输出结果
14) 判断name变量对应的值字母"l"出现几次，并输出结果
15) 如果判断name变量对应的值前四位"l"出现几次,并输出结果
16) 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
17) 从name变量对应的值中找到"N"对应的索引(如果找不到则返回‐1)输出结果
18) 从name变量对应的值中找到"X le"对应的索引,并输出结果
19) 请输出 name 变量对应的值的第 2 个字符?
20) 请输出 name 变量对应的值的前 3 个字符?
21) 请输出 name 变量对应的值的后 2 个字符?
22) 请输出 name 变量对应的值中 "e" 所在索引位置?
'''
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.count('l'))
print(name[:4].count('l'))
print(name.find('N', -1))
print(name.find('X le'))
print(name[1:2])
print(name[:3])
print(name[-2:])
print(name.index('e'))
# 2.
'''
)通过对s切片形成新的字符串s1,s1 = "123"
2)通过对s切片形成新的字符串s2,s2 = "a4b"
3)通过对s切片形成新的字符串s3,s3 = "1345"
4)通过对s切片形成字符串s4,s4 = "2ab"
5)通过对s切片形成字符串s5,s5 = "c"
6)通过对s切片形成字符串s6,s6 = "ba2"
'''
s = '123a4b5c'
s1 = s[0:3]
s2 = s[3:6]
s3 = s[::2]
s4 = s[0:-1:2]
s4 = s[1:-1:2]
s5 = s[-1]
s6 = s[-3:0:-2]
print(s4, s5, s6)
# 3.
for i in s:
    print(i)
lon = len(s)
i = 0
while i < lon:
    print(i)
    i += 1
# 4
s = 'asdfer'
l = []
l.append(s)
for i in l:
    print(i)

# 5
s = 'abcdefg'
for i in s:
    print(i + 'sb')

# 6
s = 321
s = str(s)
for i in range(len(s)):
    print('还剩余%s秒', s[i - 1])
    pass
# 7
# content=input('请输入内容:')
# l=content.split('+')
# total=0
# for i in l:
#     total+=int(i)

# 8
# content=input('请输入内容:')
# l=content.split('+')
# total=0
# for i in l:
#     total+=int(i.strip())

# 9
# content = input("请输入内容：")   # 如fhdal234slfh98769fjdla10、写代码，完成下列需求：用户可持续输入（用while循环），用户使用的情况：输入A，则显示走大路回家，然后在让用户进一步选择：是选择公交车，还是步行？选择公交车，显示10分钟到家，并退出整个程序。选择步行，显示20分钟到家，并退出整个程序。输入B，则显示走小路回家，并退出整个程序。输入C，则显示绕道回家，然后在让用户进一步选择：是选择游戏厅玩会，还是网吧？选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。11、写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？16、制作趣味模板程序需求：等待户输名字、地点、爱好，根据户的名字和爱好进任意现实如：敬爱可亲的xxx，最喜欢在xxx地xxx17、等待户输内容，检测户输内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输”，并允许户重新输并打印。敏感字符：“粉嫩”、“铁锤”18、写代码，有如下列表，按照要求实现每一个功能li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]1)计算列表的长度并输出2)列表中追加元素"seven",并输出添加后的列表3)请在列表的第1个位置插入元素"Tony",并输出添加后的列表4)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表5)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。7)请删除列表中的元素"eric",并输出添加后的列表8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表9)请删除列表中的第2至4个元素，并输出删除元素后的列表10)请将列表所有得元素反转，并输出反转后的列表11)请计算出"alex"元素在列表li中出现的次数，并输出该次数。19、写代码，有如下列表，利用切片实现每一个功能
#
# t=0
# for i in content:
#     print(i)
#     if i.isdigit():
#         t+=1
# print('t的内容是',t)

# 10
# while True:
#     content = input('请输入:')
#     if content == 'A':
#         print('走大路回家')
#         content = input('交通工具:')
#         if content == 'bus':
#             print('十分钟')
#             exit(
#
#             )
#         elif content=='不行':
#             print('20min')
#             exit()
#         elif content=='B':
#             print('小楼')
#             exit()
#         elif content=='C':
#             print('绕路回家')
#             con=input('continue input')
#             if con=='gamebar':
#                 print('xxx')
#             elif con=='netbar':
#                 print('xx')

# 11
t = 0
for i in range(100):
    if i == 88:
        pass
    else:
        t += i
print(t)
# 16
# name=input('name')
# place=input('place')
# hobby=input('hobby:')
# print('敬爱的{0},喜欢在{1},didian{1}'.format(name,place,hobby))

# 18

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
'''
1)计算列表的长度并输出
2)列表中追加元素"seven",并输出添加后的列表
3)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
4)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表'''
print(len(li))
li.append('seven')
print(li)
li.insert(0, 'tony')
print(li)
li[1] = 'kelly'
print(li)
'''
5)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
7)请删除列表中的元素"eric",并输出添加后的列表
8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
9)请删除列表中的第2至4个元素，并输出删除元素后的列表
10)请将列表所有得元素反转，并输出反转后的列表11)请计算出"alex"元素在列表li中出现的次数，并输出该次数。#       
'''
l2 = [1, "a", 3, 4, "heart"]
li.extend(l2)
print(li)
# 6
s = "qwert"
li.extend(s)
print(li)
# li.remove('eric')
# print(li)
print(li.pop(1), li)
#9
print('====>')
l=[]
for i in range(1,4):
    l.append(li.pop(i))
print(l,li)
li.reverse()
print(li)
print(li.count('alex'))
#19 ....

