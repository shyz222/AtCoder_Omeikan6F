n,m = map(int,input().split())

score_L = []
score_L = [int(input()) for val in range(n)]

score_L = sorted(score_L,reverse=True)
ans = 0
i = 0
counter = 0

while counter != 3:
    if m - score_L[i] == 0:
        ans +=score_L[i]
        counter = 3
    elif m - score_L[i] > 0:
        ans += score_L[i]
        counter += 1
    elif m - score_L[i] < 0 and i<4:
        i += 1
        counter -=1

print(ans)

