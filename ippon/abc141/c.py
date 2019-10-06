import collections

n,k,q = map(int,input().split())

a_L = []
for val in range(q):
    a_L.append(int(input()))

a_L = [i-1 for i in a_L]

count = collections.Counter(a_L)

all_L = list(map(lambda x:x-q,[k]*n))

for val in range(n):
    point = all_L[val] + count[val]
    if point > 0:
        print("Yes")
    else:
        print("No")


