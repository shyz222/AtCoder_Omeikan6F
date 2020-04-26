H = int(input())
count = 0
n = 0

if H == 1:
    print(1)
else:
    while H > 0:
        H = int(H/2)
        count += 2**(n)
        n += 1
    
    print(count)