class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # we want to use a loop -> at each point, add the num to a sum
        # have a sub while loop that check if sum is greater than target:
            # if it is -> subtract num from sum, find min(res, len(r-l)) and incement l 

        l = 0 
        total = 0 
        res = float("inf") # infinity

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, (r - l + 1))
                total -= nums[l]
                l += 1
            r += 1

        return 0 if res == float("inf") else res
