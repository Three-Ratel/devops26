#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process

class myProcess(Process):

    def __init__(self,n):
        self.n=n
        super().__init__()

    def run(self):
        print(self.n)
        print('run func ing')

if __name__ == '__main__':
    p=myProcess(20)
    p.start()
