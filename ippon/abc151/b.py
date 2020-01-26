#n = int(input())
#a_L = map(int,input().split())
n,k,m = map(int,input().split())
a_L = map(int,input().split())

x = m*n - sum(a_L)
print(x)
if x >= 0 and x <= k:
    print(x)
else:
    print(-1)
