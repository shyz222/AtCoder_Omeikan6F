A = list(map(int, input().split()))
A = sorted(A)

ans = True

diff = A[0] - A[1]
for i in range(len(A) - 1):
    if A[i] - A[i+1] != diff:
        ans = False

print("Yes") if ans == True else print("No")
