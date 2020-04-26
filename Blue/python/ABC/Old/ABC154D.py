N, K = map(str, input().split())
p = list(input().split())

s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + a[i]

res = -float('inf')
for i in range(N-K):
    val = s[K+i] - s[i]
    if (res < val):
        res = val

print(res/2)

