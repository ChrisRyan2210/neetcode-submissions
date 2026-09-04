class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # this is sliding window variable size
        # keep expanding the window while we are valid
        # valid when we have flipped at most 1 time and nums[r] != 0
        # when we are not valid we move l to i0 + 1

        l = 0
        res = 1 # answer will always be at least 1
        flip = 1

        for r in range(len(nums)):
            if nums[r] == 1 or flip > 0:
                res = max(res, (r - l + 1))
            if nums[r] == 0 and flip <= 0:
                l = i + 1
            if nums[r] == 0:
                i = r
                flip -= 1
        return res            

