# -*- coding: utf-8 -*-
"""
CS1134 Lab 9 Coding Q3
"""

from ArrayQueue import * 

def flatten_list_by_depth(lst):
    output = []
    q = ArrayQueue()
    for elem in lst:
        q.enqueue(elem)
    while not q.is_empty():
        curr = q.dequeue()
        if type(curr) == int:
            output.append(curr)
        else:
            for elem in curr:
                q.enqueue(elem)
    return output
            
        
def main():
    lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
    new_lst = flatten_list_by_depth(lst)
    print(new_lst)
    
main()