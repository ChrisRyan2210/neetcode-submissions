class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Data Struc: Array/Hash Set
        # Algo: n/a
        # Time: 
        # Space:
        
        # the trick is that any sequence of numbers must start somewhere -> so for any number i, if we check that i - 1 doesnt exist in the hash set, then we know that that is the start of a sequence and we can begin our count, otherwise just ignore

        s = set(nums)
        longest = 0

        for n in s:
            if (n - 1) not in s:
                length = 1
                curr = n
                while (curr + 1) in s:
                    length += 1
                    curr += 1
                longest = max(longest, length)
        return longest