class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = result = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            if nums[i] == 0:
                counter = 0
            if counter > result:
                result = counter
        return result