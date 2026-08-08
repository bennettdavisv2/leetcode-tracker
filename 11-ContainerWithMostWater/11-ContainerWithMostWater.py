# Last updated: 8/8/2026, 10:47:12 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        # Compute area for each. But there's two variables, height and length. height can be anything, length increases constantly. How do you not do this in O(N^2)?
4        l = 0
5        r = len(height) - 1
6        maxArea = 0
7
8        while l < r:
9            maxArea = max(maxArea, ((r-l) * min(height[l], height[r])))
10            if height[l] <= height[r]:
11                l += 1
12            else: 
13                r -= 1
14        return maxArea