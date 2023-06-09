import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

from ArrayList import ArrayList


class StaticArrayStack:
    def __init__(self, max_capacity):
        self.data = make_array(max_capacity)
        self.capacity = max_capacity 
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (len(self) == self.capacity)

    def push(self, item):
        if(self.is_full()):
            raise Exception("Stack is full")
        self.data[self.n] = item
        self.n += 1

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        item = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1
        return item

    def top(self):
        if(self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[self.n - 1]



class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()




def print_in_reverse(str):
    S = ArrayStack()

    for ch in str:
        S.push(ch)

    while (S.is_empty() == False):
        ch = S.pop()
        print(ch, end='')
    print()



def eval_postfix_exp(exp_str):
    operators = "+-*/"
    exp_lst = exp_str.split()
    args_stack = ArrayStack()
    for token in exp_lst:
        if(token not in operators):
            args_stack.push(int(token))
        else:
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if(token == '+'):
                res = arg1 + arg2
            elif (token == '-'):
                res = arg1 - arg2
            elif(token == '*'):
                res = arg1 * arg2
            elif(token == '/'):
                if(arg2 == 0):
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()

