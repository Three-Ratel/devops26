#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle

ls=['lsa']
bs=pickle.dumps(ls)
obj=pickle.loads(bs)
print(bs,obj)

import json

dic={'我':1,2:None,3:True,4:False}
S=json.dumps(dic,ensure_ascii=False)
print(S,type(S))
x=json.loads(S)
print(x,type(x))
