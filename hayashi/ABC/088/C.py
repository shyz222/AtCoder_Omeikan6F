grid = []
for _ in range(3):
    row = list(map(int, input().split()))
    grid.append(row)

ans = "Yes"
for i in range(1, 3):
    row_list = []
    col_list = []
    for j in range(3):
        row_list.append(grid[j][i] - grid[j][i-1])
        col_list.append(grid[i][j] - grid[i-1][j])

    if len(list(set(row_list))) != 1:
        ans = "No"
        break

print(ans)
