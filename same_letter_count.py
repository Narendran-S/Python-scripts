# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:41:42 2020

@author: kiddy
"""


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.


same_letter_count = sum(w[0] == w[-1] for w in sentence.split())
print(same_letter_count)