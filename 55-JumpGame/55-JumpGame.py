# Last updated: 7/30/2026, 1:41:24 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        goal = len(nums) - 1
4        for i in range(len(nums) - 1, -1, -1):
5            if i + nums[i] >= goal:
6                goal = i
7        return True if goal == 0 else False 