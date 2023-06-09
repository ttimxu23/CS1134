# -*- coding: utf-8 -*-
"""
tzx201_hw3_q4
"""

def remove_all(lst, val):
    to_move = 0
    removed = 0
    for i in range(len(lst)):
        if lst[i] != val:
            lst[to_move] = lst[i]
            to_move += 1
        else:
            removed += 1
    for i in range(removed):
        lst.pop()
    

def main():
    lst  = [3,2,4,5,6,2,34,6,6,7,78,3]
    remove_all(lst, 2)
    print(lst)
    
