N = int(input())

ans = 0


def dfs(n, use3, use5, use7):
    global ans
    if n > N:
        return
    if use3 and use5 and use7:
        ans += 1
    dfs(10*n + 3, True, use5, use7)
    dfs(10*n + 5, use3, True, use7)
    dfs(10*n + 7, use3, use5, True)


dfs(0, False, False, False)

print(ans)
