# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:46:22 2023

@author: maste
"""

def powers_of_two(n):
    for i in range(n+1):
        yield 2**i
        

        