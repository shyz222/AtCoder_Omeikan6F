n = int(input())
s = []

for i in range(n):
    s.append(str(input()))

cnt=[[0 for j in range(10)]for i in range(10)]

for i in range(n):
    for j in range(10):
        cnt[int(s[i][j])][j] += 1

mx=[0 for i in range(10)]

for i in range(10):
	for j in range(10):
		mx[i]=max(mx[i], 10 * (cnt[i][j] - 1) + j)

print(mx)
print(min(mx))