n = input()
#a,b = map(int,input().split())
a_L = list(map(int,input().split()))

ans_L = []

from itertools import product, permutations,combinations
for i in combinations(a_L,2):
    ans_L.append(i[0]*i[1])

print(sum(ans_L))
