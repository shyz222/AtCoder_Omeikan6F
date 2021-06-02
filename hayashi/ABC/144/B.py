N = int(input())


ans = "No"
for i in range(1, 10):
    for j in range(1, 10):
        Y = i * j
        if Y == N:
            ans = "Yes"

print(ans)
