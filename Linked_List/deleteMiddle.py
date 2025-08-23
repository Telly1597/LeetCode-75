# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, slow, fast = None , head, head

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev == None:
            return slow.next
        prev.next = slow.next
        return head 