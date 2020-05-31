import math
A, B = map(float, input().split())
A = int(A)
B = int(B*1000)
ans = A * B // 1000
print(ans)