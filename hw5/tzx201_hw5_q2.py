"""
tzx201_hw5_q2
"""
from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.n = 0
        self.max = None
    def __len__(self):
        return self.n
    def is_empty(self):
        return len(self) == 0
    def push(self, elem):
        #assumes that elem is a number
        self.n += 1
        self.data.push((elem, self.max))
        if self.max == None or elem > self.max:
            self.max = elem
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[0]
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        val = self.data.pop()
        if val[0] == self.max:
            self.max = val[1]
        return val[0]
    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.max
        
def main():
    s = MaxStack()
    s.push(3)
    s.push(1)
    s.push(6)
    s.push(4)
    print(s.max)
    print(s.pop())
    print(s.pop())
    print(s.max)

if __name__ == "__main__":
    main()