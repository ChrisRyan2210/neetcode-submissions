class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = []
        for item in count.items():
            result.append(item[0])
        result.sort(key = lambda x: count[x], reverse = True)
        
        return result[0:k]

            
            