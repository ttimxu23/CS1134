# -*- coding: utf-8 -*-
"""
cs1134 lab 7
"""

#1: SortLst
def SortLst(lst):
    for i in range(len(lst)):
        if lst[i] != i:
            lst[lst[i]], lst[i] = lst[i], lst[lst[i]]
lst = [0,3,2,5,4,1]
SortLst(lst)
print(lst)
#2: intersectionOfLst
def intersectionOfLst(lst1, lst2):
    res = []
    pt1 = 0
    pt2 = 0
    while pt1 < len(lst1) and pt2 < len(lst2):
        if lst1[pt1] > lst2[pt2]:
            pt2 += 1
        elif lst1[pt1] < lst2[pt2]:
            pt1 += 1
        else:
            res.append(lst1[pt1])
            pt1 += 1
            pt2 += 1
    return res

#3: isPowerOfTwo
def isPowerOfTwo(n):
    if n == 1:
        return True
    else:
        rest = isPowerOfTwo(n//2)
        if rest == True and n%2 == 0:
            return True
        else: 
            return False
        
#4: split_parity
def split_parity(lst, low, high):
    if low >= high:
        return 
    else:
        if lst[low]%2 == 0:
            split_parity(lst, low+1, high)
        else:
            lst[low], lst[high] = lst[high], lst[low]
            split_parity(lst, low, high-1)
        
#5: nested_sum(lst):
def nested_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        sum_rest = nested_sum(lst[1:])
        if type(lst[0]) == list:
            return sum_rest + nested_sum(lst[0])
        else:
            return sum_rest + lst[0]
#lst = [[1,2],3,[4,[5,6,[7],8]]]
def nested_depth_level(lst):
    if len(lst) == 0:
        return 1
    else:
        max_depth_rest = nested_depth_level(lst[1:])
        curr_depth = 1
        curr = lst[0]
        while type(curr) == list:
            curr_depth += 1
            curr = curr[0]
        if curr_depth > max_depth_rest:
            return curr_depth
        else: 
            return max_depth_rest
#print(nested_depth_level([[[[1]]],4,[5]]))












        
