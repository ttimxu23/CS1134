"""
tzx201_hw5_q4
"""
from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.enqueue_stack = ArrayStack()
        self.dequeue_stack = ArrayStack()
        self.n = 0
    def __len__(self):
        return self.n
    def is_empty(self):
        return self.n == 0
    def enqueue(self, elem):
        self.enqueue_stack.push(elem)
        self.n += 1
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.n -= 1
        if not self.dequeue_stack.is_empty():
            val = self.dequeue_stack.pop()
        else:
            for elem in range(len(self.enqueue_stack)):
                self.dequeue_stack.push(self.enqueue_stack.pop())
            val = self.dequeue_stack.pop()
        return val
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if not self.dequeue_stack.is_empty():
            val = self.dequeue_stack.top()
        else:
            for elem in range(len(self.enqueue_stack)):
                self.dequeue_stack.push(self.enqueue_stack.pop())
            val = self.dequeue_stack.top()
        return val
    
def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue()) #should be 1
    print(q.first()) #should be 2
    q.enqueue(4)
    q.enqueue(5)
    print(len(q)) #4
    print(q.dequeue()) #2
    print(q.dequeue()) #3
    print(q.first()) #4
    print(q.dequeue())
    print(len(q)) #1

if __name__ == "__main__":
    main()
