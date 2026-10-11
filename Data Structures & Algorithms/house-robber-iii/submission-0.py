# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache
        def dfs(node, canRob):
            if not node:
                return 0
            
            res = 0
            if canRob:
                res = node.val + dfs(node.right, False) + dfs(node.left, False)
            res = max(res, dfs(node.left, True) + dfs(node.right, True))

            return res
        
        return dfs(root, True)