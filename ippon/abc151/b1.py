#n = int(input())
#a_L = map(int,input().split())
n,k,m = map(int,input().split())
a_L = map(int,input().split())
goukei = sum(a_L)

for i in range(0,k+1):
    x = (goukei + i)/n
    if x >=m:
        print(i)
        exit()
print(-1)
