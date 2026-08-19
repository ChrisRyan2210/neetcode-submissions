class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # put into a hashmap
        # keep track of max number
        # then do another loop that goes from 0 to max_num
        # keep track of a counter that checks if +1 exists, if yes, counter+1 else counter = 0 but first set result = counter if greater

        result = 0
        m = {} 
        length = 0

        # this gets us O(1) look up on numbers and a max num
        for k, v in enumerate(nums):
            if v not in m:
                m[v] = k
        # {2:0, 20:1, 4:2, 10:3, 3:4, 4:5, 5: 6}
        
        
        for n in nums:
            if n - 1 not in m: # then we know it is the start of seq    
                counter = 0
                while n in m:
                    n += 1
                    counter += 1
                if counter > length:
                    length = counter
                    # counter = 0
        return length
            
        