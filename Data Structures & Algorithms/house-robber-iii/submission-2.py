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
        def dfs(node):
            if not node:
                return (0, 0)

            leftRob, leftSkip = dfs(node.left)
            rightRob, rightSkip = dfs(node.right)

            # If we rob current node, we must skip children
            rob = node.val + leftSkip + rightSkip

            # If we skip current node, children can be robbed or skipped
            skip = max(leftRob, leftSkip) + max(rightRob, rightSkip)

            return (rob, skip)

        return max(dfs(root))