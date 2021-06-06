import sys
sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))

graph = []
for start in range(N):
    graph.append([])

for start in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)


def dfs(i):
    if goals[i] == True:
        return
    goals[i] = True
    # いい加減覚える
    # pythonのin演算子はO(N)で探す
    # if i in goals:
    #     return
    # goals.append(i)
    for j in graph[i]:
        dfs(j)


ans = 0
for start in range(N):
    # goals = []
    # dfs(start)
    # ans += len(goals)
    goals = [False] * N
    dfs(start)
    ans += sum(goals)
print(ans)
