import sys

N = int(sys.stdin.readline())
items = []
for i in range(N):
  item = list(sys.stdin.readline())
  item = item[:-1]
  items.append(item)

lists = []
for i in reversed(range(N-1)):
  if 'X' not in items[i+1]:
    pass
  for j in range(1,len(items[i])-1):
    target = items[i][j]
    under = [items[i+1][j-1], items[i+1][j], items[i+1][j+1]]
    for item in lists:
      under.append(items[item[0], item[1]])
    print(under)
    if target == '.' or target == 'X':
      pass
    elif target == '#' and 'X' in under:
      lists.append([i,j])


print(lists)
ans_item = ''
ans_item_list = []
for i in range(N):
  for j in range(2*N-1):
    if([i,j] in lists):
      ans_item += 'X'
    else:
      ans_item += items[i][j]
  ans_item_list.append(ans_item)
  ans_item = ''

for i in range(len(ans_item_list)):
  print(ans_item_list[i])
