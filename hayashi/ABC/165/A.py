K = int(input())
A, B = list(map(int, input().split()))

for i in range(A, B+1):
    ans = "NG"
    if i % K == 0:
        ans = "OK"
        break
print(ans)
