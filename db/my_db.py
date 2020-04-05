#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql


class My_DB(object):
    def __init__(
        self,
        host="localhost",
        port=3306,
        db="blog_user_info",
        user="root",
        passwd="123",
        charset="utf8",
    ):
        self.conn = pymysql.connect(
            host=host, port=port, user=user, passwd=passwd, db=db, charset=charset
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    with My_DB() as db:
        # db.execute("select * from USER ;")
        try:
            db.execute("insert into USER (name, pwd) values ('GG','6890');")
            print(db)
            for i in db:
                print(i)
        except Exception as e:
            print("Error!")
            db.conn.rollback()
