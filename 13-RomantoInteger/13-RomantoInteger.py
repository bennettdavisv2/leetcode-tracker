# Last updated: 8/3/2026, 1:32:24 PM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        s = str(num)
4        roman = ""
5        decimalPlace = len(s)
6        for ch in s:
7            d = int(ch)
8            if d not in (4, 9):
9                if decimalPlace == 4:
10                    roman += "M" * d
11                if decimalPlace == 3:
12                    if d <= 3:
13                        roman += "C" * d
14                    if d == 5:
15                        roman += "D"
16                    if d >= 6:
17                        roman += "D" + ("C" * (d % 5))
18                if decimalPlace == 2:
19                    if d <= 3:
20                        roman += "X" * d
21                    if d == 5:
22                        roman += "L"
23                    if d >= 6:
24                        roman += "L" + ("X" * (d % 5))
25                if decimalPlace == 1:
26                    if d <= 3:
27                        roman += "I" * d
28                    if d == 5:
29                        roman += "V"
30                    if d >= 6:
31                        roman += "V" + ("I" * (d % 5))
32            else:
33                if decimalPlace == 3:
34                    roman += "CD" if d == 4 else "CM"
35                if decimalPlace == 2:
36                    roman += "XL" if d == 4 else "XC"
37                if decimalPlace == 1:
38                    roman += "IV" if d == 4 else "IX"
39            decimalPlace -= 1
40        return roman