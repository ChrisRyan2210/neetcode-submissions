class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # add i to map, check if target - i is in list
        map = {}

        for k, v in enumerate(nums):
            complement = target - v
            if complement in map:
                return [map[complement], k]
            else:
                map[v] = k # Add the current number and its index to the map
            
            
        
        