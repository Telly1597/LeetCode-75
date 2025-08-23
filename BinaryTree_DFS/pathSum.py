# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, cur_sum):
            if not node:
                return 0

            cur_sum += node.val
            count = prefix_map[cur_sum - targetSum]

            prefix_map[cur_sum] += 1
            count += dfs(node.left, cur_sum)
            count += dfs(node.right, cur_sum)
            prefix_map[cur_sum] -= 1

            return count
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        return dfs(root, 0)