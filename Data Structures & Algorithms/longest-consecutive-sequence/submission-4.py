class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # NESTED LOOP but the n-1 check makes it run in O(n) time
        # But we want to only start counting if n - 1 is not in the set becaue otherwise we have already started counting that sequence


        numSet = set(nums)
        i = 0 
        longest = 0
        
        for num in numSet:
            counter = 1
            if num - 1 in numSet:
                continue
            while num + 1 in numSet:
                counter += 1
                num = num + 1
            longest = max(longest, counter)

        return longest

            