"""
tzx201_hw1_q2
"""

def shift(lst, k, direction = "left"):
    k = k%len(lst)
    direction = direction.lower()
    if direction == "left":
        for i in range(len(lst)-k):
            (lst[i], lst[i+k]) = (lst[i+k], lst[i])
    elif direction == "right":
        for i in range(0,-(len(lst)-k),-1):
            (lst[i], lst[i-k]) = (lst[i-k], lst[i])
    else:
        raise ValueError("please enter a valid direction")
    
def main():
    lst = [1,2,3,4,5]
    shift(lst, 1, "ah")
    print(lst)





