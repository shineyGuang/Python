#!/usr/bin/env python
# -*- coding:utf-8 -*-
from db.my_db import My_DB


def excute_sql(sql):
    res = []
    with My_DB() as db:
        try:
            db.execute(sql)
            for i in db:
                res.append(i)
            return res
        except Exception as e:
            print(f"数据库异常{e}")
            # db.conn.rollback()
