N = int(input())
S = input()
Q = int(input())

for i in range(Q):
    t, a, b = map(int, input().split())
    # TLE
    # https://qiita.com/bee2/items/4ab87d05cc03d53e19f9
    if t == 1:
        sa = S[a-1]
        sb = S[b-1]
        sTop = ""
        sMiddle = S[a:b-1]
        sBottom = ""
        if a != 1:
            sTop = S[:a-1]
        if b != 2 * N:
            sBottom = S[b:]

        S = sTop + sb + sMiddle + sa + sBottom
    else:
        S = S[N:]+S[:N]
print(S)
