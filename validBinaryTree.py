"""Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST)."""
class BinaryTreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def add_child(self,data):
        if data==self.data:
            return False
        if data<self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
                return True
        else:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)
                return True
def isvalidBST(root):
    return isvalidBST_helper(root,float("-inf"),float("inf"))
def isvalidBST_helper(root,min_val,max_val):
    if root is None:
        return True
    if root.data<=min_val or root.data>=max_val:
        return False
    # recursive call to left and right subtrees
    # left subtree node must be smaller than root: root is max_val here
    # right subtree node must be greater than root: root is min_val here
    return isvalidBST_helper(root.left,min_val,root.data) and isvalidBST_helper(root.right,root.data,max_val)
def main():
    root=BinaryTreeNode(2)
    root.add_child(2)
    root.add_child(2)
    print(isvalidBST(root))
if __name__=="__main__":
    main()