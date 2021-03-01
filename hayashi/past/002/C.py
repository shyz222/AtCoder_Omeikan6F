N = int(input())

grid = []
for _ in range(N):
    row = list(input())
    grid.append(row)

# [N-2(-1-1), N-3, ... , 2, 1, 0]
for i in list(reversed(range(N-1))):
    for j in range(N - i - 1, N + i):
        if grid[i+1][j-1] == "X" or grid[i+1][j] == "X" or grid[i+1][j+1] == "X":
            grid[i][j] = "X"

for item in grid:
    print("".join(item))
