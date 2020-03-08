import math
A, B = map(int, input().split()) 
ans = -1

for i in range(1, 1001):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        ans = i
        break

print(ans)