N, X = list(map(int, input().split()))

S = input()

ans = X
for s in S:
    if s == "o":
        ans += 1
    else:
        ans = max(0, ans - 1)
print(ans)
