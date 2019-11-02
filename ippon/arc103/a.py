from collections import Counter

n = int(input())
a_L = list(map(int,input().split()))

L1,L2 = [],[]

for val in range(n):
    if val %2 == 0:
        L1.append(a_L[val])
    else:
        L2.append(a_L[val])

print(Counter(L1).values())
