# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:34:25 2023

@author: maste
"""

def is_palindrome(s):
    left = 0
    right = -1
    for i in range(len(s)//2):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def main1():
    print(is_palindrome("racecar"))
    print(is_palindrome("racecar1"))
    


def reverse_vowels(input_str): #could be better
        list_str = list(input_str) 
        left = 0
        right = len(list_str) - 1
        vowels = "aeiou"
        while left < right:
            if list_str[right] not in vowels:
                right -= 1
            if list_str[left] not in vowels:
                left += 1
            if list_str[left] in vowels and list_str[right] in vowels:
                list_str[left], list_str[right] = list_str[right], list_str[left]
                left += 1
                right -= 1
        return "".join(list_str)
    
def main2():
    print(reverse_vowels("tandon"))
    print(reverse_vowels("ababobo"))
    
def find_missing(lst):
    #worst case: theta(n^2)
    left = 0
    right = len(lst) - 1
    if lst[0] != 0:
        return 0
    while left <= right:
        mid = (left+right)//2
        if mid == lst[mid] and lst[mid+1] == mid+2:
            return mid + 1
        elif mid < lst[mid]: #index too small: missing number already occured
            right = mid - 1
        else:
            left = mid + 1
    return len(lst)

            
    
def find_missing_unsorted(lst):
    need = sum(range(len(lst)+1))  
    total = sum(lst)
    return need - total

def main3c():
    lst = [8,6,0,4,3,5,1,2]
    print(find_missing_unsorted(lst))

def find_pivot(lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left+right)//2
        if lst[mid-1] > lst[mid]:
            return mid
        elif lst[mid] < lst[0]:
            right = mid - 1
        else:
            left = mid + 1
    return None

def shift_binary_search(lst, target):
    left = None
    right = None
    pivot = find_pivot(lst)
    if lst[0] > target:
        left = pivot
        right = len(lst) -1
    else:
        left = 0
        right = pivot - 1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

def main4b():
    nums = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]
    print(shift_binary_search(nums, 00))

    
        
        
        
        