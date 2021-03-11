# 隣接行列を用いてグラフを表した場合の解法
# 隣接行列...頂点数の2乗の情報量を持つ

# とりあえずパラメータを全部とる
N, M, Q = list(map(int, input().split()))

raw_node_list = []
raw_query_list = []

for i in range(M):
    u, v = list(map(int, input().split()))
    raw_node_list.append([u-1, v-1])

colors = list(map(int, input().split()))

for i in range(Q):
    s = list(map(int, input().split()))
    raw_query_list.append(s)

# グラフ（隣接行列）を作る
graph = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(False)
    graph.append(row)

for node in raw_node_list:
    graph[node[0]][node[1]] = True
    graph[node[1]][node[0]] = True

for query in raw_query_list:
    if query[0] == 1:
        point = query[1]-1
        print(colors[point])
        # 隣接する頂点を全部更新する
        for i in range(len(graph[point])):
            if graph[point][i] == True:
                colors[i] = colors[point]

    else:
        point = query[1]-1
        print(colors[point])
        colors[point] = query[2]
