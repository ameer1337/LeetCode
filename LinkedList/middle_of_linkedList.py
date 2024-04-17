from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         count = 0
#         while current:
#             count += 1
#             current = current.next
            
#         current = head
#         for _ in range(count//2):
#             current = current.next
#         return current
            
    
# Optimal Approach
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while( fast != None and fast.next != None ):
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
class TestSolution(unittest.TestCase):
    def test_middleNode(self):
        solution = Solution()
        
        # Test case 1
        list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        middle = solution.middleNode(list1)
        self.assertEqual(middle.val, 3)
        self.assertEqual(middle.next.val, 4)
        self.assertEqual(middle.next.next.val, 5)
        self.assertIsNone(middle.next.next.next)
        
        # Test case 2
        list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        middle = solution.middleNode(list2)
        self.assertEqual(middle.val, 4)
        self.assertEqual(middle.next.val, 5)
        self.assertEqual(middle.next.next.val, 6)
        self.assertIsNone(middle.next.next.next)
        
if __name__ == '__main__':
    unittest.main()