S = str(input())
ans = 0

if len(S) <= 3:
    print(ans)
else:   
    for i in range(0,len(S)-2):
        for j in range(i+3,len(S)+1):
            if int(S[i:j]) % 2019 == 0:
                ans+=1
    print(ans)