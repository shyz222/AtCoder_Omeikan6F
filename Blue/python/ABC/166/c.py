N, M = map(int, input().split())
H = list(map(int, input().split())) 
A = [0]*M
B = [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
lis = []
for i in range(M):
    if H[A[i]] < H[B[i]]:
        lis.append(A[i])
    if H[A[i]] == H[B[i]]:
        lis.append(A[i])
        lis.append(B[i])
    if H[A[i]] > H[B[i]]:
        lis.append(B[i])
print(len(H)-len(set(lis)))