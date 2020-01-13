import numpy
N = int(input())
integerList = list(map(int, input().split()))

table = []
for s in integerList:
    miniTable = []
    for i in range(2,int(s**0.5)+1):
         if s % i == 0:
             miniTable.append(i)
             if i != s//i:
                 miniTable.append(s//i)
    miniTable.append(s)
    table.append(miniTable)
# print(table)

items = []
for v in table:
    for item in v:
        items.append(item)
#
# print(items)
kouyakusuList = []
for item in items:

    if items.count(item) >= N-1:
        kouyakusuList.append(item)
        # print(item)

print(max(kouyakusuList))
