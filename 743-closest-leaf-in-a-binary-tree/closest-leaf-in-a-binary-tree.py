# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode | None, k: int) -> int:
        
        graph = defaultdict(list)

        def create_graph(node):
            if node:
                if len(graph[node]) == 0:
                    graph[node] = []

                if node.left:
                    graph[node.left].append(node)
                    graph[node].append(node.left)
                    create_graph(node.left)
                
                if node.right:
                    graph[node.right].append(node)
                    graph[node].append(node.right)
                    create_graph(node.right)
            
        create_graph(root)

        queue = deque([node for node in graph if node.val == k])
        seen = set()
        while queue:
            nodes = len(queue)

            for _ in range(nodes):
                temp = queue.popleft()

                if not temp.left and not temp.right:
                    return temp.val

                for neighbor in graph[temp]:
                    if neighbor.val not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor.val)
        
        return -1