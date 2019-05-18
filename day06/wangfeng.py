#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Singer(object):
    def __init__(self,name,salary,gender,songs):
        self.name=name
        self.salary=salary
        self.gender=gender
        self.songs=songs

    def sing(self,song):
        print(self.name,'唱歌',song)
    def party(self):
        for item in self.songs:
            self.sing(item)

s=Singer('wangfeng',100,'boy',['北京','怒放'])

# s.party()
# s.sing('huaci')

class BankAccounet(object):
    def __init__(self,card_num,initmoney):
        self.card_num=card_num
        self.initmoney=initmoney

    def inaccount(self,money):
        self.initmoney+=money

    def outaccount(self,money):
        self.initmoney-=money

    def currentmoney(self):
        print(self.initmoney)

acc=BankAccounet(110,300)
acc.inaccount(30)
acc.outaccount(20)
acc.currentmoney()





