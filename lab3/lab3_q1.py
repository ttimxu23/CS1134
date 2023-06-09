# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:08:47 2023

@author: maste
"""

def reverse_list(lst, low = None, high = None):
    if low == None:
        low = 0
    if high == None:
        high = len(lst) - 1
    for i in range((high-low)//2 + 1):
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    
lst = [1,2,3,4,5,6]
reverse_list(lst, 1)
print(lst)
