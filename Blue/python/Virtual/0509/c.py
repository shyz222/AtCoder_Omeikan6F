N = int(input())
S = [list(input()) for i in range(N)]
S.reverse()
for i in range(1,N-1):
    for j in range(1,2*N-1):
        if S[i][j] == '#':
            if S[i+1][j-1] == 'X' or S[i+1][j] == 'X' or S[i+1][j+1] == 'X':
                S[i][j] = 'X'

S.reverse()
for i in S:
    print(*i)