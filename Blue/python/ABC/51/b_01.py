K, S = map(int, input().split())
res = 0
for x in range(K+1):
    y_z = S - x
    if y_z < 0:
        continue
    
    y_min = max(y_z-K,0)
    y_max = min(y_z,K)
    res += max(y_max-y_min+1,0)

print(res)