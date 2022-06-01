"""Binary Tree implementation.
Usually used for binary search trees.
Inorder, Preorder, Postorder traversal.
Inorder travelsal: left, root, right. It is the most common way to traverse a binary tree.
Inorder traversal retuns a non-decreasing order.
"""
import random
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data==self.data:
            return 1
        if data<self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add_child(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add_child(data)
    def inorder(self):
        """Returns a list of nodes in the tree in order."""
        elements=[]
        # visit left tree
        if self.left:
            elements += self.left.inorder()
        # visit root
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.inorder()
        return elements
def build_tree(elements):
    """Builds a binary tree from a list of elements."""
    root=Node(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root
def main():
    elements=[random.randint(0,100) for i in range(10)]
    print(elements)
    tree=build_tree(elements)
    print(tree.inorder())
if __name__ == '__main__':
    main()
