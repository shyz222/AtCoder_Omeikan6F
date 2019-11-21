import itertools
import math

def euclid(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

x,y = [],[]
n = int(input())
for val in range(n):
    x_tmp,y_tmp = map(int,input().split())
    x.append(x_tmp)
    y.append(y_tmp)

comb = list(itertools.combinations(range(n), 2))
zyun = list(itertools.permutations(range(n)))
distance_L = {}

# あらかじめ2転換を計算
for val in comb:
    tenkan = list(sorted(list(val)))
    a = [x[val[0]],y[val[0]]]
    b = [x[val[1]],y[val[1]]]
    
    distance_L[val] = euclid(a,b)

ans = 0
counter = 0

for i in zyun:
    for j in range(n-1):
        tmp = tuple(sorted(i[j:j+2]))
        #print(tmp)
        ans += distance_L[tmp]
    counter += 1

print(ans/counter)

