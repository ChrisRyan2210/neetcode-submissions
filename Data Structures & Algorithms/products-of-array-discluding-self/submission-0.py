class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # set up result array of [1]s
        res = [1] * len(nums)

        # multiply res[i] by num to that point then increase total
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
        