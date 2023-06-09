# -*- coding: utf-8 -*-
"""
QueueStack
"""
from ArrayQueue import *
class QueueStack1: #optimizes push
    def __init__(self):
        self.data = ArrayQueue()
        self.n = 0
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def push(self, elem):
        self.data.enqueue(elem)
        self.n += 1
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        for i in range(self.n - 1):
            curr = self.data.dequeue()
            self.data.enqueue(curr)
        val = self.data.dequeue()
        self.n -= 1
        return val
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        val = self.pop()
        self.data.enqueue(val)
        return val
    
class QueueStack2: #optimizes pop
    def __init__(self):
        self.data = ArrayQueue()
        self.n = 0
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.dequeue()
    def push(self, elem):
        self.data.enqueue(elem)
        for i in range(len(self) - 1):
            self.data.enqueue(self.data.dequeue())
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.first()
        
  
def main1():    
    q = QueueStack1()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.top())
        
#main1()

def main2():    
    q = QueueStack2()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.top())
    
main2()
    
