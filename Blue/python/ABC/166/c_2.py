N, M = map(int, input().split())
H = list(map(int, input().split())) 
A = [0]*M
B = [0]*M

for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1

lis = [0]*N

for i in range(M):
    if H[A[i]] >= H[B[i]]:
        lis[B[i]] = -1
    if H[A[i]] <= H[B[i]]:
        lis[A[i]] = -1
    

print(lis.count(0))