# Last updated: 8/1/2026, 9:12:39 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2 passes through the nums array, the first stores prefix in answer, the second multiplies the answers by post fix
        answer = [1] * (len(nums))
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix = postfix * nums[i]
        return answer