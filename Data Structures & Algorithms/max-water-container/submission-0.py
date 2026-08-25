class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Area = (j - i) * min(heights[j], heights[i])
        # (7 - 1) * min(6, 1) = 6
        # then compare heights[j-1] to heights[i+1]
        # always move the pointer of the smaller bar, as this is the limiter

        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            result = max(result, area)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return result
