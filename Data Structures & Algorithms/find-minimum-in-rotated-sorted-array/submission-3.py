class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # we use binary search 
        # we can figure out if the array is rotated by comparing m to r 
        # we use this to know which side the small numbers are in 

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]
