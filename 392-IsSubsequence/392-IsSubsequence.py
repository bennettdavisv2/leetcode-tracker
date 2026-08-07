# Last updated: 8/7/2026, 10:38:20 AM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        if s == "":
4            return True
5        
6        i = 0
7
8        for c in t:
9            if c == s[i]:
10                i +=1
11            if i == len(s):
12                return True
13        return False