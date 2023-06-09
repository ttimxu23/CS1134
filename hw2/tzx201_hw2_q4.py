# -*- coding: utf-8 -*-
"""
tzx201_hw2_h4
"""

def e_approx(n):
    denom = 1
    e = 1
    for i in range(n):
        e += 1 /((denom) * (i+1))
        denom *= (i+1)
    return e
    
def main():
    for n in range(12):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

#main()