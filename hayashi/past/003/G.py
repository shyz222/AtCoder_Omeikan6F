from collections import deque

N, X, Y = list(map(int, input().split()))

start = [201, 201]
X += 201
Y += 201

maze = []
dist = []
for i in range(403):
    maze.append([0] * 403)
    dist.append([False] * 403)


for i in range(N):
    x, y = list(map(int, input().split()))
    x += 201
    y += 201
    maze[y][x] = -1


def in_maze(x, y):
    if (0 <= x <= 402) and (0 <= y <= 402):
        return True
    return False


queue = deque()

queue.append([start])

while len(queue) > 0:
    items = queue.popleft()
    temp = []
    for item in items:
        i, j = item
        if i == Y and j == X:
            break
        for y, x in ([i+1, j+1], [i+1, j], [i+1, j-1], [i, j+1], [i, j-1], [i-1, j]):
            if not in_maze(y, x):
                continue
            if dist[y][x] == True:
                continue
            if maze[y][x] == -1:
                continue
            temp.append([y, x])
            maze[y][x] = maze[i][j] + 1
            dist[y][x] = True
        if len(temp) != 0:
            queue.append(temp)
            temp = []

ans = -1

if maze[Y][X] != 0:
    ans = maze[Y][X]

print(ans)
