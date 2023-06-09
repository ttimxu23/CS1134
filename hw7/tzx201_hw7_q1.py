"""tzx201_hw7_q1"""

from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise Exception("Tree is empty")
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            val = root.data
            return (val, val)
        elif root.left is None:
            right_minmax = subtree_min_and_max(root.right)
            if root.data > right_minmax[1]:
                return (right_minmax[0], root.data)
            elif root.data < right_minmax[0]:
                return (root.data, right_minmax[1])
            else:
                return right_minmax
        elif root.right is None:
            left_minmax = subtree_min_and_max(root.left)
            if root.data > left_minmax[1]:
                return (left_minmax[0], root.data)
            elif root.data < left_minmax[0]:
                return (root.data, left_minmax[1])
            else:
                return left_minmax
        else:
            right_minmax = subtree_min_and_max(root.right)
            left_minmax = subtree_min_and_max(root.left)
            minimum = min(right_minmax[0], left_minmax[0])
            maximum = max(right_minmax[1], left_minmax[1])
            if root.data > maximum:
                return (minimum, root.data)
            elif root.data < minimum:
                return (root.data, maximum)
            else:
                return (minimum, maximum)
    if bin_tree.root is None:
        raise Exception("Tree is empty. No min or max")
    return subtree_min_and_max(bin_tree.root)

def main():
    tree = LinkedBinaryTree()
    tree.root = LinkedBinaryTree.Node(3)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.right = LinkedBinaryTree.Node(7)
    tree.root.left.left = LinkedBinaryTree.Node(9)
    tree.root.left.left.left = LinkedBinaryTree.Node(5)
    tree.root.left.left.right = LinkedBinaryTree.Node(1)
    tree.root.right.left = LinkedBinaryTree.Node(8)
    tree.root.right.right = LinkedBinaryTree.Node(4)
    print(min_and_max(tree))

if __name__ == "__main__":
    main()
        