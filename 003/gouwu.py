#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter


# 1.充值
def chognzhi():
    # cash = input('请充值:')
    cash = 5000
    print('充值金额是:', cash)
    return cash


chognzhi()
# 2.显示商品
def xianshi():
    shop_all = [
        {'name': '电脑', 'price': 1999}
        , {'name': '鼠标', 'price': 10}
        , {'name': '键盘', 'price': 20}
        , {'name': '音响', 'price': 998}
    ]



    for i in range(len(shop_all)):
        print(i + 1, shop_all[i]['name'], shop_all[i]['price'])
    print('n 购物车结算')
    return shop_all
shop_all=xianshi()
# 3.选择商品,添加到购物车.如果输入n则进行结算.如果输入错误,提示错误并重新输入

'''shop_list格式是:   [{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}, {'name': '键盘', 'price': 20}]'''


def pay_list(shop_list):
    def shop_all_info():
        '''#===================统计购买的内容===================#'''
        shop_list_one = []  # 去重的列表
        for item in shop_list:
            if item not in shop_list_one:
                shop_list_one.append(item)
        for item in shop_list_one:
            name = item['name']
            num_total = shop_list.count(item)
            price = item['price']
            print('商品{0},的数量是{1},单价是{2}'.format(name, num_total, price))
        return shop_list_one

    def total_judge():
        total_price = 0
        for item in shop_list:
            total_price += int(item['price'])
        balance = chognzhi() - total_price
        return total_price, balance

    total_price, balance = total_judge()
    while balance < 0:
        print('钱不够了')
        shop_all_info()
        print('==============>')
        for i in range(len(shop_list)):
            print(i + 1, shop_list[i])
        shopid = int(input('请输入要删除的商品序列号,商品如上'))
        shop_list.pop(shopid - 1)
        total_price, balance = total_judge()
    else:
        shop_all_info()

    return total_price, balance


def exit_shop(shop_list):
    total_price, balance = pay_list(shop_list)
    print('总花费%s,剩余%s' % (total_price, balance))
    exit()


shop_list = []

def rukou():
    while True:
        xianshi()
        info = input('请输入商品序列号:')
        if info == 'n':
            print('进入结算ing')
            # print('shop_list是:', shop_list)
            pay_list(shop_list)
            break
        if info.lower() == 'q':  # 退出程序打印内容
            exit_shop(shop_list)
            exit()
        if info.isdigit() and int(info) <= len(shop_all) and int(info) >= 1:
            nu = int(info)
            print('您已经选择:', shop_all[nu - 1]['name'], shop_all[nu - 1]['price'])
            shop_list.append(shop_all[nu - 1])
        else:
            print('输入错误,请重新输入')
            continue

# rukou()
if __name__ == '__main__':
    rukou()
