"""
tzx201_hw4_q6
"""

def appearances(s, low, high):
    if len(s) == 0:
        return {}
    if high > (len(s)-1) or low < 0:
        raise ValueError("low and/or high parameter invalid")
    if low == high:
        return {s[high]: 1}
    else:
        appear_rest = appearances(s, low+1, high)
        if s[low] in appear_rest:
            appear_rest[s[low]] += 1
        else:
            appear_rest[s[low]] = 1
        return appear_rest
    
#print(appearances("Hello world", 0, 10))