"""Invert binary tree
Call invert for left-subtree
Call invert for right-subtree
Swap left and right subtrees
The values of the nodes are swapped in the process and in-order travelsal gives you a decreasing sequence of values.
"""
class BinaryTreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def invert(node):
    if node is None:
        return
    invert(node.left) # recursive call to left subtree: goes back to the top of the function
    invert(node.right) # recursive call to right subtree: goes back to the top of the function
    node.left,node.right=node.right,node.left # actual swapping of left and right subtrees
    return node

def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.data)
    print_tree(node.right)
    
def main():
    root=BinaryTreeNode(10)
    root.left=BinaryTreeNode(5)
    root.right=BinaryTreeNode(15)
    root.left.left=BinaryTreeNode(2)
    root.left.right=BinaryTreeNode(7)
    root.right.left=BinaryTreeNode(12)
    root.right.right=BinaryTreeNode(17)
    print("Inorder traversal of original tree")
    print_tree(root)
    print("Inorder traversal of inverted tree")
    invert(root)
    print_tree(root)
if __name__=='__main__':
    main()