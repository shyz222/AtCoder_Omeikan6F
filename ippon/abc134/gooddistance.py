import numpy as np
from itertools import combinations

n,d = map(int,input().split())

vec_L = []

for val in range(n):
    a_vec = list(map(int,input().split()))
    vec_L.append(a_vec)

a = list(range(n))

comb = list(combinations(a,2))

counter_L = []


for val in comb:
    
    vec1 = np.array(vec_L[val[0]])
    vec2 = np.array(vec_L[val[1]])
    ans = np.linalg.norm(vec1 - vec2)
    counter_L.append(ans.is_integer())

print(counter_L.count(True))
