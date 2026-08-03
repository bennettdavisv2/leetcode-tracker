# Last updated: 8/3/2026, 11:13:44 AM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        total = 0
4        i = 0
5        while i < len(s):
6            if(s[i:i + 2] in ("IV","IX", "XL", "XC", "CD", "CM")):
7                 total += self.convertHelper(s[i + 1])  - self.convertHelper(s[i])
8                 i += 2
9            else:
10                total += self.convertHelper(s[i])
11                i += 1
12        return total
13
14    def convertHelper(self, s: str) -> int:
15        if s == "I": return 1
16        if s == "V": return 5
17        if s == "X": return 10
18        if s == "L": return 50
19        if s == "C": return 100
20        if s == "D": return 500
21        if s == "M": return 1000