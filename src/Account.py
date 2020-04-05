#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lib import Md5
from lib import Excute_SQL
from config import Current_User


def register():
    print("用户注册！".center(30, "*"))
    while True:
        user_name = input("请输入姓名(N返回上一级)：").strip()
        if user_name.upper() == "N":
            return
        sql_name = "select name from user where name='%s'" % user_name
        res = Excute_SQL.excute_sql(sql_name)
        print("res:==>", res)
        if res:
            print("用户名存在，请重新输入！")
            continue
        pass_word = input("请输入密码(N返回上一级)：").strip()
        if pass_word.upper() == "N":
            return
        sql = "insert into USER (name, pwd) values ('%s', '%s');" % (
            user_name,
            Md5.encrypt_md5(pass_word),
        )
        Excute_SQL.excute_sql(sql)
        print(f"{user_name}注册成功！".center(30, "*"))


def login():
    print("登录界面".center(30, "*"))
    while True:
        user = input("请输入用户名(N返回上一级)：").strip()
        if user.upper() == "N":
            return
        pwd = input("请输入密码(N返回上一级)：").strip()
        if pwd.upper() == "N":
            return
        sql_login = "select name from USER where name='%s' and pwd='%s'" % (
            user,
            Md5.encrypt_md5(pwd),
        )
        res = Excute_SQL.excute_sql(sql_login)
        print(res)
        if not res:
            print("登录失败！".center(30, "*"))
            continue
        if res[0].get("name") == user:
            print("登录成功！".center(30, "*"))
            Current_User.CURRENT_USER = user
            return
        else:
            print("登录异常！")
            return
