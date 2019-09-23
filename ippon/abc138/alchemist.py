n = int(input())
v_L = list(map(int,input().split()))

v_L.sort()

result = v_L[0]
for val in range(1,n):
    result = (result + v_L[val])/2

print(result)
