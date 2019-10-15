n = int(input())
h_L = list(map(int,input().split()))

h_L.append(0)

count = 0
for i in range(1,n):
    tmp_L = h_L[0:i+1]
    if h_L[i] == sorted(tmp_L)[-1]:
        count +=1

print(count+1)
