# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:38:24 2023

@author: maste
"""


def shift(lst, k):
    k = k%len(lst)
    
    for i in range(0,-(len(lst)-k),-1):
        (lst[i], lst[i-k]) = (lst[i-k], lst[i])
    
def main():
    lst = [1,2,3,4,5,6]
    shift(lst, 3)
    print(lst)
    
main()





