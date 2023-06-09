# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:56:20 2023

@author: maste
"""

class Complex:   
    def __init__(self, a, b):
        self.a = a
        self.b = b       
    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Complex(new_a, new_b)  
    def __sub__(self, other):
        new_a = self.a - other.a
        new_b = self.b - other.b
        return Complex(new_a, new_b)   
    def __mul__(self, other):
        new_a = (self.a * other.a) - (self.b * other.b)
        new_b = (self.a * other.b) + (self.b * other.a)
        return Complex(new_a, new_b) 
    def __repr__(self):
        if self.b > 0:
            string = str(self.a) + " + " + str(self.b)+"i"
        else:
            string = str(self.a) + " - " + str(self.b*-1)+"i"
        return string
    def __iadd__(self, other):
        self.a = self.a + other.a
        self.b = self.b + other.b
        return self
        
cplx1 = Complex(5, 2)
print(cplx1)
cplx2 = Complex(3, 3)
print(cplx2)
print(cplx1 + cplx2) #8 + 5i
print(cplx1 - cplx2) #2 - 1i
print(cplx1 * cplx2) #9 + 21i
print(cplx1) #5 + 2i
print(cplx2) #3 + 3i
