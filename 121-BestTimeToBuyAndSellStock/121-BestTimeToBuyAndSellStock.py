# Last updated: 7/29/2026, 10:13:36 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxProfit = 0
        while R < len(prices):
            if (prices[R] - prices[L]) <= 0:
                L = R
                R += 1
            else: 
                maxProfit = max(maxProfit, prices[R] - prices[L])
                R += 1
        return maxProfit