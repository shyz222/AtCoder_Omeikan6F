import collections
import math

n = int(input())
str_L = []

for val in range(n):
    s = input()
    s_L = [i for i in s]
    s_L.sort()
    s = "".join(s_L)
    str_L.append(s)


c = collections.Counter(str_L)

str_L = list(set(str_L))


ans = 0
r = 2

def combinations_count(n, r):
    try:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    except:
        return 0

for val in str_L:
    n = c[val]
    #print(n,r)
    ans = ans + combinations_count(n,r) #comb(n, r, exact=True)

print(ans)
