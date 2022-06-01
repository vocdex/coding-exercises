"""Palindrome Linked list"""
class Node:
    """Node class"""
    def __init__(self, data,next=None):
        self.data = data
        self.next = next
def is_palindrome(head):
    """Function to check if a linked list is a palindrome"""
    if head is None or head.next is None:
        return True
    # find middle of the linked list
    slow,fast=head,head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    # reverse the second half of the linked list
    # and store the head of reversed half to revert back later
    head_secod_half=reverse(slow)
    copy_head_secod_half=head_secod_half
    # compare the first and second half of the linked list
    while head and head_secod_half:
        if head.data!=head_secod_half.data:
            return False
        head=head.next
        head_secod_half=head_secod_half.next
    reverse(copy_head_secod_half)
    # revert back the head of reversed half
    if head is None and head_secod_half is None:
        return True
    return False
def reverse(head):
    prev=None
    while head:
        temp=head.next
        head.next=prev
        prev=head
        head=temp
    return prev
def main():
    head=Node(2)
    head.next=Node(4)
    head.next.next=Node(6)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(2)
    print(is_palindrome(head))
if __name__ == '__main__':
    main()