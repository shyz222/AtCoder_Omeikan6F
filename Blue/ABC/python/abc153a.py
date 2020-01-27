H, A = map(int, input().split())
ans = int(H/A)
if H > A:
    if A == 1:
        print(H)
    elif H%A == 0:
        print(ans)
    else:
        print(ans+1)
else:
    print(1)
