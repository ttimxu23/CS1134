# -*- coding: utf-8 -*-
"""
MeanQueue
"""
from ArrayQueue import *
class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.sum = 0
        self.n = 0
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def enqueue(self, item):
        if type(item) != float and type(item) != int:
            raise TypeError("Only able to enqueue integers or floats")
        self.data.enqueue(item)
        self.n += 1
        self.sum += item
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        val = self.data.dequeue()
        self.sum -= val
        self.n -= 1
        return val
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.first()
    def sum(self):
        return self.sum
    def mean(self):
        if self.is_empty():
            return ValueError("Queue is empty")
        return self.sum / self.n

def main():    
    q = MeanQueue()
    q.enqueue(1)
    q.enqueue(9)
    print(q.sum)
    print(q.mean())




    
