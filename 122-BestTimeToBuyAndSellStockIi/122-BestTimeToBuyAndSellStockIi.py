# Last updated: 7/29/2026, 10:13:34 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        totalProfit = 0
        while R < len(prices):
            if (prices[R] - prices[L]) <= 0:
                L = R
                R += 1
            else: 
                totalProfit += prices[R] - prices[L]
                L = R
                R += 1
        return totalProfit