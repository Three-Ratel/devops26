#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ls=['风','云','乔峰','扫地方','乔峰','风']
# print(set(ls))
#
# new=set(ls)

f = open('log.txt', mode='r', encoding='utf8')
# content=f.read(3)
# print(content)
# for i in f:
#     print(i.strip())

data = f.readlines()
print(data)

f = open('fruit.txt', mode='r', encoding='utf8')
ls = []

ks = f.readline()
firs = ks.strip().split(',')
print('ks is', ks)

result = []
for lines in f:
    dic = {}
    line = lines.strip().split(',')
    for x in range(len(line)):
        dic[firs[x]] = line[x]

    result.append(dic)
print(result)
print(ls)
f.close()

f = open('log.txt', mode='w', encoding='utf8')
f.write('1223')
f.write('4444')

f.close()
f = open('log.txt', mode='a', encoding='utf8')
f.write('666')
f.write('777')

f.close()


def date(tools):
    print('1')
    print(f'2{tools}')
    print('...')


date('momo')
print('ing')
date('yy')


def login(name, pwd):
    if name == 'alex' and pwd == '123':
        return True


re = login('alex', '123')
print(re)

def max_test(a,b):
    return a if a>b else b

print(max_test(1,2))

def luru(name,age,height,gender='男'):
    print(name,age,gender,height)

luru('hp',18,188)
luru('xiaoA',18,188,'nv')

def eat(*args):
    print(args)
eat('fan','面','汤')

def eat(**kwargs):
    print(kwargs)
eat(main='面',soup='疙瘩汤',icecream='hagen-daz')

def eat(a,b,c,*args,d=99):
    print(a,b,c,d,args)

eat(1,2,3,d=100,*(4,5))