#!/usr/bin/env python
# -*- coding:utf-8 -*-

# from shopmod import shopmod

'''
1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
5，退出则是退出整个程序。
'''

import gouwu

def login():
    with open('user.txt', mode='r', encoding='utf8') as f:
        for i in f:
            i = i.strip()
            ls = i.split('|')
            count = 0
            while count < 3:
                name = input('PLS input username')
                pwd = input('pls input pwd')
                if ls[0] == name and ls[1] == pwd:
                    print('login sucess')
                    shopping()
                else:
                    print('usernaem or pwd wrong')
                count += 1
            else:
                break


def reg():
    name = input('PLS input username')
    pwd = input('pls input pwd')
    with open('user.txt', mode='r+', encoding='utf8') as f:
        for i in f:
            i = i.strip()
            ls = i.split('|')
            if ls[0] == name:
                print('用户名已占用')
            else:
                data = name + '|' + pwd + '\n'
                f.write(data)


def shopping():
    # from shop_mod import shop_mod
    gouwu.rukou()

def shop_main():
    print('''
    1.login
    2.register
    3.shopping
    4.exit
    
    ''')

    cho = int(input('PLS choice :'))
    if cho == 1:
        login()
    elif cho == 2:
        reg()
    elif cho == 3:
        shopping()
    elif cho == 4:
        exit()


shop_main()
