# Last updated: 7/29/2026, 10:13:26 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 1, nums[0]
        for i in nums[1:]:
            count += 1 if i == result else -1
            if count < 0:
                result = i
                count += 1
        return result