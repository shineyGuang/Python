#!/usr/bin/env python
# -*- coding:utf-8 -*-
from src import Account
from src import Blog


def run():
    print("欢迎进入博客！".center(50, "="))
    func_dict = {
        "1": Account.register,
        "2": Account.login,
        "3": Blog.show_titles,
    }
    while True:
        print("1.注册；2.登录；3.文章列表")
        choice = input("请选择序号(N退出)：")
        if choice.upper() == "N" or not choice:
            continue
        func = func_dict.get(choice)
        if not func:
            print("序号选择错误！")
            continue
        func()
