class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        i = 0
        
        while i < len(path):

            while i < len(path) and path[i] == "/":
                i += 1
            
            j = i

            while j < len(path) and path[j] != "/":
                j += 1

            if i == j:
                continue
            
            if path[i:j] == "..":
                if stack:
                    stack.pop()
            elif path[i:j] != '.':
                stack.append(path[i:j])
            
            i = j
        
        return "/" + "/".join(stack)