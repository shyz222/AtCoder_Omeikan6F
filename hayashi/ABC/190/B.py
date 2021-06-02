N, S, D = list(map(int, input().split()))
flag = False
for i in range(N):
    X, Y = list(map(int, input().split()))
    if X < S and Y > D:
        flag = True
        break
print("Yes" if flag == True else "No")
