"""
tzx201_hw4_q5
"""
#a
def count_lowercase(s, low, high):
    if len(s) == 0:
        return 0
    if high > (len(s)-1) or low < 0:
        raise ValueError("low and/or high parameter invalid")
    if low == high:
        if s[high].islower():
            return 1
        else:
            return 0
    else:
        count_rest = count_lowercase(s, low+1, high)
        if s[low].islower():
            return count_rest + 1
        else:
            return count_rest
def main1():    
    s = "l"
    print(count_lowercase(s, 4, len(s)-1))

#b
def is_number_of_lowercase_even(s, low, high):
    if len(s) == 0:
        return True
    if high > (len(s)-1) or low < 0:
        raise ValueError("low and/or high parameter invalid")
    if low == high:
        if s[high].islower():
            return False
        else:
            return True
    else:
        rest_even = is_number_of_lowercase_even(s, low+1, high)
        if s[low].islower():
            return not rest_even
        else:
            return rest_even

def main2():
    s = "!a!aH"
    print(is_number_of_lowercase_even(s, 0, len(s)-1))