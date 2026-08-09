class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {}
        for k, v in enumerate(nums):
            x = target - v
            if x in num_map:
                return [num_map[x], k]
            num_map[v] = k