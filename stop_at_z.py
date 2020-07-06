# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:17:00 2020

@author: kiddy
"""


def stop_at_z(list):
   i = 0
   while i < len(list):

       if (list[i] == 'z'):
           return list[0:i]
       i+=1
   return list[0:i]
print(stop_at_z(['a','b','c','z']))