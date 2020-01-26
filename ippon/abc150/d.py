n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = a[0]

import fractions
for i in range(1, len(a)):
    #ans = fractions.gcd(ans, a[i])
    ans = ans * a[i] // fractions.gcd(ans, a[i])

counter = 1
while True:
    ans = counter * ans
    if ans >= m:
        break
    counter += 1

counter = 0
while True:
    if ans % 2 !=0:
        print(counter)
        exit()
    ans = ans/2
    counter += 1

print(counter+1)
