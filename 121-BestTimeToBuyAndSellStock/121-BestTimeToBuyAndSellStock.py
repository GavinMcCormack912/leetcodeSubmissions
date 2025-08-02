# Last updated: 8/1/2025, 10:27:19 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        maxProfit = 0

        for i in range(1, len(prices)):
            sell = prices[i]

            if prices[buy] < sell:
                profit = sell - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = i
        return maxProfit

        

        