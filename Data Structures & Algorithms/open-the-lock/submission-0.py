class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque(["0000"])
        dist = 0
        visited = set()
        
        while queue:
            states = len(queue)

            for _ in range(states):
                state = queue.popleft()

                if state in visited:
                    continue
                
                visited.add(state)

                if state == target:
                    return dist

                if state in deadends:
                    continue
                
                for i in range(len(state)):
                    right = state[:i] + str((int(state[i]) + 1) % 10) + state[i + 1:]
                    left = state[:i] + str((int(state[i]) - 1) % 10) + state[i + 1:]
                    if right not in visited:
                        queue.append(right)
                    
                    if left not in visited:
                        queue.append(left)
                        
            dist += 1
        
        return -1