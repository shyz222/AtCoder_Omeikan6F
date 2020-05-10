import sys
input = sys.stdin.readline

S = input().rstrip()
N = int(input().rstrip())

order = []
for i in range(N):
  l,r = map(int, input().rstrip().split())
  order.append([l-1, r-1])

string = S
length = len(S)
for i in range(N):
  order_i = order[i]
  rev_start = order_i[0] - length
  rev_end = order_i[1] - length
  string = string[:order_i[0]] + string[rev_end:rev_start-1:-1] + string[order_i[1]+1:]
print(string)
