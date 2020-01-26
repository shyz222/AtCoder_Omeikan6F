n,k = map(int,input().split())
L = []
for val in range(n):
    val = int(input())
    L.append(val)

L = sorted(L)
ans_L = []
for i in range(n-k+1):
    ans = L[i+k-1] - L[i]
    ans_L.append(ans)
print(min(ans_L))
