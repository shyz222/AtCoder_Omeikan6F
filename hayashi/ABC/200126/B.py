H, N = map(int, input().split())

list = list(map(int,list(input().split())))

if sum(list) >= H:
  print('Yes')
else:
  print('No')
