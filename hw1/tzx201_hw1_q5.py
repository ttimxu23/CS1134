"""
tzx201_hw1_q5
"""


def fibs(n):
    cur = 0
    add = 1
    if n > 0:
        yield 1
    for i in range(n-1):
        tot = cur + add
        cur = add
        add = tot
        yield tot
def main():
    for curr in fibs(3):
        print(curr, end = " ")


