H, N = map(int,input().split())
A = list(input().split())

if sum(int(i) for i in A) >= H:
    print("Yes")
else:print("No")