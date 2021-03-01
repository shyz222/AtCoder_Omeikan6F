A, B = input().split()

flag = False
for i in range(max(len(A), len(B))):
    if(A[i] < B[i]):
        print(int(B[1]) + int(B[2]) + int(B[0]))
        flag = True
        break
if(not flag):
    print(int(A[1]) + int(A[2]) + int(A[0]))
