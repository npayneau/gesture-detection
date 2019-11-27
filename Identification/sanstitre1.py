# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:04:34 2019

@author: Jules
"""


import time
import progressbar

bar = progressbar.Bar(maxval=20)
bar.start()
for i in range(20):
    time.sleep(0.1)
    bar.update(i)