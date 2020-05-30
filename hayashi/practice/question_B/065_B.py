import sys
input = sys.stdin.readline


N = int(input().rstrip())
a_dict = {}
for i in range(N):
  a_dict[i+1] = int(input().rstrip())

target = 1
next_target = a_dict[target]
cont = True
ans = 0

if next_target == 2:
  cont = False
  ans += 1

while cont:
  target = next_target
  next_target = a_dict[target]
  ans += 1
  del a_dict[target]
  if next_target not in a_dict:
    ans = -1
    cont = False
  elif next_target == 2:
    ans += 1
    cont = False
print(ans)
