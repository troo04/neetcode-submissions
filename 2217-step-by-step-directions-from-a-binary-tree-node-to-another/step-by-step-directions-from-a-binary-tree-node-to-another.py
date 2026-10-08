# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        adj_map = defaultdict(list)

        def dfs(node):
            if node:
                if node.left:
                    adj_map[node.val].append((node.left.val, 'L'))
                    adj_map[node.left.val].append((node.val, 'U'))

                if node.right:
                    adj_map[node.val].append((node.right.val, 'R'))
                    adj_map[node.right.val].append((node.val, 'U'))
                
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)

        queue = deque([(startValue, "")])
        visited = set()

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()

                if node[0] == destValue:
                    return node[1]
                
                if node[0] in visited:
                    continue
                
                visited.add(node[0])

                for neighbor in adj_map[node[0]]:
                    name, direction = neighbor

                    if name not in visited:
                        queue.append((name, node[1] + direction))
        
        return ""