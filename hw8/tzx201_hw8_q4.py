"""tzx201_hw8_q4"""

"""recursive function that returns 3 things
min in subtree max in subtree and the min difference in subtree"""
from BinarySearchTreeMap import BinarySearchTreeMap
# from tzx201_hw8_q3 import restore_bst

def find_min_abs_difference(bst):
    def min_diff_helper(root):
        if root.left is None and root.right is None:
            curr_val = root.item.key
            return (curr_val, curr_val, None)
        elif root.left is None:
            right_min, right_max, r_min_diff = min_diff_helper(root.right)
            curr_val = root.item.key
            if r_min_diff == None or ((right_min - curr_val) < r_min_diff):
                r_min_diff = right_min - curr_val
            return (curr_val, right_max, r_min_diff)
        elif root.right is None:
            left_min, left_max, l_min_diff = min_diff_helper(root.left)
            curr_val = root.item.key
            if l_min_diff == None or ((curr_val - left_max) < l_min_diff):
                l_min_diff = curr_val - left_max
            return (left_min, curr_val, l_min_diff)
        else:
            curr_val = root.item.key
            right_min, right_max, r_min_diff = min_diff_helper(root.right)
            left_min, left_max, l_min_diff = min_diff_helper(root.left)
            if r_min_diff == None or ((right_min - curr_val) < r_min_diff):
                r_min_diff = right_min - curr_val
            if l_min_diff == None or ((curr_val - left_max) < l_min_diff):
                l_min_diff = curr_val - left_max
            min_diff = min(l_min_diff, r_min_diff)
            return (left_min, right_max, min_diff)
    if bst.is_empty():
        raise Exception("Binary Search Tree Map is empty")
    bst_min, bst_max, min_diff = min_diff_helper(bst.root)
    return min_diff

# def main():
#     lst = [9,7,3,1,6,13,11,15]
#     bst = restore_bst(lst)
#     print(find_min_abs_difference(bst))

# if __name__ == "__main__":
#     main()
