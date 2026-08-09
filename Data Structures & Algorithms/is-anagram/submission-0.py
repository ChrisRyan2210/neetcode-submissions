class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # want to sort the string and then check if equal
        if sorted(list(s)) == sorted(list(t)):
            return True
        else:
            return False