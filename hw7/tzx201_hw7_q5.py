"""tzx201_hw7_q5"""

from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    prefix_exp = prefix_exp_str.split()
    def create_expression_tree_helper(prefix_exp, start_pos):
        operators = "+-*/"
        if start_pos > len(prefix_exp):
            return (None, 0)
        elif prefix_exp[start_pos] in operators:
            root = LinkedBinaryTree.Node(prefix_exp[start_pos])
            left = create_expression_tree_helper(prefix_exp, start_pos + 1)
            right = create_expression_tree_helper(prefix_exp, start_pos + left[1] +1)
            root.left = left[0]
            root.right = right[0]
            return (root, left[1]+right[1]+1)
        else:
            root = LinkedBinaryTree.Node(int(prefix_exp[start_pos]))
            return (root, 1)
        
    tree = LinkedBinaryTree()
    tree.root = create_expression_tree_helper(prefix_exp, 0)[0]
    tree.size = tree.count_nodes()

    return tree

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    list = []
    for node in tree.postorder():
        list.append(str(node.data))
    string = " ".join(list)
    return string

def main():
    pre = "* 2 + - 15 6 4"
    tree = create_expression_tree(pre)
    for elem in tree.inorder():
        print (elem.data, end = " ")
    print("\n")
    print(prefix_to_postfix(pre))

if __name__ == "__main__":
    main()
        
    
        

    
