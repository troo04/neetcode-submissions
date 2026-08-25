class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == "+":
                stack.append(stack.pop() + stack.pop())
            elif tok == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif tok == "*":
                stack.append(stack.pop() * stack.pop())
            elif tok == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(tok))
        
        return stack[0]