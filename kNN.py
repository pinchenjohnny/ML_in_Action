#!/usr/bin/env python
# -*- coding:utf-8 -*-
# proj: ML_in_Action
# author:Pin Chen
# datetime:2022/5/23 17:42

from numpy import *
import operator

# ===============
# common
# ===============
def createDateSet():
    group = array([
        [1., 1.1],
        [1., 1.],
        [0, 0 ],
        [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels