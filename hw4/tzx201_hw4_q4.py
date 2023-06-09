"""
tzx201_hw4_q4
"""

def list_min(lst, low, high):
    if len(lst) == 0:
        return None
    if high > (len(lst)-1) or low < 0:
        raise ValueError("low and/or high parameter invalid")
    if low == high:
        return lst[low]
    else:
        min_rest = list_min(lst, low+1, high)
        if lst[low] < min_rest:
            return lst[low]
        else:
            return min_rest

def main():
    lst = [0]
    print(list_min(lst, 0, len(lst)-1))

