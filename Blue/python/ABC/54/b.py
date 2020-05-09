N,M = map(int, input().split())
A = [list(str(input())) for i in range(N)]
B = [list(str(input())) for i in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        if B[0] == A[i][j:j+M]:
            for k in range(1,M):
                if B[k] != A[i+k][j:j+M]:
                    break
            else:
                print('Yes')
                exit()
            
print('No')