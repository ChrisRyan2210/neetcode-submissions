class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold stock when next day price is higher
        # dont hold when next day is lower

        profit = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                break
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]

        return profit
