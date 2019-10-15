a_L = list(map(int,input().split()))
ans = 0
for val in range(2):
    a_L.sort(reverse=True)
    ans += a_L[0]
    a_L[0] -=1
print(ans)
