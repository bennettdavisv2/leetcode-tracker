# Last updated: 8/2/2026, 11:57:01 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        if len(height) <= 1:
4            return 0
5        L = 0
6        R = 1
7        possWater = 0
8        total = 0
9
10        while R < len(height):
11            if height[R] >= height[L]:
12                total += possWater
13                possWater = 0
14                L = R
15                R += 1
16            else:
17                possWater += (height[L] - height[R])
18                R += 1
19
20        peak = L
21        R = len(height) - 1
22        L = len(height) - 2
23        possWater = 0
24
25        while L >= peak:
26            if height[L] >= height[R]:
27                total += possWater
28                possWater = 0
29                R = L
30                L -= 1
31            else:
32                possWater += height[R] - height[L]
33                L -= 1
34        
35        return total