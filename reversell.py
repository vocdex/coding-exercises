"""Reverse a linked list. Stack using list is slow. Use pointers approach"""
import time


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def reverse_stack(head):
    if head is None or head.next is None:
        return head
    stack=ListNode(head.val)
    head=head.next
    while head is not None:
        temp=ListNode(head.val)
        temp.next=stack
        stack=temp
        head=head.next
    return stack


def reverse_replace(head):
    prev=None
    while head is not None:
        temp=head.next
        head.next=prev
        prev=head
        head=temp
    return prev

def main():
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    head.next.next.next=ListNode(4)
    head.next.next.next.next=ListNode(5)
    head.next.next.next.next.next=ListNode(6)
    start=time.time()
    head=reverse_stack(head)
    end=time.time()
    print(f"The time for stack:{end-start}")
    start2=time.time()
    head=reverse_replace(head)
    end2=time.time()
    print(f"The time for replace:{end2-start2}")
if __name__ == '__main__':
    main()