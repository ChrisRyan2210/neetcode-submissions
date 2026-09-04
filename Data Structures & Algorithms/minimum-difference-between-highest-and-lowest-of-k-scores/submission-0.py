class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l = 0 
        res = float("inf")

        for r in range(len(nums)):
            if (r - l + 1) > k:
                l += 1
            if (r - l + 1) == k:
                res = min(res, nums[r] - nums[l])
        return res
        
        # [1, 2, 3, 3, 5, 6]