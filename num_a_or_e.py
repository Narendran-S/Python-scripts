# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:44:35 2020

@author: kiddy
"""


sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for i in sentence.split():
    if ('a' in i) or ('e' in i):
        num_a_or_e += 1

print(num_a_or_e)

