# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # let's reverse the list.
        slow, fast = head , head 
        max_val = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        cur , prev = slow , None
        # print(head)
        while cur:
            cur.next, prev, cur = prev, cur, cur.next 
        
        while prev:
            max_val = max(max_val, head.val + prev.val)
            head = head.next
            prev = prev.next
        
        return max_val