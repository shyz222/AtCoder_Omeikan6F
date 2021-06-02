N, K = list(map(int, input().split()))

for i in range(K):
    if N % 200 == 0:
        N = int(N / 200)
        continue
    N = int(str(N) + "200")


print(N)
