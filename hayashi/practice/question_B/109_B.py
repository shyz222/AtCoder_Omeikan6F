import sys

N = int(input())
items = []
for i in range(N):
  item = input()
  items.append(item)

if(len(items) != len(set(items))):
  print('No')
  sys.exit()

for i in range(len(items)):
  if(i != 0 and items[i][0] != items[i-1][-1]):
    print('No')
    sys.exit()

print('Yes')
