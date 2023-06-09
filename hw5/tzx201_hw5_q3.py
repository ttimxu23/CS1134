"""
tzx201_hw5_q3
"""
from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack():
    def __init__(self):
        self.half1 = ArrayStack()
        self.half2 = ArrayDeque()
        #this might be unnecessary
        #self.n = 0
    def __len__(self):
        return len(self.half1)+ len(self.half2)
    def is_empty(self):
        return len(self) == 0
    def push(self, elem):
        self.half2.enqueue_last(elem)
        if len(self.half2) > len(self.half1):
            to_move = self.half2.dequeue_first()
            self.half1.push(to_move)
    def top(self):
        if not self.half2.is_empty():
            return self.half2.last()
        elif not self.half1.is_empty():
            return self.half1.top()
        else:
            raise Exception("Stack is empty")
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if len(self.half1) > len(self.half2):
            self.half2.enqueue_first(self.half1.pop())
        val = self.half2.dequeue_last()
        return val
    def mid_push(self, elem):
        if len(self.half1) > len(self.half2):
            self.half2.enqueue_first(elem)
        else:
            self.half1.push(elem)
            
def main():
    s = MidStack()
    s.push(2)
    s.push(4)
    s.push(6)
    s.push(8)
    s.push(10)
    s.mid_push(12)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
        
if __name__ == "__main__":
    main()