import numpy as np
from itertools import combinations

l,r = map(int,input().split())

a = list(range(1,l))
b = list(range(1,r))
a.extend(b)
comb = list(combinations(a,2))

ans_L = []


for val in comb:
    ans = int(val[0]) * int(val[1])
    ans = ans%2019
    ans_L.append(ans)

print(min(ans_L))
