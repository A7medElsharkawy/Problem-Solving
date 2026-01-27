# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            tail.next = ListNode(total % 10)
            tail = tail.next
            
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        return dummy.next
    
    """"
    time complexity: O(max(N,M)) where N and M are the lengths of l1 and l2
    space complexity: O(max(N,M)) for the output linked list"""

