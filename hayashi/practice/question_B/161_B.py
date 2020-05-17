import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

votes = list(map(int, input().rstrip().split()))
ans = []

for i in range(len(votes)):
  if votes[i] >= sum(votes) / (4*M):
    ans.append(votes[i])

if len(ans) >= M:
  print('Yes')
else:
  print('No')
