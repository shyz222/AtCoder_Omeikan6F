import math

a,b,x = list(map(int, input().split(" ")))
list = []
for i in range(1,len(str(x))+1):
    y = math.floor((x - b*i)/a)
    if len(str(y)) == i and x >= y >=0:
        list.append(y)
    else:
        list.append(0)

ans = max(list)
if ans>=10**9:
    ans = 10**9
print(ans)
