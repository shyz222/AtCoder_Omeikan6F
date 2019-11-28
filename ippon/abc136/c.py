n = int(input())
h = list(map(int,input().split()))
h.append(10**9)
lock = 0
for i in range(n-1):
    if h[i] +1 == h[i]:
        lock = 0
        pass
    elif f-1 == h[i+1] and lock==0:
        lock = -1
    else:
        print("No")
        exit()

print("Yes")