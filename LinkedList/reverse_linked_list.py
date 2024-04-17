from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1 : Brute Force         
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         stack = []
#         current = head
#         while current:
#             stack.append(current.val)
#             current = current.next
        
#         current = head
        
#         while current and stack:
#             current.val = stack.pop()
#             current = current.next
            
#         return head
    
# Optimal Approach 1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        front = head
        
        while current:
            front = front.next
            current.next = prev
            prev = current
            current = front
        return prev
            
            
class TestSolution(unittest.TestCase):
    def test_reverseList(self):
        solution = Solution()
        
        # Test case 1
        list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        reverse = solution.reverseList(list1)
        # print(reverse)
        self.assertEqual(reverse.val, 5)
        self.assertEqual(reverse.next.val, 4)
        self.assertEqual(reverse.next.next.val, 3)
        self.assertEqual(reverse.next.next.next.val, 2)
        self.assertEqual(reverse.next.next.next.next.val, 1)
        self.assertIsNone(reverse.next.next.next.next.next)

if __name__ == '__main__':
    unittest.main()
    
    
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
