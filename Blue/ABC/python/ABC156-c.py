N = int(input())
X = list(map(int, input().split()))
ans = float('inf')

for i in range(1,100):
    cost = 0
    
    for j in range(N):
        cost += (X[j] - i) ** 2
        
    ans = min(ans, cost)
    
print(ans)