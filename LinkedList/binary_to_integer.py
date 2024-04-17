import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         bi = ''
#         while head:
#             bi += str(head.val)
#             head = head.next
#         return int(bi, 2)

# Optimal Solution with shifting the left bit
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0
        while head:
            decimal_value = (decimal_value << 1) | head.val # shifting the left bit is equivalent to multiplying by 2
            head = head.next
        return decimal_value
    
    
class TestSolution(unittest.TestCase):
    def test_getDecimalValue(self):
        head = ListNode(1)
        head.next = ListNode(0)
        head.next.next = ListNode(1)
        self.assertEqual(Solution().getDecimalValue(head), 5)
        
        head = ListNode(0)
        self.assertEqual(Solution().getDecimalValue(head), 0)
        
        head = ListNode(1)
        self.assertEqual(Solution().getDecimalValue(head), 1)

if __name__ == '__main__':
    unittest.main()
    