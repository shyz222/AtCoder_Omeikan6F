N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=False)
ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += A[i]
    else:
        ans -= A[i]

print(abs(ans))
