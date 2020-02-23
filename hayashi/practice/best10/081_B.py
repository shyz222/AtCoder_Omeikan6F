N = int(input())
list = list(map(int, input().split()))

count = 0

for i,item in enumerate(list):
  if item%2 != 0:
    break
  list[i] = item/2


print(count)
