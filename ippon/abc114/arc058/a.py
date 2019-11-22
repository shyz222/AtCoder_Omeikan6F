n,k = map(int,input().split())
d_L = list(map(str,input().split()))

a_L = [str(val) for val in range(10)]

use_num = list(set(a_L) - set(d_L))

ans = 0
while True:
    c = list(set(list(str(n)))) + use_num
    if len(use_num) == len(list(set(c))):
        print(n)
        exit()

    n += 1
