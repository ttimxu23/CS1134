# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:56:50 2023

@author: maste
"""

class Polynomial:
    
    def __init__(self, coef_list = 0):
        self.coef_list = coef_list
        
    def __add__(self, other):
        if len(self.coef_list) > len(other.coef_list):
            longer = self.coef_list
            shorter = other.coef_list
        else:
            shorter = self.coef_list
            longer = other.coef_list
        output = []
        for i in range(len(shorter)):
            output.append(shorter[i] + longer[i])
        for i in range(len(shorter), len(longer)):
            output.append(longer[i])
        return Polynomial(output)
    def __call__(self, num):
        output = 0
        for i in range(len(self.coef_list)):
            output += self.coef_list[i] * (num ** i)
        return output
    def __repr__(self):
        ls = []
        for i in range(len(self.coef_list)):
            if i > 0 and self.coef_list[i] > 0:
                ls.append(str(self.coef_list[i])+"x^"+str(i))
            if i == 0:
                ls.append(str(self.coef_list[0]))
        ls.reverse()
        return " + ".join(ls)
    
a = Polynomial([3,0,0,2,1])
b = Polynomial([0,0,0,0,0,6,7])
print(a+b)