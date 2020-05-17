import sys
input = sys.stdin.readline

N = int(input().rstrip())

values = list(map(int, input().rstrip().split()))
keys = list(range(1,N+1))

q_dic = dict(zip(keys, values))
ans = []

M = int(input().rstrip())

drinks = []
for i in range(M):
  a, b = map(int, input().rstrip().split())
  items = {a: b}
  drinks.append(items)

for i in range(len(drinks)):
  key = list(drinks[i].keys())[0]
  val = list(drinks[i].values())[0]
  q_dic[key] = val
  ans.append(sum(q_dic.values()))
  q_dic = dict(zip(keys, values))

for i in range(len(ans)):
  print(ans[i])
