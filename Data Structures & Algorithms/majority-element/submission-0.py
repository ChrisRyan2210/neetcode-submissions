class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majo = len(nums) / 2
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > majo:
                return num
        