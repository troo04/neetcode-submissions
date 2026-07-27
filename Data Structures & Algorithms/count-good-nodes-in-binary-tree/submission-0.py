# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.nodes = 0

        def dfs(node, greatest):
            if not node:
                return
            
            else:
                if greatest <= node.val:
                    self.nodes += 1
                dfs(node.left, max(greatest, node.val))
                dfs(node.right, max(greatest, node.val))
        
        dfs(root, root.val)
        return self.nodes