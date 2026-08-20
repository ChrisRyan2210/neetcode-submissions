from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strMap = {}
        result = []
        
        for word in strs:
            sorted = list(word)
            sorted.sort()
            k = str(sorted)
            if k not in strMap:
                strMap[k] = [word]
            else:
                strMap[k].append(word)

        for item in strMap.items():
            result.append(item[1])
        
        return result
