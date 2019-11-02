s_L = [int(val) for val in input()]
n = len(s_L)

if sum(s_L) == 0 or sum(s_L) == n:
    print(0)
    exit()
elif n == 1:
    print(0)
    exit()

one = s_L.count(1)
zero = s_L.count(0)
print(2*min(zero,one))
