import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # dont think about this in terms of the bananas themselves
        # think about it where the value k is somewhere inside a range of values from 1 to -> max piles
        # for the example [1,4,3,2] -> we know that max we would ever need to eat is 4 and the min is always 1.
        # brute force would be to loop k = [1, .... 4] and divide piles[i] by k and keep a running total -> then return the first value where the total is less than hours
        # but we can reduce time comp by using binary search
        # [1, 2, 3, 4] -> set k to middle (2) -> check if this k is less than h, if it is it may be the answer 

        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2 # [1, 2 (here), 3, 4]
            t = 0
            for p in piles: # [1, 4, 3, 2]
                t += math.ceil(p/mid) # 6 hours in first run
            if t <= h:
                result = min(result, mid)
                right = mid - 1 # [1]
            elif t > h:
                left = mid + 1
        return result
            



            

