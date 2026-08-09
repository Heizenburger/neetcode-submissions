class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            buy = min(prices[i], buy)
            sell = prices[i]
            max_profit = max(sell - buy, max_profit)
        return max_profit