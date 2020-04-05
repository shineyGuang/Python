#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lib import Excute_SQL
from config import Current_User
from lib.Decorate import auth


def create_blog():
    title = input("请输入文章标题：")
    if title.upper() == "N":
        return
    content = input("请输入文章内容：")
    if content.upper() == "N":
        return
    confirm = input("确认发布？[Y/N]")
    if confirm.upper() == "Y":
        sql_create_blog = "insert into blog (title, content) values ('%s', '%s');" % (
            title,
            content,
        )
        Excute_SQL.excute_sql(sql_create_blog)
        print("文章发布成功！".center(30, "*"))
    return


def create_comment(bid):
    comment = input("请评论(N返回上一级)：")
    if comment.upper() == "N":
        return
    current_user_id = Excute_SQL.excute_sql(
        "select id from user where name = '%s';" % Current_User.CURRENT_USER
    )
    print(current_user_id)
    sql_create_comment = (
        "insert into comment (uid, details, cid) values ('%s', '%s', '%s');"
        % (current_user_id[0].get("id"), comment, bid)
    )
    Excute_SQL.excute_sql(sql_create_comment)
    print("评论成功！".center(15, "="))
    return


def call_up(bid):
    sql_call_up = "update blog set up = up + 1 where id = '%s';" % bid
    Excute_SQL.excute_sql(sql_call_up)
    print("点赞成功！".center(10, "="))


def show_details():
    while True:
        id = input("选择博文序号(N返回上一级):")
        if id.upper() == "N":
            return
        res = Excute_SQL.excute_sql("select content from blog where id='%s'" % id)
        print("%s\n" % res[0].get("content"))
        comments = show_comments(id)
        for item in comments:
            print(f"    {item.get('name')}：{item.get('details')}\n")

        print("1.评论；   2.点赞")
        func_dic = {"1": create_comment, "2": call_up}
        choice = input("选择序号(N返回上一级)：")
        func = func_dic.get(choice)
        if choice.upper() == "N":
            return
        if not func:
            continue
        func(bid=id)


def show_comments(id):
    sql_comments = (
        "select name, details from user left join comment on user.id = comment.uid where cid = '%s';"
        % id
    )
    res = Excute_SQL.excute_sql(sql_comments)
    return res


@auth
def show_titles():
    print("文章列表".center(30, "*"))
    while True:
        res = Excute_SQL.excute_sql("select * from blog;")
        if not res:
            print("什么也没有~~~~~")
        else:
            for i in range(len(res)):
                print(
                    "%s.%s\n点赞：%s"
                    % (res[i].get("id"), res[i].get("title"), res[i].get("up"))
                )
        print("1.创建博文；2.查看博文")
        choice = input("请选择序号(N返回上一级)：")
        if choice.upper() == "N" or not choice:
            return
        func_dic = {"1": create_blog, "2": show_details}
        func = func_dic.get(choice)
        if not func:
            print("输入序号有误".center(30, "*"))
            continue
        func()


if __name__ == "__main__":
    current_user_id = Excute_SQL.excute_sql(
        "select id from user where name = '%s';" % "CC"
    )
    print(current_user_id)
