N = int(input())
items = []

for i in range(N):
  item = list(input().split())
  item[1] = abs(100 - int(item[1]))
  item.append(i+1)
  items.append(item)

items = sorted(items)

for i in items:
  print(i[2])
