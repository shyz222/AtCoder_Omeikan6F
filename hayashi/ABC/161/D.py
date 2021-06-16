from collections import deque

K = int(input())

Q = deque()

Q.append([0])

count = 0

while len(Q) > 0:
    i = Q.popleft()
    count += len(i)
    for item in i:
        temp = []
        key = str(item[-1])
        if key != "0":
            temp.append(item * 10 + int(key) - 1)
        if key != "9":
            temp.append(item * 10 + int(key) + 1)
        temp.append(item * 10 + int(key))
