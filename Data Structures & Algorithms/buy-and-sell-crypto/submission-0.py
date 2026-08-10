class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        j = len(prices) - 1

        for i in range(len(prices)):
            while i < j:
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                j-=1
            j = len(prices) - 1
        return max_profit