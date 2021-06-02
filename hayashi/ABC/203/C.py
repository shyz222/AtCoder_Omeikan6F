N, K = list(map(int, input().split()))

friends = []
for i in range(N):
    friends.append(list(map(int, input().split())))

friends = sorted(friends)

amount = K

for f in friends:
    if f[0] <= amount:
        amount += f[1]
    else:
        break

print(amount)
