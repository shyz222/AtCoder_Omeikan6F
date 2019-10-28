N, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(N)]

print(AB)
rest = M
ans = 0
for a, b in sorted(AB, key=lambda x: x[0]):
    if (b < rest):
        ans += a*b
        rest -= b
    else:
        ans += (a*rest)
        break
print(ans)