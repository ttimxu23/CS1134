"""lab 11 coding"""
from LinkedBinaryTree import LinkedBinaryTree
#1: bt_even_sum:
def bt_even_sum(root):
    if root is None:
        return 0
    else:
        left_sum = bt_even_sum(root.left)
        right_sum = bt_even_sum(root.right)
        add = 0
        if root.data%2 == 0:
            add = root.data
        return left_sum + right_sum + add
    
#2: contains: in LinkedBinaryTree file

#3: is_full:
def is_full(root):
    if root is None:
        return True
    else:
        left_full = is_full(root.left)
        right_full = is_full(root.right)
        if root.left is None and root.right is not None:
            return False
        elif root.left is not None and root.right is None:
            return False
        else:
            return left_full and right_full


def main():
    tree = LinkedBinaryTree()
    tree.root = LinkedBinaryTree.Node(1)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.right = LinkedBinaryTree.Node(3)
    print(bt_even_sum(tree.root))
    print(3 in tree) #true
    print(4 in tree) #false
    print(is_full(tree.root)) #true
    tree.root.left.left = LinkedBinaryTree.Node(4)
    print(is_full(tree.root)) #false
    print(4 in tree) #true
main()