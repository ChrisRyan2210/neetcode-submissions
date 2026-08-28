class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # we can tell which side of the array is sorted by checking if l < m or else
        # then we check if target is in that range or not and if so, move that way
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target <= nums[m] and target >= nums[l]:
                    r = m - 1
                else: 
                    l = m + 1
            elif nums[m] <= nums[r]:
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else: 
                    r = m - 1 
        return -1 

            
                