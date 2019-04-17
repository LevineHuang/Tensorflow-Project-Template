# -*- coding:utf-8 -*-  
""" 
@file: _init_paths.py
@time: 2019-04-17 23:22

@author: Levine Huang 
@contact: levinehuang@163.com
@site:  
@project: Tensorflow-Project-Template
@software: PyCharm 
"""

import os
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = os.getcwd()

root_path = os.path.join(this_dir, '..', '')
add_path(root_path)