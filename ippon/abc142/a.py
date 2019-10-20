n = int(input())

L = []

import sys
if n ==0:
    print(0.0)
    sys.exit()

for val in range(n+1):
    if val % 2 ==1:
        L.append(val)
print(len(L)/n)
