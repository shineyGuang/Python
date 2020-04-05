#!/usr/bin/env python
# -*- coding:utf-8 -*-
from config import Current_User


def auth(func):
    def inner(*args, **kwargs):
        if not Current_User.CURRENT_USER:
            print("未登录，请登录！".center(30, "@"))
            return
        func(*args, **kwargs)

    return inner
