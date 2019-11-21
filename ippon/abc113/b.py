n = int(input())
t,a = map(int,input().split())
h_L = list(map(int,input().split()))

a_L = []
for val in h_L:
    temp = t-val*0.006
    x = abs(a-temp)
    a_L.append(x)

print(a_L.index(min(a_L))+1)