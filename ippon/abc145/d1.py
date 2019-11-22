import sys
import itertools

X,Y = map(int,input().split())

if (X+Y)%3 != 0:
    print(0)
    exit()

n = int((2*Y-X)/3)
m = int((2*X - Y)/3)
print((Y-X)/3)

if n < 0 or m < 0:
    print(0)
else:
    ans = len(list(itertools.combinations(range(n+m), n)))
    mod = 10**9+7
    print(ans%mod)
