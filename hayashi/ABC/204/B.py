N = int(input())

A = list(map(int, input().split()))

sum = 0
for a in A:
    sum += max(a-10, 0)

print(sum)
