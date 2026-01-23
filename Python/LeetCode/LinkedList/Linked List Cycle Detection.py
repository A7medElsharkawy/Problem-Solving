# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        l = head
        f = head

        while f and f.next:
            l=l.next
            f=f.next.next
            if l == f:
                return True
        return False


"""
time complexity: O(n)
space complexity: O(1)
"""
