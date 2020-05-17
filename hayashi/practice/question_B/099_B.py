import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

diff = b - a
sum = diff
for i in range(diff):
  sum += i

print(int(sum - b))
