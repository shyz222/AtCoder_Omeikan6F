N = int(input())

A = list(map(int, input().split()))

sorted_A = sorted(A)

count = 0
ans = "No"
for i, item in enumerate(sorted_A):
    if count == item - 1 and item == N:
        ans = "Yes"
    if count == item - 1:
        count += 1

print(ans)
