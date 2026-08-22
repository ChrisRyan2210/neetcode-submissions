class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # the idea is that we add elements to a set then loop through nums again, check if the val the val is in the set, and keep a counter then return the highest counter.
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

            