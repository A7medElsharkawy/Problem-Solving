# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        curr = head

        while curr:
            dumb = curr.next
            curr.next = pre
            pre = curr
            curr = dumb
        
        return pre


""""
Time Complexity: O(n)
Space Complexity: O(1)
"""