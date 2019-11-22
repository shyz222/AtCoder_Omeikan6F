n = int(input())

ans = 0
for val in range(n):
    x,u = map(str,input().split())
    if u == "JPY":
        tanni = 1.0
    else:
        tanni = 380000.0
    ans = ans + tanni * float(x)

print(ans)
