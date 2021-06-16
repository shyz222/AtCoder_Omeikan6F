import sys
sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))

route = []
visited = []

for h in range(H):
    C = list(input())
    route.append(C)
    visited.append([False] * W)


def in_maze(y, x):
    if 0 <= y <= H-1 and 0 <= x <= W-1:
        return True
    return False


def dfs(y, x):
    if not in_maze(y, x):
        return
    if visited[y][x] == True:
        return
    if route[y][x] == "#":
        return
    visited[y][x] = True
    for i, j in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
        dfs(i, j)


goal = [0, 0]
for y in range(H):
    for x in range(W):
        if route[y][x] == "s":
            dfs(y, x)
        if route[y][x] == "g":
            goal = [y, x]


print("Yes") if visited[goal[0]][goal[1]] == True else print("No")
