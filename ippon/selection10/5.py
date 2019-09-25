n,a,b = map(int,input().split())
n += 1

ans = 0
for val in range(n):
    # 和を計算
    tmp = 0
    for i in str(val):
        tmp = tmp + int(i)

    if tmp >= a and tmp <= b:
        ans = ans + val

print(ans)
