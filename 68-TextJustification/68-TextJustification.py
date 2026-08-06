# Last updated: 8/6/2026, 10:51:15 AM
1class Solution:
2    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
3        res = []
4        i = 0
5        n = len(words)
6        
7        while i < n:
8            line = []
9            letters = 0
10
11            while i < n and letters + len(words[i]) + len(line) <= maxWidth:
12                line.append(words[i])
13                letters += len(words[i])
14                i += 1
15            
16            if i == n or len(line) == 1:
17                s = " ".join(line)
18                s += " " * (maxWidth - len(s))
19                res.append(s)
20            else:
21                total_spaces = maxWidth - letters
22                gaps = len(line) - 1
23                even_space = total_spaces // gaps
24                extra_space = total_spaces % gaps
25                s = ""
26
27                for j in range(gaps):
28                    s += line[j]
29                    s += " " * even_space
30                    if j < extra_space:
31                        s += " "
32                
33                s += line[-1]
34                res.append(s)
35        return res