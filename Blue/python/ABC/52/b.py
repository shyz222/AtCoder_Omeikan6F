N = int(input())
S = str(input())
ans = 0
tmp = 0
for i in range(N):
    if S[i] == 'I':
        tmp += 1
    else:tmp -= 1

    ans = max(ans,tmp)

print(ans)