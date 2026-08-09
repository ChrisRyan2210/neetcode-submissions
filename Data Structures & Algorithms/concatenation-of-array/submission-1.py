class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return 2 * nums
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans