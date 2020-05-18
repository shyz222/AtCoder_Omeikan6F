N = int(input())
d = list(map(int, input().split(" ")))

newList = list(dict.fromkeys(d))

if len(d) == len(newList):
  print('YES')
else:
  print("NO")
