# -*- coding: utf-8 -*-
"""
ArrayDeque
"""
import ctypes
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    initial_cap = 8 
    def __init__(self):
        self.data = make_array(ArrayDeque.initial_cap)
        self.capacity = ArrayDeque.initial_cap
        self.n = 0
        self.front_ind = None
        self.back_ind = None
    def __len__(self):
        return self.n
    def is_empty(self):
        return len(self) == 0
    def first(self):
        if self.is_empty():
            return Exception("Queue is empty")
        return self.data[self.front_ind]
    def last(self):
        if self.is_empty():
            return Exception("Queue is empty")
        return self.data[self.back_ind]
    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data = new_data
        self.capacity = new_cap
        self.front_ind = 0
        self.back_ind = self.n - 1
    def enqueue_first(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.n += 1
        else:
            self.front_ind  = (self.front_ind - 1 + self.capacity) % self.capacity
            self.data[self.front_ind] = elem
            self.n += 1
    def enqueue_last(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.n += 1
        else:
            self.back_ind = (self.back_ind + 1) % self.capacity
            self.data[self.back_ind] = elem
            self.n += 1
    def dequeue_first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        val = self.first()
        self.data[self.front_ind] = None
        self.n -= 1 
        if self.is_empty():
            self.front_ind = None
            self.back_ind = None
        else:
            self.front_ind = (self.front_ind + 1) % self.capacity
        if self.n < (self.capacity // 4):
            self.resize(self.capacity // 2)
        return val
    def dequeue_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        val = self.last()
        self.data[self.back_ind] = None
        self.n -= 1
        if self.is_empty():
            self.front_ind = None
            self.back_ind = None
        else:
            self.back_ind = (self.back_ind - 1 + self.capacity) % self.capacity
        if self.n < (self.capacity // 4):
            self.resize(self.capacity // 2)
        return val
            

            
            
def main():
    q = ArrayDeque()
    q.enqueue_first(2)
    q.enqueue_first(1)
    q.enqueue_last(3)
    print(q.dequeue_first()) # should be 1
    print(q.first()) #should be 2
    print(q.last()) #should be 3
    #Queue is: 2 3
    q.enqueue_last(4)
    q.enqueue_first(1)
    q.enqueue_last(5)
    q.dequeue_first()
    q.dequeue_last()
    #first and last should be 2 and 4
    print(q.first())
    print(q.last())
    
main()

        
