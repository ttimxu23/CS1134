"""
tzx201_hw5_q1
"""
from ArrayStack import ArrayStack
def interpreter_postfix_calculator():
    inp = input("--> ")
    variables = {}
    operators = "+-*/"
    while inp != "done()":
        inp_lst = inp.split()
        args_stack = ArrayStack()
        for elem in inp_lst:
            if elem not in operators:
                if elem.isdigit():
                    elem = int(elem)
                args_stack.push(elem)
            else:
                arg2 = args_stack.pop()
                arg1 = args_stack.pop()
                if arg1 in variables.keys():
                    arg1 = variables[arg1]
                if arg2 in variables.keys():
                    arg2 = variables[arg2]    
                if elem == "+":
                    res = arg1 + arg2
                elif elem == "-":
                    res = arg1 - arg2
                elif elem == "*":
                    res = arg1 * arg2
                else:
                    res = arg1 / arg2
                args_stack.push(res)
        num = args_stack.pop()
        if args_stack.is_empty():
            if num in variables.keys():
                num = variables[num]
            print(num)
        else:
            args_stack.pop()
            var_name = args_stack.pop()
            variables[var_name] = num
            print(var_name)
        inp = input("--> ")
                
def main():          
    interpreter_postfix_calculator()

if __name__ == "__main__":
    main()   
            
        

        
