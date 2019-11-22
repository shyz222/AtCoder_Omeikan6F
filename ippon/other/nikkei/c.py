import numpy as np

n = int(input())
a_L = list(map(int,input().split()))
b_L = list(map(int,input().split()))

a_L = sorted(a_L)
b_L = sorted(b_L)

a = np.array(a_L)
b = np.array(b_L)

check = a-b
check = check <= 0

#print(check)

if False not in check:
    print("Yes")
else:
    print("No")
