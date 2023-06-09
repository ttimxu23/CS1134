"""tzx201_hw7_q3"""

from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):
     def subtree_node_heights(root):
        if root.left is None and root.right is None:
            return (0,0, True)
        elif root.left is None:
            right_heights = subtree_node_heights(root.right)
            right_height = max(right_heights[0], right_heights[1]) + 1
            if right_height > 1 or right_heights[2] == False:
                balance = False
            else:
                 balance = True
            return (0, right_height, balance)
        elif root.right is None:
            left_heights = subtree_node_heights(root.left)
            left_height = max(left_heights[0], left_heights[1]) + 1
            if left_height > 1 or left_heights[2] == False:
                balance = False
            else: 
                balance = True
            return (left_height, 0, balance)
        else:
            right_heights = subtree_node_heights(root.right)
            left_heights = subtree_node_heights(root.left)
            right_height = max(right_heights[0], right_heights[1]) + 1
            left_height = max(left_heights[0], left_heights[1]) + 1
            if abs(right_height - left_height) > 1 or right_heights[2] == False or left_heights[2] == False:
                balance = False
            else:
                balance = True
            return (left_height, right_height, balance)
     if bin_tree.root is None:
         return True
     return subtree_node_heights(bin_tree.root)[2]
     
    



def main():
    tree = LinkedBinaryTree()
    # tree.root = LinkedBinaryTree.Node(3)
    # tree.root.left = LinkedBinaryTree.Node(2)
    # tree.root.right = LinkedBinaryTree.Node(7)
    # tree.root.left.left = LinkedBinaryTree.Node(9)
    # # tree.root.left.right = LinkedBinaryTree.Node("Placeholder")
    # tree.root.left.left.left = LinkedBinaryTree.Node(5)
    # tree.root.left.left.right = LinkedBinaryTree.Node(1)
    # tree.root.right.left = LinkedBinaryTree.Node(8)
    # tree.root.right.right = LinkedBinaryTree.Node(4)
    print(is_height_balanced(tree))


if __name__ == "__main__":
     main()