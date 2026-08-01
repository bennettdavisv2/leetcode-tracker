# Last updated: 8/1/2026, 9:12:39 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        # 2 passes through the nums array, the first stores prefix in answer, the second multiplies the answers by post fix
4        answer = [1] * (len(nums))
5        prefix = 1
6        postfix = 1
7
8        for i in range(len(nums)):
9            answer[i] = prefix
10            prefix = prefix * nums[i]
11        for i in range(len(nums) - 1, -1, -1):
12            answer[i] *= postfix
13            postfix = postfix * nums[i]
14        return answer