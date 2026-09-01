class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # we can use a map to store the letter and the index of the letter -> we can then update l to point to index if we see this letter again

        l = 0 
        letters = {}
        res = 0

        for r in range(len(s)):
            if s[r] in letters and letters[s[r]] >= l:
                l = letters[s[r]] + 1
            letters[s[r]] = r
            res = max(res, r - l + 1)
        return res


        # {p:0}
        # {p:0, w:1}
        # 

        

            

        


