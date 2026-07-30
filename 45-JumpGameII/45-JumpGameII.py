# Last updated: 7/30/2026, 2:04:28 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        res = 0
4        l = r = 0
5
6        while r < len(nums) - 1:
7            farthest = 0
8            for i in range(l, r +1):
9                farthest = max(farthest, i + nums[i])
10            l = r + 1
11            r = farthest
12            res +=1
13        return res