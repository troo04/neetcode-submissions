class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == '(':
                left_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                else:
                    if star_stack:
                        star_stack.pop()
                    else:
                        return False
        
        if len(star_stack) < len(left_stack):
            return False
        
        while left_stack:
            if star_stack[-1] >= left_stack[-1]:
                star_stack.pop()
                left_stack.pop()
            else:
                return False
        
        return True