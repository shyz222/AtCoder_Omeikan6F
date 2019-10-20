n,x = map(int,input().split())
L = list(map(int,input().split()))

d = 0
counter = 1
for val in range(n):
    d = d + L[val]
    if d <= x:
        counter +=1

print(counter)
