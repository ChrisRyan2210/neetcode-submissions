class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # going to treat this as a stack as we need to be able to revert back (pop) to the last score
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        
        return sum(stack)