a,b = map(int,input().split())
L = []
tmp = 0
for i in range(10000):
    tmp += i
    L.append(tmp)

point = b-a
print(L[point]-b)
