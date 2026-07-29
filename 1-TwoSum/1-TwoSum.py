# Last updated: 7/29/2026, 10:14:17 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Avoid checking pairs twice
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # Return an empty list if no solution is found
