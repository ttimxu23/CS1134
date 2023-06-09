"""
tzx201_hw4_q7
"""

def split_by_sign(lst, low, high):
    if len(lst) == 0:
        return 
    if high > (len(lst)-1) or low < 0:
        raise ValueError("low and/or high parameter invalid")
    if low == high:
        return
    else:
        if lst[low] > 0:
            lst[low], lst[high] = lst[high], lst[low]
            split_by_sign(lst, low, high-1)
        else:
            split_by_sign(lst, low+1, high)

def main():
    lst = [10,-3,4,-5,-6,12,6,-5,-5,112,9]
    split_by_sign(lst, 0, len(lst)-1)
    print(lst)