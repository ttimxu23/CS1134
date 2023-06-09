"""
tzx201_hw4_q8
"""

def flat_list(nested_lst, low, high):
    if len(nested_lst) == 0:
        return []
    if high > (len(nested_lst)-1) or low < 0:
        raise ValueError("low and/or high parameter invalid")
    if low == high:
        if type(nested_lst[low]) == int:
            return [nested_lst[low]]
        else:
            return flat_list(nested_lst[low], 0, len(nested_lst[low])-1)
    else:
        flat_rest = flat_list(nested_lst, low, high-1)
        if type(nested_lst[high]) == int:
            return flat_rest + [nested_lst[high]]
        else:
            return flat_rest + flat_list(nested_lst[high], 0, len(nested_lst[high])-1)
       





def main():
    lst=[[1, 2], 3, [4, [5, 6, [7], 8]]]
    l = len(lst)-1
    print(flat_list(lst, 0, l))
