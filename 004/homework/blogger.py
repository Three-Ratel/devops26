#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random, json, time
import homework4reglogin

USER = None


def wrapper(func):
    def inner(*args, **kwargs):
        if USER:
            func(*args, **kwargs)
        else:
            print('需要登录啊')

    return inner


def login():
    global USER
    USER=homework4reglogin.login()
    # name = input('pls input username: ')
    # passwd = input('pls input pwd: ')
    # l = []
    # for i in range(0, 4):
    #     l.append(chr(random.randint(65, 90)))
    # scode = ''.join(l)
    # print('请输入右侧图像', scode)
    # code = input('pls input securet code ')
    # if name == 'alex' and passwd == '123' and code == scode:
    #     print('welcome login %s' % name)
    #     global USER
    #     USER = name
    # return USER


def explor_blogs():
    with open('news.db', mode='r', encoding='utf8') as f:
        info = json.load(f)
        # print(info)
        for k, v in info.items():
            print('#====================================>')
            print('序号%s 博文标题内容:%s \n收藏数:%s\n回复内容:%s' % (k, v.get(k), v.get('star'), v.get('reply')))
        return info


@wrapper
def like_blogs():
    info = explor_blogs()
    likenu = int(input('说,给谁点赞收藏呢:(输入博客序号)'))
    with open('news.db', mode='w', encoding='utf8') as f:
        # info = json.load(f)
        # print('载入完毕',info)
        for k, v in info.items():
            if int(k) == likenu:  # 是选择的博文
                print('修改之前: ', info)

                info[k]['star'] = str(int(info[k]['star']) + 1)
        # db = json.dumps(info, ensure_ascii=False)
        db = json.dumps(info)
        print('修改之后: ', info)
        print('转换之后: ', db)
        f.write(db)


@wrapper
def reply_blogs():
    info = explor_blogs()
    likenu = int(input('请选择需要回复的博文'))
    text = input('回复内容balabala:....')
    with open('news.db', mode='w', encoding='utf8') as f:
        # info = json.load(f)
        # print('载入完毕',info)
        for k, v in info.items():
            if int(k) == likenu:  # 是选择的博文
                print('修改之前: ', info)

                info[k]['reply'].append(text)

        # db = json.dumps(info, ensure_ascii=False)
        db = json.dumps(info)
        print('修改之后: ', info)
        print('转换之后: ', db)
        f.write(db)


def reg():
    homework4reglogin.reg()
def logout():
    global USER
    USER = None

def dairy():
    with open('olddairy',mode='r',encoding='utf8') as f:
        for i in f:
            print(i)



if __name__ == '__main__':
    while True:
        dic = {1: 'login', 2: 'reg', 3: 'explor_blogs', 4: 'dairy', 5: 'reply_blogs', 6: 'like_blogs'}
        print('''欢迎来到博客园首页
        1:请登录
        2:请注册
        3:文章页面
        4:日记页面
        5:评论页面
        6:收藏页面
        7:注销
        8:退出程序''')
        s = int(input('请选择功能: '))
        if s == 1:
            login()
        elif s == 2:
            reg()
        elif s == 3:
            explor_blogs()
        elif s == 4:
            dairy()
        elif s == 5:
            reply_blogs()
        elif s == 6:
            like_blogs()
        elif s == 7:
            logout()
        elif s == 8:
            exit()
