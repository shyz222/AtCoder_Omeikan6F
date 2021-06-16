A, B = input().split()

sum_a = 0
sum_b = 0
for i in range(3):
    sum_a += int(A[i])
    sum_b += int(B[i])

print(max(sum_a, sum_b))
