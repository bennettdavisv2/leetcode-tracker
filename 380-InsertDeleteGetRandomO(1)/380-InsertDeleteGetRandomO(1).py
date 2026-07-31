# Last updated: 7/31/2026, 12:45:14 PM
1import random
2
3class RandomizedSet:
4
5    def __init__(self):
6        self.vals = []
7        self.pos = {}
8
9    def insert(self, val: int) -> bool:
10        if val in self.pos:
11            return False
12        self.pos[val] = len(self.vals)
13        self.vals.append(val)
14        return True
15
16    def remove(self, val: int) -> bool:
17        if val not in self.pos:
18            return False
19
20        idx = self.pos[val]
21        last = self.vals[-1]
22
23        self.vals[idx] = last
24        self.pos[last] = idx
25
26        self.vals.pop()
27        del self.pos[val]
28
29        return True
30
31    def getRandom(self) -> int:
32        return random.choice(self.vals)