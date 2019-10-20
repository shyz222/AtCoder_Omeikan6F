N = int(input())
list = list(map(int, input().split(" ")))
S = sorted(list,reverse=True)
count = 0

while len(S) >= 3:
    for i in range(1,len(S)-1):
        if not (S[0] < S[i]+S[i+1] and S[i] < S[i+1]+S[0] and S[i+1] < S[i]+S[0]):
            del S[0]
            break
        elif (S[0] < S[i]+S[i+1] and S[i] < S[i+1]+S[0] and S[i+1] < S[i]+S[0]):
            count += 1
            # print(count)
        del S[0]

print(count)
