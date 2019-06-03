#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
import requests


def writeimg(url, i):
    ret = requests.get(url)
    res = ret.content
    with open('img%s.jpg' % i, mode='wb') as f:
        f.write(res)


# url_list = []

url_list = [
    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369819138&di=b55c855e6d1078ee31e1b1b447ca6501&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180812%2Fca01fb5aba994936a47d5640ed4e48d9.jpeg",
    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369819138&di=b55c855e6d1078ee31e1b1b447ca6501&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180812%2Fca01fb5aba994936a47d5640ed4e48d9.jpeg",
    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559369818983&di=36ccc51b913cb17d6385502b79818398&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Ff8b28a79d598c9a7597a5bec93cf64b8e2f5589435839-ejtiMv_fw658"

]

if __name__ == '__main__':
    p_list = []
    for i, url in enumerate(url_list):
        p = Process(target=writeimg, args=(url, i + 1))
        p.start()
        p_list.append(p)
    [pp.join() for pp in p_list]
