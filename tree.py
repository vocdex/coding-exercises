
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
        elemets=[]
        if self.left:
            elemets+=self.left.inorder()
        elemets.append(self.data)
        if self.right:
            elemets+=self.right.inorder()
        return elemets
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
if __name__=="__main__":
    main()
