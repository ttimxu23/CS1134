"""
tzx201_hw4_q3
"""

def print_triangle(n):
    if type(n) != int:
        raise TypeError("please provide a positive integer")
    if n < 1:
        raise ValueError("please provide a positive integer")
    if n == 1:
        print("*")
    else:
        print_triangle(n-1)
        print("*"*n)
        
def print_opposite_triangles(n):
    if type(n) != int:
        raise TypeError("please provide a positive integer")
    if n < 1:
        raise ValueError("please provide a positive integer")
    if n == 1:
        print("*")
        print("*")
    else:
        print("*"*n)
        print_opposite_triangles(n-1)
        print("*"*n)
        
def print_ruler(n):
    if type(n) != int:
        raise TypeError("please provide a positive integer")
    if n < 1:
        raise ValueError("please provide a positive integer")
    if n == 1:
        print("-")
    else:
        print_ruler(n-1)
        print("-"*(n))
        print_ruler(n-1)
        



