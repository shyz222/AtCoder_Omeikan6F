n = int(input())
v_L = list(map(int,input().split()))
c_L = list(map(int,input().split()))


ans = 0
for val in range(len(v_L)):
    if v_L[val] - c_L[val] >= 0:
        ans += v_L[val] - c_L[val]

print(ans)
    
