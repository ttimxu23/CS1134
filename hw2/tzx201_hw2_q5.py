"""
tzx201_hw2_q5
"""

def split_parity(lst):
    #want odd first
    left = 0
    #want evens last
    right = len(lst) - 1 
    while left < right: 
        #odd alr at left: just move on
        if lst[left]%2 == 1:
            left += 1
        #even alr at right: just move on
        elif lst[right]%2 == 0:
            right -= 1
        else:
            lst[left], lst[right] = lst[right], lst[left]
    return lst

def main():
    lst = [1,7,12,4,8,9,13,9,10,11,0,6]
    print(split_parity(lst))

#main()