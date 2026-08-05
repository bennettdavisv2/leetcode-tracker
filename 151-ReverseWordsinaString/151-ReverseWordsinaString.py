# Last updated: 8/5/2026, 9:19:07 AM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        # walk through list and prepend words to an output string.
4
5        L = 0
6        R = 0
7        result = ""
8
9        while L < len(s) and R < len(s):
10            # L goes until first letter, set R = L and go until next space.
11            while not s[L].isalnum() and L < len(s) - 1:
12                L += 1
13            R = L
14            while R < len(s) - 1 and s[R + 1] is not " ":
15                R += 1
16            
17            if s[L:R + 1].isalnum():
18                result = " " + s[L:R + 1] + result
19            L = R + 1
20        return result[1:]