# Last updated: 7/29/2026, 10:13:27 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        
