# Last updated: 8/2/2026, 12:51:26 PM
1class Solution:
2    def candy(self, ratings: List[int]) -> int:
3        n = len(ratings)
4        candy = [1] * n
5
6        for i in range(1, n):
7            if ratings[i] > ratings[i - 1]:
8                candy[i] = candy[i - 1] + 1
9
10        for i in range(n - 2, -1, -1):
11            if ratings[i] > ratings[i + 1]:
12                candy[i] = max(candy[i], candy[i + 1] + 1)
13
14        return sum(candy)