N = int(input())
l = [input() for i in range(N)]
l = list(set(l))

print(len(l))