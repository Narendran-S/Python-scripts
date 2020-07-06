# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:53:34 2020

@author: kiddy
"""


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores_split = scores.split(" ")
a_scores = 0
for x in scores_split:
    x = float(x)
    if x >= 90:
        a_scores += 1

print(a_scores)