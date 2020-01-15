def makeInt(n):
    return int(n)

N, K, M = input().split(" ")

scores = list(map(makeInt,list(input().split())))

sum_now = sum(scores)
best = int(N) * int(M)

key = best - sum_now

if (key > int(K)):
    print(-1)
elif (key > 0):
    print(key)
else:
    print(0)
