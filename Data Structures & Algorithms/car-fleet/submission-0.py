class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Pair up the position and time
        # Sort by position
        # Calculate how much time it takes to reach the target
        # 

        stack = []

        paired = [(p, s) for p, s in zip(position, speed)]
        paired.sort(key = lambda x: [x][0], reverse = True)
        
        for pair in paired:
            t = (target - pair[0]) / pair[1]
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
