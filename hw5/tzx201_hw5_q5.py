"""
tzx201_hw5_q5
"""
from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def permutations(lst):
    elems_s = ArrayStack()
    perms_q = ArrayQueue()
    res = []
    for elem in lst:
        elems_s.push(elem)
    length = 0
    while not elems_s.is_empty():
        new_val = elems_s.pop()
        if perms_q.is_empty():
            perms_q.enqueue([new_val])
        else:
            length += 1
            for elem in range(len(perms_q)):
                curr_perm = perms_q.dequeue()
                for i in range(length+1):
                    new_perm = curr_perm[:]
                    new_perm.insert(i, new_val)
                    perms_q.enqueue(new_perm)
    #print(len(perms_q))         
    for elem in range(len(perms_q)):
        res.append(perms_q.dequeue())
    return res

def main():
    lst = [1,2,3]
    perms = permutations(lst)
    print(perms)
    print(len(perms))
    
                
if __name__ == "__main__":
    main()




        
