K = int(input())
S = str(input())
nk = S[:K]
if len(S) <= K:
    print(S)
else:print(nk + "...")