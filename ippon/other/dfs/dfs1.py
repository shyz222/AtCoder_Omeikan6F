from collections import deque

H,W = map(int, input().split())
C = [input() for _ in range(H)]

# sの位置をあらかじめ調べておく
for n1,c_w in enumerate(C):
    for n2,c in enumerate(c_w):
        if c == "s":
            s_h = n1
            s_w = n2

stack = deque([[s_h, s_w]])  # スタートの位置だけ入ったスタックを作成

visited_list = [[0]*W for _ in range(H)]
visited_list[s_h][s_w] = 1

def dfs(town, visited_list, stack):
    while len(stack) > 0:
        h, w = stack.pop()
        if town[h][w] == "g":
            return "Yes"
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_h, new_w = h+j, w+k
            if new_h < 0 or new_h >= H or new_w < 0 or new_w >= W:
                continue
            if town[new_h][new_w] != "#" and visited_list[new_h][new_w] == 0:
                visited_list[new_h][new_w] = 1
                stack.append([new_h, new_w])

    return "No"

print(dfs(C, visited_list, stack))