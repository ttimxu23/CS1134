# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:36:27 2023

@author: maste
"""

class Student:
    def __init__(self, name = "student", age = 18):
        self.name = name
        self.age = age
        
peter = Student(16)
print(peter.name, peter.age)
peter = Student("Peter Parker")
print(peter.name, peter.age)
peter = Student(age = 16)
print(peter.name, peter.age)
print(' , '.join([]))
print("a")

a = "aah"
b = "bahh"
a, b = b, a
print(a,b)