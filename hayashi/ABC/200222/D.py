from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n,a,b = map(int, input().split())

sum = pow(2,n,1000000007) -1

a = min(a, n-a)
b = min(b, n-b)
ans = sum - cmb(n,a)-cmb(n,b)

print(ans)
