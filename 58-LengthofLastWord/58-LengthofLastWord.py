# Last updated: 8/4/2026, 10:36:53 AM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        L = len(s) - 1
4        R = len(s) - 1
5
6        while not s[R].isalpha():
7            R -= 1
8        L = R
9
10        while s[L] is not (" ") and L > 0:
11            L -= 1
12
13        if s[L] is " ":
14            L += 1
15        
16        return R - L + 1
17
18        