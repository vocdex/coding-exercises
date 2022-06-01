#linkedlist is a collection of nodes that collectively form a linear sequence
"""each node stores a reference to an object that is an element of the sequence
and a reference to the next node of the list
The first node is called head.
The last node is called tail.
The tail has None as its next reference.
No fixed size, contrary to list/array(static)
Inserting object at the head
Create a new node, set its element to the new element, set its link to refer to the current head. Set the list's head to point to the new node"""
"""Unsorted linked list"""
"""
class Node:
    #Creating a node
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    # Insert at the beginning
    def insertAtBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    # Insert after
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must be in LinkedList")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    # Insert at the end
    def insertAtEnd(self,new_data):
        new_node=Node(new_data)
        if self.head is None: # if empty, the new node is the first node
            self.head=new_node
            return
        last=self.head #traverse the llist to the last node and replace it with the new_node
        while(last.next):
            last=last.next
        last.next=new_node
    def deleteNode(self,position):
        if self.head is None:
            return
        temp=self.head
        if position==0:
            self.head=temp.next
            temp=None
            return
        #Find the key to be deleted
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
    #Search an element
    def search(self,key):
        current=self.head
        while current is not None:
            if current.data==key:
                return True
            current=current.next
        return False
    # Sort the linked list
    def sortLinkedList(self,head):
        current=head
        index=Node(None)
        if head is None:
            return
        else:
            while current is not None:
                index=current.next
            while index is not None:
                if current.data>index.data:
                    current.data,index.data=index.data,current.data
                index=index.next
            current=current.next
    def printList(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" ",end=" ")
            temp=temp.next
"""
class Node:
    __slots__ = ('value','next')
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0
    def insert(self,value): #insert at the end
        node=Node(value)
        if not self.tail: # if empty
            self.head=self.tail=node
        else: # if not empty, point previous tail node's pointer to new node. Update previous pointer's node to new node
            self.tail.next=node
            self.tail=node
        self.len+=1
    def remove(self,value):
        node,prev,found=self.find_value(self.head,None,value)
        if not node:
            raise ValueError()
        if prev:
            prev.next=node.next
        else: #remove the head
            self.head=node.next
        if not node.next:
            self.tail=prev
        self.len-=1
    def __contains__(self, item,value):
        _,_,found=self.find_value(self.head,None,value)
        return found
    def __len__(self):
        return self.len
    def __iter__(self):
        yield from self._iter(self.head)
    def _iter(self,node):
        if node:
            yield node.value
            yield from self._iter(node.next)
    def find_value(self,curr,prev,value):
        while curr:
            if curr.value==value:
                return curr,prev,True
            prev=curr
            curr=curr.next
        return curr,prev,False
ll=LinkedList()
values=[2,3,4,5,6]
for value in values:
    ll.insert(value)
    print (list(ll))
    print(len(ll))
for value in values:
    ll.remove(value)
    print(list(ll))
    print(len(ll))