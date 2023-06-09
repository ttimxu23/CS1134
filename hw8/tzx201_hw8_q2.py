"""tzx201_hw8_q2"""

from BinarySearchTreeMap import BinarySearchTreeMap

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for num in range(1, n+1):
        bst.insert(num, None)
    return bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low == high:
        bst.insert(low, None)
    else:
        val = (low+high)//2
        #print(low, val, high)
        bst.insert(val, None)
        add_items(bst, low, val-1)
        add_items(bst, val+1, high)

def main():
    bst = create_complete_bst(7)
    for node in bst.inorder():
        print(node.item.key, end = " ")

if __name__ == "__main__":
    main()