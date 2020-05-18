N, K = map(int, input().split(" "))
p = list(map(int, input().split(" ")))

maxList = []
maxList_sum = 0
kitaichi = 0
for index in range(len(p)):
  list_p = p[index:index+K]
  if sum(list_p) > maxList_sum:
    maxList = list_p
    maxList_sum = sum(maxList)

for item in range(len(maxList)):
  # number = maxList[item]
  # s = sum(list(range(number+1)))
  # kitaichi += s / number
  kitaichi += (1 + number)/2

print(kitaichi)
