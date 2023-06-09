# -*- coding: utf-8 -*-
"""
tzx201_hw3_q2
"""

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iter_collection = None):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0
        if iter_collection != None:
            self.extend(iter_collection)

    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val


    def __repr__(self):
        data_as_strings = [str(self.data[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'


    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times
    
    def remove(self, val):
        for i in range(len(self)):
            if self.data[i] == val:
                self.data[i] = None
                self.n -= 1
                for j in range(i, self.n-1):
                    self.data[j] = self.data[j+1]
                break
        raise ValueError("given value not found")
    
    #removeAll method
    def removeAll(self, val):
        removed = 0
        to_move = 0
        for i in range(self.n):
            if self.data[i] == val:
                removed += 1
                to_move = i
            else:
                self.data[to_move] = self.data[i]   
        #if removed == 0:
            #raise ValueError("value not found")
        self.n -= removed

        
                
    #a: insert method
    def insert(self, index, val):
        if (not (-self.n <= index <= self.n - 1)):
            raise IndexError('invalid index')
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        if index < 0:
            index = self.n + index
        #making room for the inserted item
        for i in range(self.n, index, -1):
            self.data[i] = self.data[i-1] 
        self.n += 1
        self.data[index] = val
        
    #b: pop method
    def pop(self, index = -1):
        if self.n == 0:
            raise IndexError("The list is empty")
        if (not (-self.n <= index <= self.n - 1)):
            raise IndexError('invalid index')
        if index == -1:
            ret = self.data[self.n-1]
            self.data[self.n-1] = None
        else:
            if index < 0:
                index += self.n
            ret = self.data[index]
            self.data[index] = None
            for i in range(index, self.n-1):
                self.data[i] = self.data[i+1]
        self.n -= 1
        if self.n < self.capacity//4:
            self.resize(self.capacity//2)
        return ret
            
"""
C:
    
    1. the total cost of the n append operations is as follows:
        n(cost of all n appends) + (1 + 2 + 4 + 8 + ... + n)(cost of all resize operations)
            = n + (2n + 1) = 2n + 1
        the total cost of the n pop operations is as follows:
        n(cost of all n pops) + (n/2 + n/4 + n/8 + ... + 1)(cost of all resize operations)
            = n + (n - 1) = 2n - 1
        sum of all append and pop operations:
            4n, which is O(n)
        
    2. 



"""
    
def removeAlltest():      
    arr = ArrayList([1,2,3,2,3,4,2,2])
    print(arr)
    arr.removeAll(2)
    print(arr)     
    
def inserttest():    
    arr_lst = ArrayList()
    for i in range(1, 4+1):
        arr_lst.append(i)
    print(arr_lst)
    arr_lst.insert(2, 30)
    print(arr_lst)
    
def poptest():  
    arr_lst = ArrayList()
    for i in range(1, 5+1):
        arr_lst.append(i)
    print(arr_lst)
    print(arr_lst.pop(2))
    print(arr_lst)
    
    
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        

