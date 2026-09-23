# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        adj_map = defaultdict(list)

        def dfs(node):
            if node:
                if node.left:
                    adj_map[node.val].append(node.left.val)
                    adj_map[node.left.val].append(node.val)
                
                if node.right:
                    adj_map[node.val].append(node.right.val)
                    adj_map[node.right.val].append(node.val)
                
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        queue = deque([start])
        counter = 0
        visited = set()
        visited.add(start)

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                for neighbor in adj_map[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
            if queue:
                counter += 1
        
        return counter