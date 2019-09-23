n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a = [d-1 for d in a]
#print(a)
manzoku = 0
jotai = a[0]

for val in a:
    manzoku = manzoku + b[val]
    if jotai +1 == val:
        manzoku += c[val-1]
    jotai = val

print(manzoku)
