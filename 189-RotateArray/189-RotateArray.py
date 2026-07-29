# Last updated: 7/29/2026, 10:13:25 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])