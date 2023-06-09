"""final review all the optional problems on all the labs"""

from BinarySearchTreeMap import BinarySearchTreeMap
from LinkedBinaryTree import LinkedBinaryTree
def lca_BT(bt, node1, node2):
    if bt.root == node1 or bt.root == node2:
        return bt.root
    else:
        subtree_l = LinkedBinaryTree()
        #FUCK I'LL DO THIS LATER
        #idk just do recursion

def merge_bt(root1, root2):
    if root1 is not None and root2 is not None:
        num = root1.data + root2.data
        node = LinkedBinaryTree.Node(num)
        node.left = merge_bt(root1.left, root2.left)
        node.right = merge_bt(root1.right, root2.right)
        return node
    elif root1 is not None:
        num = root1.data
        node = LinkedBinaryTree.Node(num)
        node.left = merge_bt()
        pass