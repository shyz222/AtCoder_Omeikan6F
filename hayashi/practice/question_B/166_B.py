import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

items = []

for i in range(K):
  d = int(input().rstrip())
  items.extend(list(map(int, input().rstrip().split())))

print(N - len(set(items)))
