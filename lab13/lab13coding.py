"""cs1134 lab 13 coding"""
from BinarySearchTreeMap import BinarySearchTreeMap

#1: min_max_BST
def min_max_BST(bst):
    """runs with a worst case runtime of 
    O(n)"""
    if len(bst) == 0:
        raise Exception("BST is empty")
    min_cursor = bst.root
    while min_cursor.right is not None:
        min_cursor = min_cursor.left
    min = min_cursor.item.key
    max_cursor = bst.root
    while max_cursor.right is not None:
        max_cursor = max_cursor.right
    max = max_cursor.item.key
    return (min, max)

def q1_test():
    bst = BinarySearchTreeMap()
    bst[2] = 1
    bst[1] = 1
    bst[3] = 1
    bst[9] = 1
    print(min_max_BST(bst))
#q1_test()

#2: glt_n
def glt_n(bst, n):
    cursor = bst.root
    cur_max = -1
    while cursor is not None:
        val = cursor.item.key
        if val > cur_max and val <= n:
            cur_max = val
        if n == val:
            return n
        elif n < val:
            cursor = cursor.left
        else:
            cursor = cursor.right
    return cur_max

def q2_test():
    bst = BinarySearchTreeMap()
    bst[5] = 1
    bst[2] = 1
    bst[1] = 1
    bst[3] = 1
    bst[12] = 1
    bst[9] = 1
    bst[21] = 1
    bst[19] = 1
    bst[25] = 1
    print(glt_n(bst, 5))
#q2_test()

#3: compare_BST
def compare_BST(bst1, bst2):
    if len(bst1) != len(bst2):
        return False
    set1 = [key for key in bst1]
    set2 = [key for key in bst2]
    return set1 == set2

def q3_test():
    bst = BinarySearchTreeMap()
    bst[15] = 1
    bst[10] = 1
    bst[5] = 1
    bst[12] = 1
    bst[20] = 1
    bst[25] = 1
    bst2 = BinarySearchTreeMap()
    bst2[15] = 1
    bst2[12] = 1
    bst2[5] = 1
    bst2[10] = 1
    bst2[20] = 1
    bst2[25] = 1
    bst2[26] = 1 #true -> false
    print(compare_BST(bst,bst2))
#q3_test()

#4: is_BST
def is_BST(root):
    return is_BST_helper(root)[2]

def is_BST_helper(root):
    if root.left is None and root.right is None:
        val = root.item.key
        return (val, val, True)
    elif root.left is None:
        right_traits = is_BST_helper(root.right)
        right_min = right_traits[0]
        right_max = right_traits[1]
        val = root.item.key
        is_bst = right_traits[2] and (val < right_min)
        return (val, right_max, is_bst)
    elif root.right is None:
        left_traits = is_BST_helper(root.left)
        left_min = left_traits[0]
        left_max = left_traits[1]
        val = root.item.key
        is_bst = left_traits[2] and (val > left_max)
        return(left_min, val, is_BST)
    else:
        right_traits = is_BST_helper(root.right)
        left_traits = is_BST_helper(root.left)
        right_min = right_traits[0]
        right_max = right_traits[1]
        left_min = left_traits[0]
        left_max = left_traits[1]
        val = root.item.key
        is_BST = left_traits[2] and right_traits[2] and (val > left_max) and (val < right_min)
        return (left_min, right_max, is_BST)
    
def q4_test():
    bst = BinarySearchTreeMap()
    bst[5] = 1
    bst[4] = 1
    bst[7] = 1
    print(is_BST_helper(bst.root))
    bst.root.item.key = 2
    print(is_BST_helper(bst.root))




    

q4_test()
    






