N, P = map(int, input().split())
S = list(input().rstrip())
ans = 0

if P == 2 or P == 3:
    for i in range(N):
        if int(S[i])%P==0:
            ans += i+1

else:
    dp = [0] * P
    dp[0] = 1
    t = 1
    for s in reversed(S):
        dp.append((dp[-1]+int(s)*t)%P)
        t = t*10%P