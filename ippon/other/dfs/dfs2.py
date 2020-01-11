from collections import deque

H,W = map(int, input().split())
C = [list(input()) for _ in range(H)]

for i,l1 in enumerate(C):
    for j,l2 in enumerate(l1):
        if l2 == "s":
            start = [i,j]

stack = deque([start])

visited_list = [[0]*W for _ in range(H)]
visited_list[start[0]][start[1]] = 1



def dfs(C,stack,visited_list):
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    while len(stack) > 0:
        h,w = stack.pop()
        if C[h][w] == "g":
            print("Yes")
            exit()
        
        for i,j in move:
            new_h = h + i
            new_w = w + j
        
            if new_h <0 or new_w < 0 or new_h >= H or new_w >= W:
                continue
            if C[new_h][new_w] != "#" and visited_list[new_h][new_w] == 0:
                visited_list[new_h][new_w] = 1
                stack.append([new_h,new_w])
    print("No")

dfs(C,stack,visited_list)



