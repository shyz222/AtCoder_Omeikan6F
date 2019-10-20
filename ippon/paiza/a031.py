#p1,p2,p3,k = map(int,input().split())
import math

L = list(map(int,input().split()))
k = L[-1]
L.pop()

L = sorted(L,reverse=True)

a_L = []

for _a in range(k):
    for _b in range(k):
        for _c in range(k):
            ans = L[0]**_c * L[1]**_b * L[2]**_a
            a_L.append(ans)


print(sorted(a_L)[k-1])
