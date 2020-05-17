#BFS(幅優先探索のテンプレート)
from collections import deque
inf = float("INF")

N,M = map(int,input().split())
path = [[] for i in range(N)]
dist = [inf for i in range(N)]
visited = [0 for i in range(N)]

for _ in range(M):
    #辺をpathに追加
    a,b = map(int,input().split())
    #インデックスのため-1
    a = a - 1
    b = b - 1
    """
    頂点aからb,bからaへのパスを追加
    フォーマットは[[b],[a,c,d]]のようになる
    """
    path[a].append(b)
    #有向グラフの場合はここを消す
    path[b].append(a)

def BFS(path,root,visited):
    #頂点の距離は0
    dist[root] = 0
    #頂点0を初期ノードに設定、訪問済みにする
    visited[root] = 1
    #初期ノードをキューに追加
    queue = deque([root])
    #BFS開始(キューが空になるまで行う)
    while queue:
        #キューから先頭頂点を取り出す
        current = queue.popleft()
        for i in path[current]:
            #すでに訪問図済みの頂点は探索しない
            if visited[i] == 1:
                continue
            else:
                #新たな頂点iに対して距離情報を更新してキューに追加
                dist[i] = current + 1#距離情報の更新
                visited[i] = 1#訪問済みにする
                queue.append(i)#キューに追加

    if all([i == 1 for i in visited]):
        return "Yes"
    else:
        return "No"

flag = BFS(path,0,visited)