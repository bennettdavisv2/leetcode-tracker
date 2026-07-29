# Last updated: 7/29/2026, 10:13:49 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            index = 0
            for i in range(len(nums)):
                if nums[i] > nums[index]:
                    index +=1
                    nums[index] = nums[i]
            return index + 1

            