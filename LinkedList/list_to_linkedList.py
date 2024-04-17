from typing import Optional
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def list_to_linkedlist(lst):
    current = dummy = ListNode(0)
    for e in lst:
        current.next = ListNode(e)
        current = current.next
        
    return dummy.next

def traverse_linkedlist(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next
        
def search_element(head: Optional[ListNode], value: int):
    while head:
        if (head.val == value):
            return 1
        head = head.next
    return 0
        

LL = list_to_linkedlist([1,2,3,4,5])
traverse_linkedlist(LL)
print(search_element(LL, 5))