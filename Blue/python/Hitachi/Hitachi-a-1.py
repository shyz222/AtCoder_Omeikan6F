S = str(input())
ans = 0
for i in range(0,len(S)-1,2):
    if S[i] == 'h' and S[i+1] == 'i':
        ans += 0
    else:ans += 1

if ans == 0:
    print('Yes')
else:print('No')