class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # technically a monotonic decreasing stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    

    # [1, 2, 3] is given
    # lets say we want to add 0
    # we can just append it to our normal stack as usual -> [1,2,3,0]
    # but we want to update our minStack so it holds only the smallest value