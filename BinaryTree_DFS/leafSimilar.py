# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 
            if node.left == None and node.right == None:
                yield node.val 
                return 
            yield from dfs(node.left)
            yield from dfs(node.right)
            
        return list(dfs(root1)) == list(dfs(root2))