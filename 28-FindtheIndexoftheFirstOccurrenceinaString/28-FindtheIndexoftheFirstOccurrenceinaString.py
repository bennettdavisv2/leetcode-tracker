# Last updated: 8/6/2026, 9:46:25 AM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        count = 0
4        i = 0
5        while i < len(haystack):
6            if haystack[i] == needle[count]:
7                count += 1
8                i += 1
9            else:
10                i = i + 1 - count
11                count = 0
12            if count == len(needle):
13                return i - len(needle)
14        return -1