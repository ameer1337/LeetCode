from typing import Optional
import unittest

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(-1)
        curret = node
        
        while list1 and list2:
            if (list1.value < list2.value):
                curret.next = list1
                list1 = list1.next
            else:
                curret.next = list2
                list2 = list2.next
            curret = curret.next
        curret.next = list1 if list1 else list2
        return node.next
            
    
class TestSolution(unittest.TestCase):
    def test_mergeTwoLists(self):
        solution = Solution()

        # Test case 1
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        merged = solution.mergeTwoLists(list1, list2)
        self.assertEqual(merged.value, 1)
        self.assertEqual(merged.next.value, 1)
        self.assertEqual(merged.next.next.value, 2)
        self.assertEqual(merged.next.next.next.value, 3)
        self.assertEqual(merged.next.next.next.next.value, 4)
        self.assertEqual(merged.next.next.next.next.next.value, 4)
        self.assertIsNone(merged.next.next.next.next.next.next)

if __name__ == '__main__':
    unittest.main()
    