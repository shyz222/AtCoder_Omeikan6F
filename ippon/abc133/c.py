
from itertools import combinations
import sys

l,r = map(int,input().split())

if r-l> 2019:
    print(0)
    sys.exit(0)

A = list(range(l,r+1))

ans_L = [i[0]*i[1]%2019 for i in combinations(A,2)]
print(sorted(ans_L)[0])
