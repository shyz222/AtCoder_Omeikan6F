import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

aaa = tuple(p)
bbb = tuple(q)
pm = list(itertools.permutations(set(p)))
a = pm.index(aaa) + 1
b = pm.index(bbb) + 1
print(abs(a-b)) 
