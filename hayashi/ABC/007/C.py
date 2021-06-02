from collections import deque

R, C = list(map(int, input().split()))
start_y, start_x = list(map(int, input().split()))
goal_y, goal_x = list(map(int, input().split()))

start_y = start_y - 1
start_x = start_x - 1
goal_y = goal_y - 1
goal_x = goal_x - 1

maze = []

for i in range(R):
    maze_row = []
    row = input()
    for j in range(C):
        maze_row.append(row[j])
    maze.append(maze_row)

dist = []
for i in range(R):
    dist.append([-1]*C)


def in_maze(j, i):
    if j <= 0 or j >= R:
        return False
    if i <= 0 or i >= C:
        return False
    return True


queue = deque()
queue.append([[start_y, start_x]])
dist[start_y][start_x] = 0

count = 0
while len(queue) > 0:
    items = queue.popleft()
    temp = []
    for item in items:
        i, j = item
        if i == goal_y and j == goal_x:
            break
        for y, x in ([i-1, j], [i+1, j], [i, j-1], [i, j+1]):
            if not in_maze(y, x):
                continue
            if maze[y][x] == "#":
                continue
            if dist[y][x] != -1:
                continue
            temp.append([y, x])
            dist[y][x] = dist[i][j] + 1
    if len(temp) != 0:
        queue.append(temp)
        temp = []
        count += 1


print(count)
