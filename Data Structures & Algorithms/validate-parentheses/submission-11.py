class Solution:
    def isValid(self, s: str) -> bool:

        o_stack = []
        b_map = {")":"(", "}":"{", "]":"["}
        
    
        for char in s:
            if char == "(" or char == "{" or char == "[":
                o_stack.append(char)
            elif not o_stack:
                return False
            elif b_map[char] != o_stack[-1]:  
                return False  
            else:
                o_stack.pop(len(o_stack) - 1)
        return not o_stack
            
        