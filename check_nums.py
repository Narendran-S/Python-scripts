# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:12:18 2020

@author: kiddy
"""
#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.


def check_nums(x):
    sub = []
    x = (num for num in x) 
    num = next(x, 7)  
    while num != 7:
        sub.append(num)
        num = next(x, 7)  
    return sub

x = [1, 3, 4, 5, 6, 7, 3]
print(check_nums(x))