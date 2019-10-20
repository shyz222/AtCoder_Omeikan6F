

n = int(input())
a_L = list(map(int,input().split()))

diff_L = []

for t in range(n):
    sum1 = sum(a_L[:t])
    sum2 = sum(a_L[t:])
    diff_L.append(abs(sum1-sum2))

print(sorted(diff_L)[0])
