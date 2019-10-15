n,m = map(int,input().split())

l_L,r_L = [],[]

for val in range(m):
    l,r = map(int,input().split())

    l_L.append(l)
    r_L.append(r)

r = min(r_L)
l = max(l_L)

if r-l >= 0:
    print(r-l+1)
else:
    print(0)
