"""
Lab 8 Code
"""
from ArrayStack import *

s=ArrayStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

#1
def stack_sum(s):
    if s.is_empty():
        return 0
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        sum_rest = stack_sum(s)
        
        new_sum = sum_rest + val
        s.push(val)
        return new_sum
#print(stack_sum(s))
#print(s.top())

#2
def eval_prefix(exp_str):
    operators = "+-*/"
    exp_lst = exp_str.split()
    s = ArrayStack()
    for i in range(len(exp_lst)-1,-1,-1):
        if exp_lst[i] not in operators:
            s.push(int(exp_lst[i]))
        else:
            val1 = s.pop()
            val2 = s.pop()
        #+
            if exp_lst[i] == "+":
                new_val = val1 + val2
        #-
            elif exp_lst[i] == "-":
                new_val = val1 - val2

        #*
            elif exp_lst[i] == "*":
                new_val = val1 * val2
        #/
            else:
                new_val = val1 / val2
            s.push(new_val)

    return int(s.pop())
#print(eval_prefix("- + * 16 5 * 8 4 20"))
#print(eval_prefix("- + * 8 2 4 + 3 6"))
#print(eval_prefix("+ * 5 5 / 10 2"))

#3
def flatten_list(lst):
    s = ArrayStack()
    for i in range(len(lst)-1, -1, -1):
            s.push(lst.pop())
    while s.is_empty() == False:
        val = s.pop()
        if type(val) == int:
            lst.append(val)
        else:
            new_lst = val
            for i in range(len(new_lst)-1, -1, -1):
                s.push(new_lst[i])
#lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
#flatten_list(lst)
#print(lst)
            
                
            