"""tzx201_hw8_q3"""

from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    def restore_bst_helper(prefix_lst, start, end):
        if start > end:
            bst = BinarySearchTreeMap()
            return bst
        
        # if start == end:
        #     bst = BinarySearchTreeMap()
        #     val = int(prefix_lst[start])
        #     bst[val] = None
        #     return bst
        
        else:
            bst = BinarySearchTreeMap()
            root = int(prefix_lst[start])
            bst[root] = None
            i = start+1
            # print(i)
            while i <= end and prefix_lst[i] < root:
                i += 1
            # print(root)
            # print(start, end, i)
            left = restore_bst_helper(prefix_lst, start+1, i-1)
            right = restore_bst_helper(prefix_lst, i, end)
            bst.root.left = left.root
            bst.root.right = right.root
            return bst
    bst = restore_bst_helper(prefix_lst, 0, len(prefix_lst)-1)
    bst.n = len(prefix_lst)
    return bst
        
def main():
    lst = [9,7,3,1,5,13,11,15]
    bst = restore_bst(lst)
    print("len", len(bst))
    for i in bst.inorder():
        print(i.item.key, end = " ")
    
if __name__ == "__main__":
    main()





    



