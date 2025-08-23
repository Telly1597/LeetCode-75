from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')
        queue = deque()
        queue.append(root)
        cur_index, max_sum_index = 0 , 0

        while queue:
            total = 0
            cur_index += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if total > max_val: 
                max_val = total 
                max_sum_index = cur_index
                
        return max_sum_index