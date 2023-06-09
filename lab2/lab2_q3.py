# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:32:47 2023

@author: maste
"""

class UnsignedBinaryInteger:
    
    def __init__(self, num_str):
        self.num_str = num_str
       
    def __lt__(self, other):
        if len(self.num_str) > len(other.num_str):
            return False
        elif len(self.num_str) < len(other.num_str):
            return True
        else:
            for i in range(1, len(self.num_str)):
                if int(self.num_str[i]) < int(other.num_str[i]):
                    return True
                if int(self.num_str[i]) > int(other.num_str[i]):
                    return False
        return False    

    def __gt__(self, other):
        if other < self:
            return True
        else: 
            return False
        
    def __eq__(self, other):
        if (other < self) == False and (self < other) == False:
            return True
        else:
            return False
        
    def is_twos_power(self):
        if self.num_str.count("1") == 1:
            return True
        else: 
            return False
        
    def largest_twos_power(self):
        return(2**(len(self.num_str)-1))
    
a = UnsignedBinaryInteger("11000")
b = UnsignedBinaryInteger("1111")
print(a.largest_twos_power())
                        
