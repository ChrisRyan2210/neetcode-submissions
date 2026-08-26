class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # k must be between 1 and max(piles)
            # 1 and 4
    
        l = 1
        r = max(piles) + 1

        while l <= r:
            mid = (l + r) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile/mid)
            if t <= h:
                r = mid - 1
            elif t > h:
                l = mid + 1
            else:
                return mid
        return l
