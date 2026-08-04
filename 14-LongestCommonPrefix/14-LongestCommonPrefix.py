# Last updated: 8/4/2026, 10:55:40 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        minLength = len(strs[0])
4        
5        for word in strs:
6            minLength = min(minLength, len(word))
7
8        prefix = ""
9
10        for i in range(minLength):
11            compChar = strs[0][i]
12            for s in strs:
13                if s[i] is not compChar:
14                    return prefix
15            prefix += compChar
16        
17        return prefix
18            