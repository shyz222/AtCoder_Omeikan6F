n = int(input())
x_L = list(map(int,input().split()))
x_L = list(sorted(x_L))
start = x_L[0]
end = x_L[-1]
a = 10**20
for i in range(start,end+1):
    sums = 0
    for k,val in enumerate(x_L):
        sums += (x_L[k]-i)**2
    a = min(a,sums)
print(a)