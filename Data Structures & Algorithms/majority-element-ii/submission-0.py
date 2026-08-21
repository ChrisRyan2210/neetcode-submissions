class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        m = {}
        l = len(nums)
        result = set()
        
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
            if m[num] > l/3:
                result.add(num)
        
        return list(result)
