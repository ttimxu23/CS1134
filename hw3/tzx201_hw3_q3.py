"""
tzx201_hw3_q3
"""

def find_duplicates(lst):
    count_nums = [0] * (len(lst))
    for i in range(len(lst)):
        count_nums[lst[i]] += 1
    dups = [i for i in range(len(count_nums)) if count_nums[i] > 1]
    return dups

def main():
    lst=[1,2,3,4,5,6,6,6,6,5]
    print(find_duplicates(lst))