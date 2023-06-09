"""cs1134 lab 12 coding"""
from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack

#1: Iterative Preorder LinkedBinaryTree Method
def q1_test():
    tree = LinkedBinaryTree()
    tree.root = LinkedBinaryTree.Node(3)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.right = LinkedBinaryTree.Node(7)
    tree.root.left.left = LinkedBinaryTree.Node(9)
    tree.root.left.left.left = LinkedBinaryTree.Node(5)
    tree.root.left.left.right = LinkedBinaryTree.Node(1)
    tree.root.right.left = LinkedBinaryTree.Node(8)
    tree.root.right.right = LinkedBinaryTree.Node(4)
    print([num for num in tree.preorder_with_stack()])

#q1_test()

#2: is_perfect
#these def might be wrong potentially a number of cases where they don't work
def is_perfect_recursive(root):
    if root.left is None and root.right is None:
        return (1, 0, True)
    elif root.left is None:
        right = is_perfect_recursive(root.right)
        return (right[0]+1, right[1]+1, False)
    elif root.right is None:
        left = is_perfect_recursive(root.left)
        return (left[0]+1, left[1]+1, False)
    else:
        left = is_perfect_recursive(root.left)
        right = is_perfect_recursive(root.right)
        num_nodes = left[0] + right[0] + 1
        depth = max(left[1], right[1]) + 1
        num = 0
        for i in range(depth+1):
            num += 2**i
        perf = (num == num_nodes) and left[2] and right[2]
        return (num_nodes, depth, perf)
    
def is_perfect_iterative(root):
    bfs_q = ArrayQueue()
    bfs_q.enqueue(root)
    #num_nodes = 0
    while not bfs_q.is_empty():
        curr_node = bfs_q.dequeue()
        added = 0
        if curr_node.left is not None:
            bfs_q.enqueue(curr_node.left)
            added += 1
        if curr_node.right is not None:
            bfs_q.enqueue(curr_node.right)
            added += 1
        if added == 1:
            return False
    return True

def q2_test():
    tree = LinkedBinaryTree
    tree.root = LinkedBinaryTree.Node(1)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.right = LinkedBinaryTree.Node(3)
    tree.root.left.left = LinkedBinaryTree.Node(4)
    tree.root.left.right = LinkedBinaryTree.Node(5)
    tree.root.right.left = LinkedBinaryTree.Node(6)
    tree.root.right.right = LinkedBinaryTree.Node(7)
    print(is_perfect_iterative(tree.root))

#q2_test()

#3: invert_bt
def invert_bt_recursive(root):
    if root is None:
        return 
    else:
        root.left, root.right = root.right, root.left
        invert_bt_recursive(root.right)
        invert_bt_recursive(root.left)

def invert_bt_iterative(root):
    s = ArrayStack()
    s.push(root)
    while not s.is_empty():
        node = s.pop()
        node.left, node.right = node.right, node.left
        if node.right is not None:
            s.push(node.right)
        if node.left is not None:
            s.push(node.left)

def q3_test():
    tree = LinkedBinaryTree()
    tree.root = LinkedBinaryTree.Node(1)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.right = LinkedBinaryTree.Node(3)
    tree.root.left.left = LinkedBinaryTree.Node(4)
    tree.root.left.right = LinkedBinaryTree.Node(5)
    tree.root.right.left = LinkedBinaryTree.Node(6)
    tree.root.right.right = LinkedBinaryTree.Node(7)
    print([num.data for num in tree.inorder()])
    #invert_bt_recursive(tree.root)
    invert_bt_iterative(tree.root)
    print([num.data for num in tree.inorder()])

#q3_test()

#4: merge_bt
def merge_bt(root1, root2):
    def helper(root1, root2):
        if root1 is not None and root2 is not None:
            node = LinkedBinaryTree.Node(root1.data + root2.data)
            node.left = helper(root1.left, root2.left)
            node.right = helper(root1.right, root2.right)
            return node
        elif root1 is not None:
            node = LinkedBinaryTree.Node(root1.data)
            node.left = helper(root1.left, None)
            node.left = helper(root1.right, None)
            return node
        elif root2 is not None:
            node = LinkedBinaryTree.Node(root2.data)
            node.left = helper(None, root2.left)
            node.right = helper(None, root2.right)
            return node
        else:
            return None
    return helper(root1, root2)

def q4_test():
    tree = LinkedBinaryTree()
    tree.root = LinkedBinaryTree.Node(1)
    tree.root.left = LinkedBinaryTree.Node(2)
    tree.root.right = LinkedBinaryTree.Node(3)
    tree1 = LinkedBinaryTree()
    tree1.root = LinkedBinaryTree.Node(1)
    tree1.root.left = LinkedBinaryTree.Node(2)
    tree1.root.right = LinkedBinaryTree.Node(3)
    tree2 = merge_bt(tree1.root, tree.root).data
    for i in tree2.inorder():
        print(i.data)
    #fix this

q4_test()

