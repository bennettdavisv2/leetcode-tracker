# Last updated: 8/5/2026, 9:57:16 AM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        count = 0
4        increment = True
5        sArr = [""] * numRows
6
7        if numRows == 1:
8            return s
9
10        for i in range(len(s)):
11            if count == numRows - 1:
12                increment = False
13            if count == 0:
14                increment = True
15            
16            if increment:
17                sArr[count] += s[i]
18                count += 1
19            else:
20                sArr[count] += s[i]
21                count -= 1
22
23        result = ""
24        
25        for word in sArr:
26            result += word
27
28        return result