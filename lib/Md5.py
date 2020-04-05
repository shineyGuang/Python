#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib


def encrypt_md5(password):
    """
    md5加密
    """
    m = hashlib.md5()
    m.update(password.encode("utf-8"))
    return m.hexdigest()
