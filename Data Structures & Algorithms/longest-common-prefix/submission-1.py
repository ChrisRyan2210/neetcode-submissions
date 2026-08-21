class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #we want to take the full first word and compare it to every other word
        # remove the last char if we need to

        result = ""
        
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i == len(word) or word[i] != strs[0][i]:
                    return result
            result+=strs[0][i]

        return result