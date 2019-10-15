n,m = map(int,input().split())

tmp = set()

for val in range(m):
    l,r = map(int,input().split())
    tmp = set(list(range(l,r+1)))
    if val ==0:
        seki = tmp
    else:
        seki = seki & tmp

print(len(list(seki)))
