#!/usr/bin/env python
# -*- coding:utf-8 -*-

lst = ['烂片', '妇联', '蜘蛛侠', '蝙蝠侠']

it = lst.__iter__()

# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())#StopIteration

while True:
    try:
        print(it.__next__())
    except StopIteration as e:
        print('没了')
        break

from collections import Iterable, Iterator

print(isinstance(lst, Iterable))
print(isinstance(lst, Iterator))

print(isinstance(it, Iterable))
print(isinstance(it, Iterator))


def func(n):
    if isinstance(n, Iterable):
        for x in n:
            print(x)
    else:
        print(n)


func(123)
func('asdf')


def gen():
    print('111')
    yield 1
    print('2222')
    yield 2


v = gen()
print(v)
print(v.__next__())


# print(v.__next__())

def order():
    for i in range(1000):
        yield '衣服' + str(i)


o = order()
print(o.__next__())
print(o.__next__())
print(o.__next__())
print(o.__next__())
print(o.__next__())

v = ['周末班%s' % i for i in range(1, 10) if i % 2 == 0]
print(v)

lst = ["欧阳娜娜", "张崔猛", "欧阳难过", "张亚无照", "胡一飞", "胡怎么飞", "张炸辉"]
v = [i for i in lst if '张' in i]
print(v)

# [1, 4, 9, 16, 25, 36]

# 在[3,6,9]的基础上推到出[[1,2,3], [4,5,6],[7,8,9]]

print([i * i for i in range(1, 7)])
v1 = [3, 6, 9]
print([[i - 2, i - 1, i] for i in v1])
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst = ['张三丰', '张无忌', '张翠山']

print({i: lst[i] for i in range(len(lst))})

v = (i for i in range(10))
print('====================')


def func():
    print(111)
    yield 222


g = func()
g1 = (i for i in g)
g2 = (i for i in g1)
print(list(g1))
print(list(g2))
print(list(g))

s = 18
print(format(18, "f"))

lst = ['高俅', '波多野结衣', '苍老师', '仓木麻衣']


def func(lst):
    return len(lst)


print(sorted(lst, key=func))

lst = [{"id": 1, "name": 'alex', "age": 18},
       {"id": 2, "name": 'wusir', "age": 16},
       {"id": 3, "name": 'taibai', "age": 17}]


# 用age排序
def age_sort(d):
    return d.get('age')


print(sorted(lst, key=age_sort))
print('=========')
print(list(filter(lambda d: d.get('age') >= 18, lst)))
#结果:[{'id': 1, 'name': 'alex', 'age': 18}]