# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:48:36 2023

@author: maste
"""

def can_construct(word, letters):
    word_ls = [char for char in word]
    letters_ls = [char for char in letters]
    
    for char in letters_ls:
        if char in word_ls:
            word_ls.remove(char)
    
    if len(word_ls) == 0:
        return True
    else:
        return False