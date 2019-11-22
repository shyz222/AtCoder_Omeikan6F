import math

s_L = [int(val) for val in input()]

n = len(s_L)
g = sum(s_L)

if g > n/2:
    g = g - math.ceil(n/2)
    #print(n-2*g)
    print(2*g)
elif g == n/2:
    print(n)
    exit()
elif n ==0:
    print(0)
    exit()
print(2*g)
