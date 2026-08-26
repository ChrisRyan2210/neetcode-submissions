class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Data Struc: Hash Map
        # 
        # Time: 
        # Space:
        
        m = {}
        res = []

        for word in strs:
            s = "".join(sorted(word))
            if s not in m:
                m[s] = [word]
            else:
                m[s].append(word)
        
        for item in m.items():
            res.append(item[1])
        
        return res
            
            