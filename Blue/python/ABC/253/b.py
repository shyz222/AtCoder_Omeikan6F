h, w = map(int, input().split())
str_list = [input() for _ in range(h)]
l = []
for i in range(h):
    for j in range(w):
        if str_list[i][j] == 'o':
            l.append([i,j])

ans = abs(l[0][0]-l[1][0]) + abs(l[0][1]-l[1][1])
print(ans)