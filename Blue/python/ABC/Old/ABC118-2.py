N, M = map(int, input().split())
favo = []
count = 0
for i in range(N):
        favo.append([int(x) for x in input().split()][1:])

for j in range(1, M+1):
        if all([j in x for x in favo]):
                count += 1

print(count)
