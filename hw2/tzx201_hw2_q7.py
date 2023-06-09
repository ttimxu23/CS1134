"""
tzx_hw2_q7
"""

def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    #if only zeroes, returns none to prevent index out of range
    if lst01[-1] == 0:
        return None
    #cannot have change if the lst is either 0 or 1 elems
    if len(lst01) <= 1:
        return None
    while left <= right:
        mid = (left+right)//2
        if lst01[mid] == 0 and lst01[mid+1] == 1:
            return mid+1
        elif lst01[mid] == 1 and lst01[mid+1] == 1:
            right = mid - 1
        else:
            left = mid +1
    return None

def main():
    lst01 = [0,0,0,0,0,0,0,1]
    print(findChange(lst01))

#main()