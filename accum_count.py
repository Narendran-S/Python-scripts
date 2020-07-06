# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:42:43 2020

@author: kiddy
"""


items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if 'w' in i:
        acc_num += 1

print(acc_num)
