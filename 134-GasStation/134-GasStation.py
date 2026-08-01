# Last updated: 8/1/2026, 10:43:57 AM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3    
4        if sum(gas) < sum(cost):
5            return -1
6
7        total = 0
8        start = 0
9
10        for i in range(len(gas)):
11            total += (gas[i] - cost[i])
12            if total < 0:
13                total = 0
14                start = i + 1
15
16        return start