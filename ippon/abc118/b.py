n,m = map(int,input().split())

for val in range(n):
    tmp = list(map(int,input().split()))
    k = tmp[0]
    if val == 0:
        a_L = set(tmp[1:])
    else:
        a_L = set(tmp[1:]) & a_L

print(len(a_L))

