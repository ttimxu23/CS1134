# -*- coding: utf-8 -*-
"""
CS1134 Lab 6 Coding
"""
#1: sum_to
def sum_to(n):
    if n == 0:
        return 0
    else:
        sum_rest = sum_to(n-1)
        return sum_rest + n
#print(sum_to(5))

#2: product_evens
def product_evens(n):
    if n == 2:
        return 2
    else:
        prod_rest = product_evens(n-2)
        return prod_rest * n
#print(product_evens(8))

#3: find_max
"""
a. the runtime is O(n^2), because the function will make
n-1 recursive calls until lst is len 1, and each recusive
call is O(n) because it requires list slicing which is linear
T(n) = O((n-1)*n) = O(n^2)
"""
#3b: linear find_max
def find_max(lst, low, high):
    if low == high:
        return lst[high]
    else:
        max_rest = find_max(lst, low+1, high)
        if lst[low] > max_rest:
            return lst[low]
        else:
            return max_rest
#print(find_max([2,60,1,0,12,5,1000],0,6))

#4: valid palindrome
def is_palindrome(string, low, high):
    #problems: invalid with empty string - what should I do with empty string?
              #also indexing out of range is common, which I think is fine in the case of this problem?
    if low >= high:
        return True
    else:
        if string[low] != string[high]:
            return False
        return is_palindrome(string, low+1, high-1)
#print(is_palindrome("racecar", 1, 5))

#5: binary search
def binary_search(lst, low, high, val):
    if low > high:
        return None
    else:
        #test to see if recursive call is working properly
        #print(lst[low:high+1])
        mid = (low+high)//2
        if lst[mid] == val:
            return mid
        elif lst[mid] > val:
            return binary_search(lst, low, mid-1, val)
        else:
            return binary_search(lst, mid+1, high, val)
#print(binary_search([0,1,2,3,4,5,6,7,8],0,8,9))
    
#6: vowel and consonant count
def vc_count(word, low, high):
    vowels = "aeiouAEIOU"
    if low == high:
        if word[high] in vowels:
            return (1, 0)
        else:
            return (0, 1)
    else:
        count_rest = vc_count(word, low+1, high)
        if word[low] in vowels:
            return (count_rest[0] + 1, count_rest[1])
        else:
            return (count_rest[0], count_rest[1] + 1)
#print(vc_count("NYUTandonEngineering",0,19))
         
    
    
    
    
    
    
    
    