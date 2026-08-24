class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for token in tokens:
            if token == '+':
                l = stack.pop()
                r = stack.pop()
                stack.append(int(l) + int(r))
            elif token == '-':
                l = stack.pop()
                r = stack.pop()
                stack.append(int(r) - int(l))
            elif token == '*':
                l = stack.pop()
                r = stack.pop()
                stack.append(int(l) * int(r))
            elif token == '/':
                l = stack.pop()
                r = stack.pop()
                stack.append(int(int(r/l)))
            else: 
                stack.append(int(token))

        return stack[-1]