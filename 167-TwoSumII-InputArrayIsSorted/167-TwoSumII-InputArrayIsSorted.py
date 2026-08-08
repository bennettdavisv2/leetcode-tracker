# Last updated: 8/8/2026, 10:35:25 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        result = [1] * 2
4        l = 0
5        r = len(numbers) - 1
6        while l < r:
7            if numbers[l] + numbers[r] == target:
8                result[0] += l
9                result[1] += r
10                return result
11            else:
12                if numbers[l] + numbers[r] > target:
13                    r -= 1
14                else:
15                    l += 1
16        return result