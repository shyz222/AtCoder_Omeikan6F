n,x = map(int,input().split())
a_L = list(map(int,input().split()))

a_L = list(sorted(a_L))

counter = 0
for val in range(n):
    if x - a_L[val] >= 0 and val != n-1:
        counter += 1
        x = x-a_L[val]

    if x - a_L[val] == 0 and val == n-1:
        counter +=1
        break

print(counter)
