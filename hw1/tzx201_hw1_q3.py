"""
tzx201_hw1_q3
"""

#a
def sum_squares(n):
    output = 0
    for i in range(1, n):
        output += i**2
    return output


#b
def sum_squares2(n):
    total = sum([i**2 for i in range(1, n)])
    return total

#c
def sum_odd_squares(n):
    output = 0
    for i in range(1, n):
        if i%2 == 1:
            output += i**2
    return output

#d
def sum_odd_squares2(n):
    total = sum([i**2 for i in range(1,n) if i%2 == 1])
    return total

def main():
    print(sum_squares(5))
    print(sum_squares2(5))
    print(sum_odd_squares(5))
    print(sum_odd_squares2(5))


