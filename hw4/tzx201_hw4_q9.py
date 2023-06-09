"""
tzx201_hw4_q9
"""

def permutations(lst, low, high):
    if low == high:
        return [[lst[high]]]
    else:
        perm_rest = permutations(lst, low, high-1)
        new_perm = []
        for elem in perm_rest:
            for i in range(high-low+1):
                to_add = elem[:]
                to_add.insert(i, lst[high])
                new_perm.append(to_add)
        return new_perm
        
        
def main():      
    lst = [1,2,3,4]
    print(permutations(lst, 0, 2))
