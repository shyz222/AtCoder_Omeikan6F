import math

n,k = map(int,input().split())

ans = 0
for val in range(1,n+1):
    #print(val,",",math.log2(k)-math.log2(val))
    x = math.ceil(math.log(k,2)-math.log(val,2))
    ans = ans + 1/n * (1/2)**x 
print(ans)
