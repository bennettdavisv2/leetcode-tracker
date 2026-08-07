# Last updated: 8/7/2026, 9:55:27 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = ''.join(c.lower() for c in s if c.isalnum())
4
5        L = 0
6        R = len(s) - 1
7        
8        while L < R:
9            if s[L] == s[R]:
10                L += 1
11                R -= 1
12            else:
13                return False
14        return True