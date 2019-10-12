r,d,x2000 = map(int,input().split())

x = x2000*r - d
print(x)
for val in range(9):
    x = x*r -d
    print(x)

