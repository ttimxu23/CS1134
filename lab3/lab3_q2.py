# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:21:09 2023

@author: maste
"""

def move_zeroes(nums):
    checker = 0
    tomove = 0
    for i in range(len(nums)):
        if nums[checker] != 0:
            nums[checker], nums[tomove] = nums[tomove], nums[checker]
            tomove += 1
        checker += 1

            
        
        
lst = [0,1,0,3,13,0,0,14,0,0,19]
move_zeroes(lst)
print(lst)
    