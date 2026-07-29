# Last updated: 7/29/2026, 10:13:18 AM
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def binaryCalculator(n:int) -> int:
            sumOfOnes = 0
            while n > 0:
                sumOfOnes += n % 2
                n = n // 2
            return sumOfOnes

        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = binaryCalculator(i)
        
        return ans
            
        