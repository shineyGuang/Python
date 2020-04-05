#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
from src import run

base_dir = os.path.dirname(os.path.dirname(os.path.__file__))
sys.path.append(base_dir)

if __name__ == "__main__":
    run.run()
