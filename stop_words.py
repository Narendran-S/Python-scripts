# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:22:20 2020

@author: kiddy
"""


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

stopwords = set(w.upper() for w in stopwords)
acro = ''.join(i[0] for i in org.upper().split(' ') if i not in stopwords)