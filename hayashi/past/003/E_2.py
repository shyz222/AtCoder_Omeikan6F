# 隣接リストを用いてグラフを表した場合の解法
# 隣接リスト...情報量は辺の数に比例する

# とりあえずパラメータを全部とる
N, M, Q = list(map(int, input().split()))

raw_edge_list = []
raw_query_list = []

for i in range(M):
    u, v = list(map(int, input().split()))
    raw_edge_list.append([u-1, v-1])

colors = list(map(int, input().split()))

for i in range(Q):
    s = list(map(int, input().split()))
    raw_query_list.append(s)

# グラフ（隣接リスト）を作る
graph = []

for i in range(N):
    row = []
    # 頂点の数だけ枠をいれる
    graph.append(row)

for edge in raw_edge_list:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for query in raw_query_list:
    if query[0] == 1:
        point = query[1]-1
        print(colors[point])
        # 隣接する頂点を全部更新する
        for edge in graph[point]:
            colors[edge] = colors[point]

    else:
        point = query[1]-1
        print(colors[point])
        colors[point] = query[2]
