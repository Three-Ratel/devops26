from datetime import datetime
import os, sys
import shutil


# 1.数据类型 list  tuple  dict   set
# 计算   max  min
# 类型转换 hex  oct   chr ord
# len
# 2  random  hashlib  time  json

# 3   a=json.dumps({"ddf":"你好"},ensure_ascii=False)

# 4

def reg():
    name = input('pls input username ')
    pwd = input('pls input pwd')
    t = datetime.now()

    t = t.strftime('%Y-%m-%d-%H:%M:%S')
    print(t)
    l = []
    l.append(name)
    l.append(pwd)
    l.append(t)
    l.append('0')
    with open('user.txt', mode='a', encoding='utf8') as f:
        print(l)
        data = '|'.join(l) + '\n'
        f.write(data)


def login():
    with open('user.txt', mode='r', encoding='utf8') as fil, open('sf.txt', mode='r+', encoding='utf8') as sf:
        l = []
        for i in fil:
            i = i.strip()
            user = i.split('|')
            l.append(user)
        print(l)
        x = 0
        while True:
            name = input('pls input username ')
            pwd = input('pls input pwd')
            for item in sf:
                if name in item:
                    print(',已锁定过的账号.错误三次')
                    sys.exit(0)

            for item in l:
                if name == item[0]:
                    if pwd == item[1]:
                        print('welcome login')
                        return name
                        # sys.exit(0)
                    else:
                        x = x + 1
                        if x == 3:
                            sf.write(name)
                            print('错误三次')
                            sys.exit(0)


def main_func():
    print('1,注册  2 登陆 三次机会')
    i = int(input('pls choice'))
    if i == 1:
        reg()
    elif i == 2:
        login()


# main_func() #测试
