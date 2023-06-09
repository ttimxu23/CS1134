
from LinkedBinaryTree import LinkedBinaryTree


def q2_test():
    tree = LinkedBinaryTree()
    tree.root = LinkedBinaryTree.Node(3)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.right = LinkedBinaryTree.Node(7)
    tree.root.left.left = LinkedBinaryTree.Node(9)
    tree.root.left.left.left = LinkedBinaryTree.Node(5)
    tree.root.left.left.right = LinkedBinaryTree.Node(1)
    tree.root.right.left = LinkedBinaryTree.Node(8)
    tree.root.right.right = LinkedBinaryTree.Node(4)
    print(tree.leaves_list())


q2_test()
