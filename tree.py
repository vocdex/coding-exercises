
import random
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data==self.data:
            return False
        if data<self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BSTNode(data)
                return True
        else:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BSTNode(data)
                return True
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def inorder(self):
        # Left->Root->Right
        elements=[]
        if self.left:
            elements+=self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder()
        return elements
    def preorder(self):
        # Root->Left->Right
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.preorder()
        if self.right:
            elements+=self.right.preorder()
        return elements
    def postorder(self):
        # Left->Right->Root
        elements=[]
        if self.left:
            elements+=self.left.postorder()
        if self.right:
            elements+=self.right.postorder()
        elements.append(self.data)
        return elements
def build_tree(elements):
    root = BSTNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
def main():
    elements=random.sample(range(100),10)
    countries=['India','USA','China','Russia','Japan','Germany','France','Italy','UK','Canada']
    country_tree=build_tree(countries)
    print("Check if a country is present in the tree:")
    for i in countries:
        print(i,":",country_tree.search(i))
    print("Inorder traversal of the tree:")
    print(country_tree.inorder())
    print("Preorder traversal of the tree:")
    print(country_tree.preorder())
    print("Postorder traversal of the tree:")
    print(country_tree.postorder())
if __name__=="__main__":
    main()
