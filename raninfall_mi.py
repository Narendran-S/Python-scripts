# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:41:12 2020

@author: kiddy
"""

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi_split = rainfall_mi.split(",")
num_rainy_months = 0
for x in rainfall_mi_split:
    x = float(x)
    if x > 3.0:
        num_rainy_months += 1

print(num_rainy_months)