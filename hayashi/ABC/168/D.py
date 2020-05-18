import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ans_dict = dict(zip(list(range(2, N+1)), {}))
root_dict = {}
for i in range(M):
  A, B = map(int, input().rstrip().split())
  minimum = min(A, B)
  maximum = max(A, B)
  if minimum not in root_dict:
    root_dict[minimum] = [maximum]
  else:
    root_dict[minimum].append(maximum)

root_sorted = sorted(root_dict.items(), key=lambda x: x[0])
print(root_sorted)

# for i in root_sorted.values():
#   for j in i:
