n,k = map(int,input().split())
a_L = list(map(int,input().split()))

counter = 0
for val in range(n):
    if int(a_L[val]) >= int(k):
        counter += 1
print(counter)
