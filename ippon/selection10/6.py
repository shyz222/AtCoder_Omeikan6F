n = int(input())
c_L = list(map(int,input().split()))

c_L.sort(reverse=True)

alice,bob = 0,0

for val in range(len(c_L)):
    if val %2==0:
        alice += c_L[val]
    else:
        bob += c_L[val]
print(alice-bob)
