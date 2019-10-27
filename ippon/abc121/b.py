n,m,c = map(int,input().split())
b_L = list(map(int,input().split()))

ans = 0
for i in range(n):
    counter = 0
    a_L = list(map(int,input().split()))

    for j in range(m):
        counter += a_L[j] * b_L[j]
    counter += c

    if counter > 0:
        ans += 1

print(ans)
