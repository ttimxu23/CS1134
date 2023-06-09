# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:40:38 2023

@author: maste
"""

def max_sum_sub(nums, k):
    sub_len = len(nums)//k
    ind1 = 0
    ind2 = sub_len - 1
    max_sum = sum(nums[ind1: ind2+1])
    cur_sum = max_sum
    while ind2 < len(nums)-1:
    
        ind1 += 1
        ind2 += 1
        cur_sum -= nums[ind1-1]
        cur_sum += nums[ind2]
        if cur_sum > max_sum:
            max_sum = cur_sum
            
    return max_sum

nums= [1,12,-5,-6,50,3]
max_sum = max_sum_sub(nums,2)
print(max_sum)
 