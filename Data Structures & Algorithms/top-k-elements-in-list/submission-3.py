class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_map = {}

        for i in nums:
            if i in num_map:
                num_map[i] += 1
            else:
                num_map[i] = 1

        items = list(num_map.items())
        
        items.sort(key=lambda x: x[1], reverse=True)


        result = []
        for j in range(k):
            result.append(items[j][0])
            
        return result



        

            