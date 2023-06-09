# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:20:13 2023

@author: maste
"""
import random

def create_permutation(num):
    lst = []
    for i in range(num):
        lst.append(i)
    new_lst = []
    for i in range(num):
        rand_ind = random.randint(0, len(lst)-1)
        new_lst.append(lst[rand_ind])
        lst.pop(rand_ind)
    return new_lst

def scramble_word(word):
    ind_order = create_permutation(len(word))
    scrambled = []
    for i in range(len(ind_order)):
        scrambled.append(word[ind_order[i]])
    return "".join(scrambled)

def scramble_game(word):
    scrambled = scramble_word(word)
    letters = " ".join([char for char in scrambled])
    print("Unscramble the word:", letters)
    tries = 1
    guess = None
    while guess != word and tries <= 3:
        guess = input("Try #{}: ".format(tries))
        if guess != word:
            print("Wrong!")
            tries += 1
    if guess == word:
        print("You got it!")
    else:
        print("Unlucky! you didn't get it!")
        
        
scramble_game("pokemon")