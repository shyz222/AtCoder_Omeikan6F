N = int(input())
A_list = list(map(int, input().split()))

ans = 0
keys = range(N)
A_dict = dict(zip(keys, A_list))
for i in keys:
    for j in range(i+1, N):
        A_i = A_dict[i]
        A_j = A_dict[j]
        ans += abs(A_i - A_j)

print(ans)
