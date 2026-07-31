# Last updated: 7/31/2026, 12:45:46 PM
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        citations.sort()
4        for i in range(len(citations)):
5            if citations[i] >= len(citations) - i:
6                    return len(citations) - i
7        return 0
8