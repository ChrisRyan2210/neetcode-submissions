class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # if its valid, we move just icrement the map
        # if its not valid we move l to the right by 1 and decrement the counter map by 1 for that key/letter

        # AAABABB
        # after 3 loops we have l = 0, r = 2 and {A:3}
        # next loop we have r = 3 and {A:3, B:1}
        # at each loop check if winow len (r-l + 1) - maxfreq <= k which is essentially checking if the other values in the map occur more than k times
        # next 2 loops we have l = 6 and {A:4, B:2}
        # now l - maxfreq > k so we shift l forward 1 and decrement
        # remember to check maxfreq at each time we increment map

        count = {}
        res = 0
        l = 0
        maxfreq = 0

        for r in range(len(s)):
            # increment the map
            if s[r] in count:
                count[s[r]] += 1
            else: 
                count[s[r]] = 1
            # recalculate max frequency
            maxfreq = max(maxfreq, count[s[r]])
            # while our window is not valid
            while (r - l + 1) - maxfreq > k:
                # increment l and decrement the map value
                count[s[l]] -= 1 
                l += 1
            # update result
            res = max(res, r - l + 1)

        return res