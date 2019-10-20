n = int(input())


a_L = list(map(int,input().split()))

d = {}

for val in range(n):
    d[val] = a_L[val]

#print(d)
ans = sorted(d.items(),key=lambda x:x[1])
#print(ans)

ans_L = []

for val in ans:
    ans_L.append(str(val[0]+1))

print(" ".join(ans_L))
