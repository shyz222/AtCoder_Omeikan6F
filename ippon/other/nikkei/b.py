import itertools

n = input()
d_L = list(map(int,input().split()))

d_L = list(sorted(d_L))


g = itertools.groupby(d_L)

ans = 1
for key, gr in g:
    #ans = ans*len(list(gr))
    #print(key,len(list(gr)))
    print(key,list(gr))
print(ans%998244353)