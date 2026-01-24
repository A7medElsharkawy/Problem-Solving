# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        ds = head
        lenth = 1
        while ds.next:
            ds = ds.next
            lenth += 1
        
        ds.next = head

        k = k % lenth

        new_tail = head
        for _ in range(lenth - k -1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head


"""Explanation:
1. . create a linked list crcular by connecting the tail to the head.
            while ds.next:
                ds = ds.next
                lenth += 1

            ds.next = head
2. Calculate the length of the linked list and connect the tail to the head to form a circular linked list.
3. Compute the effective number of rotations needed using k % length.
        - k = k % lenth
        - to handle cases where k is greater than the length of the list.
4. Find the new tail of the rotated list by moving (length - k - 1) steps from the head.
        - now we at the end of the required rotation
        - we should connect new tail to Node
        - and new next node to new head 
5. Set the new head to be the node after the new tail and break the circular link by setting new_tail.next to None.
6. Return the new head of the rotated list.
"""
